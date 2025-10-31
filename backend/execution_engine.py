"""
Campaign Execution Engine - Phase 4
Handles background task processing, SMS API integration, rate limiting, and retry logic
"""

import asyncio
import time
import random
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
import httpx
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)

from models import Campaign, CampaignLog, APIGateway, CampaignStatus, APIStatus
from config import settings
import logging

logger = logging.getLogger(__name__)


class RateLimiter:
    """Rate limiter for API requests"""
    
    def __init__(self):
        self.api_counters: Dict[int, Dict[str, Any]] = {}
        self.lock = asyncio.Lock()
    
    async def can_make_request(self, api_id: int, rate_per_minute: int, rate_per_hour: int) -> bool:
        """Check if API can handle another request"""
        async with self.lock:
            now = datetime.utcnow()
            
            if api_id not in self.api_counters:
                self.api_counters[api_id] = {
                    'minute_count': 0,
                    'hour_count': 0,
                    'minute_reset': now + timedelta(minutes=1),
                    'hour_reset': now + timedelta(hours=1)
                }
            
            counter = self.api_counters[api_id]
            
            # Reset counters if needed
            if now >= counter['minute_reset']:
                counter['minute_count'] = 0
                counter['minute_reset'] = now + timedelta(minutes=1)
            
            if now >= counter['hour_reset']:
                counter['hour_count'] = 0
                counter['hour_reset'] = now + timedelta(hours=1)
            
            # Check limits
            if counter['minute_count'] >= rate_per_minute:
                return False
            if counter['hour_count'] >= rate_per_hour:
                return False
            
            return True
    
    async def increment_counter(self, api_id: int):
        """Increment request counter for API"""
        async with self.lock:
            if api_id in self.api_counters:
                self.api_counters[api_id]['minute_count'] += 1
                self.api_counters[api_id]['hour_count'] += 1


class SMSAPIClient:
    """Client for making SMS API requests with retry logic"""
    
    def __init__(self):
        self.client = httpx.AsyncClient(
            timeout=settings.request_timeout,
            follow_redirects=True
        )
        self.rate_limiter = RateLimiter()
    
    async def close(self):
        """Close HTTP client"""
        await self.client.aclose()
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type((httpx.TimeoutException, httpx.NetworkError))
    )
    async def send_sms(
        self,
        api: APIGateway,
        target: str,
        message: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send SMS via API gateway with retry logic
        
        Returns:
            Dict with status, response_code, response_time_ms, error info
        """
        start_time = time.time()
        
        try:
            # Check rate limit
            can_proceed = await self.rate_limiter.can_make_request(
                api.id,
                api.rate_limit_per_minute,
                api.rate_limit_per_hour
            )
            
            if not can_proceed:
                return {
                    'status': 'rate_limited',
                    'response_code': 429,
                    'response_time_ms': 0,
                    'error_type': 'RateLimitError',
                    'error_message': 'API rate limit exceeded'
                }
            
            # Prepare request
            url = api.url.replace('{phone}', target).replace('{target}', target)
            headers = api.headers or {}
            
            # Prepare payload
            payload = {}
            if api.payload_template:
                payload = api.payload_template.copy()
                # Replace placeholders
                payload = self._replace_placeholders(payload, target, message)
            
            # Make request
            if api.method.upper() == 'GET':
                response = await self.client.get(url, headers=headers, params=payload)
            elif api.method.upper() == 'POST':
                response = await self.client.post(url, headers=headers, json=payload)
            elif api.method.upper() == 'PUT':
                response = await self.client.put(url, headers=headers, json=payload)
            else:
                response = await self.client.request(api.method, url, headers=headers, json=payload)
            
            # Increment counter
            await self.rate_limiter.increment_counter(api.id)
            
            # Calculate response time
            response_time_ms = int((time.time() - start_time) * 1000)
            
            # Check response
            if response.status_code in [200, 201, 202]:
                return {
                    'status': 'success',
                    'response_code': response.status_code,
                    'response_time_ms': response_time_ms,
                    'response_message': response.text[:500] if response.text else None,
                    'error_type': None,
                    'error_message': None
                }
            else:
                return {
                    'status': 'failed',
                    'response_code': response.status_code,
                    'response_time_ms': response_time_ms,
                    'response_message': response.text[:500] if response.text else None,
                    'error_type': 'HTTPError',
                    'error_message': f'HTTP {response.status_code}: {response.text[:200]}'
                }
        
        except httpx.TimeoutException as e:
            response_time_ms = int((time.time() - start_time) * 1000)
            return {
                'status': 'error',
                'response_code': 408,
                'response_time_ms': response_time_ms,
                'error_type': 'TimeoutError',
                'error_message': str(e)
            }
        
        except httpx.NetworkError as e:
            response_time_ms = int((time.time() - start_time) * 1000)
            return {
                'status': 'error',
                'response_code': 0,
                'response_time_ms': response_time_ms,
                'error_type': 'NetworkError',
                'error_message': str(e)
            }
        
        except Exception as e:
            response_time_ms = int((time.time() - start_time) * 1000)
            logger.error(f"Unexpected error sending SMS: {e}")
            return {
                'status': 'error',
                'response_code': 0,
                'response_time_ms': response_time_ms,
                'error_type': type(e).__name__,
                'error_message': str(e)
            }
    
    def _replace_placeholders(self, payload: Dict, target: str, message: Optional[str]) -> Dict:
        """Replace placeholders in payload template"""
        import json
        
        # Convert to string, replace, convert back
        payload_str = json.dumps(payload)
        payload_str = payload_str.replace('{phone}', target)
        payload_str = payload_str.replace('{target}', target)
        payload_str = payload_str.replace('{number}', target)
        
        if message:
            payload_str = payload_str.replace('{message}', message)
        
        return json.loads(payload_str)


class CampaignExecutor:
    """Executes campaigns with wave-based SMS sending"""
    
    def __init__(self, db_session: AsyncSession):
        self.db = db_session
        self.sms_client = SMSAPIClient()
        self.active_campaigns: Dict[int, bool] = {}
    
    async def close(self):
        """Close resources"""
        await self.sms_client.close()
    
    async def execute_campaign(self, campaign_id: int):
        """
        Execute a campaign with all its waves
        
        This is the main entry point for campaign execution
        """
        try:
            # Mark campaign as active
            self.active_campaigns[campaign_id] = True
            
            # Get campaign
            result = await self.db.execute(
                select(Campaign).where(Campaign.id == campaign_id)
            )
            campaign = result.scalar_one_or_none()
            
            if not campaign:
                logger.error(f"Campaign {campaign_id} not found")
                return
            
            # Update campaign status
            campaign.status = CampaignStatus.RUNNING
            campaign.started_at = datetime.utcnow()
            await self.db.commit()
            
            logger.info(f"Starting campaign {campaign_id}: {campaign.name}")
            
            # Get active APIs
            apis = await self._get_active_apis()
            
            if not apis:
                logger.error("No active APIs available")
                campaign.status = CampaignStatus.FAILED
                campaign.completed_at = datetime.utcnow()
                await self.db.commit()
                return
            
            # Execute waves
            for wave_num in range(1, campaign.waves + 1):
                # Check if campaign is still active
                if not self.active_campaigns.get(campaign_id, False):
                    logger.info(f"Campaign {campaign_id} stopped by user")
                    break
                
                # Refresh campaign status
                await self.db.refresh(campaign)
                if campaign.status == CampaignStatus.PAUSED:
                    logger.info(f"Campaign {campaign_id} paused, waiting...")
                    await self._wait_for_resume(campaign_id)
                
                if campaign.status == CampaignStatus.CANCELLED:
                    logger.info(f"Campaign {campaign_id} cancelled")
                    break
                
                logger.info(f"Campaign {campaign_id} - Wave {wave_num}/{campaign.waves}")
                
                # Execute wave
                await self._execute_wave(campaign, apis, wave_num)
                
                # Delay between waves (except last wave)
                if wave_num < campaign.waves:
                    await asyncio.sleep(campaign.delay_seconds)
            
            # Mark campaign as completed
            campaign.status = CampaignStatus.COMPLETED
            campaign.completed_at = datetime.utcnow()
            
            if campaign.started_at:
                campaign.duration_seconds = int(
                    (campaign.completed_at - campaign.started_at).total_seconds()
                )
            
            # Calculate final success rate
            if campaign.total_requests > 0:
                campaign.success_rate = (
                    campaign.successful_requests / campaign.total_requests
                ) * 100
            
            await self.db.commit()
            
            logger.info(
                f"Campaign {campaign_id} completed: "
                f"{campaign.successful_requests}/{campaign.total_requests} successful "
                f"({campaign.success_rate:.2f}%)"
            )
        
        except Exception as e:
            logger.error(f"Error executing campaign {campaign_id}: {e}")
            
            # Mark campaign as failed
            result = await self.db.execute(
                select(Campaign).where(Campaign.id == campaign_id)
            )
            campaign = result.scalar_one_or_none()
            
            if campaign:
                campaign.status = CampaignStatus.FAILED
                campaign.completed_at = datetime.utcnow()
                await self.db.commit()
        
        finally:
            # Remove from active campaigns
            self.active_campaigns.pop(campaign_id, None)
    
    async def _execute_wave(
        self,
        campaign: Campaign,
        apis: List[APIGateway],
        wave_num: int
    ):
        """Execute a single wave of SMS sending"""
        
        # Shuffle APIs if randomization is enabled
        if campaign.randomize_apis:
            apis_to_use = random.sample(apis, len(apis))
        else:
            apis_to_use = sorted(apis, key=lambda x: x.priority, reverse=True)
        
        # Create tasks for all targets
        tasks = []
        for target in campaign.targets:
            # Select API for this target
            api = apis_to_use[len(tasks) % len(apis_to_use)]
            
            # Create task
            task = self._send_sms_and_log(campaign, api, target, wave_num)
            tasks.append(task)
        
        # Execute with concurrency limit
        semaphore = asyncio.Semaphore(settings.max_concurrent_requests)
        
        async def bounded_task(task):
            async with semaphore:
                return await task
        
        # Execute all tasks
        results = await asyncio.gather(
            *[bounded_task(task) for task in tasks],
            return_exceptions=True
        )
        
        # Update campaign statistics
        successful = sum(1 for r in results if r and r.get('status') == 'success')
        failed = sum(1 for r in results if r and r.get('status') != 'success')
        
        campaign.total_requests += len(results)
        campaign.successful_requests += successful
        campaign.failed_requests += failed
        
        if campaign.total_requests > 0:
            campaign.success_rate = (
                campaign.successful_requests / campaign.total_requests
            ) * 100
        
        await self.db.commit()
    
    async def _send_sms_and_log(
        self,
        campaign: Campaign,
        api: APIGateway,
        target: str,
        wave_num: int
    ) -> Dict[str, Any]:
        """Send SMS and create log entry"""
        
        # Send SMS
        result = await self.sms_client.send_sms(api, target)
        
        # Create log entry
        log = CampaignLog(
            campaign_id=campaign.id,
            target=target,
            api_name=api.name,
            status=result['status'],
            response_code=result.get('response_code'),
            response_message=result.get('response_message'),
            response_time_ms=result.get('response_time_ms'),
            error_type=result.get('error_type'),
            error_message=result.get('error_message')
        )
        
        self.db.add(log)
        
        # Update API statistics
        api.total_requests += 1
        
        if result['status'] == 'success':
            api.successful_requests += 1
            api.last_success = datetime.utcnow()
            api.consecutive_failures = 0
        else:
            api.failed_requests += 1
            api.last_failure = datetime.utcnow()
            api.consecutive_failures += 1
        
        # Update success rate
        if api.total_requests > 0:
            api.success_rate = (api.successful_requests / api.total_requests) * 100
        
        # Update average response time
        if result.get('response_time_ms'):
            if api.avg_response_time_ms == 0:
                api.avg_response_time_ms = result['response_time_ms']
            else:
                # Moving average
                api.avg_response_time_ms = int(
                    (api.avg_response_time_ms * 0.9) + (result['response_time_ms'] * 0.1)
                )
        
        # Update API status based on consecutive failures
        if api.consecutive_failures >= 5:
            api.status = APIStatus.ERROR
        elif api.consecutive_failures >= 3:
            api.status = APIStatus.RATE_LIMITED
        else:
            api.status = APIStatus.ACTIVE
        
        api.last_checked = datetime.utcnow()
        
        await self.db.commit()
        
        return result
    
    async def _get_active_apis(self) -> List[APIGateway]:
        """Get all active and enabled API gateways"""
        result = await self.db.execute(
            select(APIGateway).where(
                APIGateway.is_enabled == True,
                APIGateway.status.in_([APIStatus.ACTIVE, APIStatus.RATE_LIMITED])
            )
        )
        return list(result.scalars().all())
    
    async def _wait_for_resume(self, campaign_id: int):
        """Wait for campaign to be resumed"""
        while True:
            await asyncio.sleep(5)
            
            result = await self.db.execute(
                select(Campaign).where(Campaign.id == campaign_id)
            )
            campaign = result.scalar_one_or_none()
            
            if not campaign or campaign.status != CampaignStatus.PAUSED:
                break
    
    async def stop_campaign(self, campaign_id: int):
        """Stop a running campaign"""
        self.active_campaigns[campaign_id] = False


# Global executor instance
_executor: Optional[CampaignExecutor] = None


async def get_executor(db: AsyncSession) -> CampaignExecutor:
    """Get or create campaign executor"""
    global _executor
    if _executor is None:
        _executor = CampaignExecutor(db)
    return _executor


async def close_executor():
    """Close executor and cleanup resources"""
    global _executor
    if _executor:
        await _executor.close()
        _executor = None