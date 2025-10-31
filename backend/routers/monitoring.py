"""
Monitoring and Health Check Router
Provides system health, metrics, and monitoring endpoints
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from datetime import datetime, timedelta

from database import get_db
from models import Campaign, APIGateway, CampaignLog, CampaignStatus, APIStatus, User
from auth import get_current_user, get_current_admin_user
from task_manager import get_task_manager

router = APIRouter(prefix="/monitoring", tags=["Monitoring"])


@router.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    """Comprehensive health check"""
    
    try:
        # Check database
        await db.execute(select(1))
        db_healthy = True
    except Exception:
        db_healthy = False
    
    # Check task manager
    task_manager = get_task_manager()
    running_campaigns = len(task_manager.get_running_campaigns())
    
    # Overall health
    healthy = db_healthy
    
    return {
        "status": "healthy" if healthy else "unhealthy",
        "timestamp": datetime.utcnow(),
        "components": {
            "database": "healthy" if db_healthy else "unhealthy",
            "task_manager": "healthy",
            "running_campaigns": running_campaigns
        }
    }


@router.get("/metrics")
async def get_metrics(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get system metrics"""
    
    # Campaign metrics
    total_campaigns = await db.execute(select(func.count(Campaign.id)))
    total_campaigns = total_campaigns.scalar()
    
    running_campaigns = await db.execute(
        select(func.count(Campaign.id)).where(Campaign.status == CampaignStatus.RUNNING)
    )
    running_campaigns = running_campaigns.scalar()
    
    completed_campaigns = await db.execute(
        select(func.count(Campaign.id)).where(Campaign.status == CampaignStatus.COMPLETED)
    )
    completed_campaigns = completed_campaigns.scalar()
    
    # API metrics
    total_apis = await db.execute(select(func.count(APIGateway.id)))
    total_apis = total_apis.scalar()
    
    active_apis = await db.execute(
        select(func.count(APIGateway.id)).where(
            APIGateway.status == APIStatus.ACTIVE,
            APIGateway.is_enabled == True
        )
    )
    active_apis = active_apis.scalar()
    
    # Request metrics (last 24 hours)
    yesterday = datetime.utcnow() - timedelta(days=1)
    
    recent_logs = await db.execute(
        select(
            func.count(CampaignLog.id).label('total'),
            func.sum(func.case((CampaignLog.status == 'success', 1), else_=0)).label('successful')
        ).where(CampaignLog.created_at >= yesterday)
    )
    log_stats = recent_logs.first()
    
    total_requests_24h = log_stats.total or 0
    successful_requests_24h = log_stats.successful or 0
    success_rate_24h = (
        (successful_requests_24h / total_requests_24h * 100)
        if total_requests_24h > 0 else 0
    )
    
    # User metrics
    total_users = await db.execute(select(func.count(User.id)))
    total_users = total_users.scalar()
    
    active_users_24h = await db.execute(
        select(func.count(func.distinct(User.id)))
        .join(Campaign, Campaign.user_id == User.id)
        .where(Campaign.created_at >= yesterday)
    )
    active_users_24h = active_users_24h.scalar()
    
    return {
        "timestamp": datetime.utcnow(),
        "campaigns": {
            "total": total_campaigns,
            "running": running_campaigns,
            "completed": completed_campaigns,
            "success_rate": round(
                (completed_campaigns / total_campaigns * 100)
                if total_campaigns > 0 else 0,
                2
            )
        },
        "apis": {
            "total": total_apis,
            "active": active_apis,
            "inactive": total_apis - active_apis
        },
        "requests_24h": {
            "total": total_requests_24h,
            "successful": successful_requests_24h,
            "failed": total_requests_24h - successful_requests_24h,
            "success_rate": round(success_rate_24h, 2)
        },
        "users": {
            "total": total_users,
            "active_24h": active_users_24h
        }
    }


@router.get("/api-health")
async def check_api_health(
    current_user: User = Depends(get_current_admin_user),
    db: AsyncSession = Depends(get_db)
):
    """Check health of all API gateways"""
    
    result = await db.execute(
        select(APIGateway).where(APIGateway.is_enabled == True)
    )
    apis = result.scalars().all()
    
    api_health = []
    for api in apis:
        # Calculate health score
        health_score = 100
        
        # Deduct for failures
        if api.consecutive_failures > 0:
            health_score -= min(api.consecutive_failures * 10, 50)
        
        # Deduct for low success rate
        if api.success_rate < 90:
            health_score -= (90 - api.success_rate)
        
        # Deduct for high response time
        if api.avg_response_time_ms > 5000:
            health_score -= 20
        elif api.avg_response_time_ms > 3000:
            health_score -= 10
        
        health_score = max(0, health_score)
        
        # Determine status
        if health_score >= 80:
            health_status = "excellent"
        elif health_score >= 60:
            health_status = "good"
        elif health_score >= 40:
            health_status = "fair"
        else:
            health_status = "poor"
        
        api_health.append({
            "id": api.id,
            "name": api.name,
            "status": api.status,
            "health_score": health_score,
            "health_status": health_status,
            "success_rate": round(api.success_rate, 2),
            "avg_response_time_ms": api.avg_response_time_ms,
            "consecutive_failures": api.consecutive_failures,
            "last_checked": api.last_checked,
            "last_success": api.last_success,
            "last_failure": api.last_failure
        })
    
    # Sort by health score
    api_health.sort(key=lambda x: x['health_score'], reverse=True)
    
    return {
        "timestamp": datetime.utcnow(),
        "total_apis": len(api_health),
        "healthy_apis": sum(1 for a in api_health if a['health_score'] >= 60),
        "unhealthy_apis": sum(1 for a in api_health if a['health_score'] < 60),
        "apis": api_health
    }


@router.get("/performance")
async def get_performance_stats(
    hours: int = 24,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get performance statistics for specified time period"""
    
    since = datetime.utcnow() - timedelta(hours=hours)
    
    # Get logs in time period
    result = await db.execute(
        select(CampaignLog).where(CampaignLog.created_at >= since)
    )
    logs = result.scalars().all()
    
    if not logs:
        return {
            "period_hours": hours,
            "total_requests": 0,
            "avg_response_time_ms": 0,
            "success_rate": 0,
            "requests_per_hour": 0
        }
    
    # Calculate statistics
    total_requests = len(logs)
    successful = sum(1 for log in logs if log.status == 'success')
    
    response_times = [
        log.response_time_ms
        for log in logs
        if log.response_time_ms is not None
    ]
    
    avg_response_time = (
        sum(response_times) / len(response_times)
        if response_times else 0
    )
    
    success_rate = (successful / total_requests * 100) if total_requests > 0 else 0
    
    requests_per_hour = total_requests / hours
    
    # API performance breakdown
    api_performance = {}
    for log in logs:
        if log.api_name not in api_performance:
            api_performance[log.api_name] = {
                'total': 0,
                'successful': 0,
                'response_times': []
            }
        
        api_performance[log.api_name]['total'] += 1
        if log.status == 'success':
            api_performance[log.api_name]['successful'] += 1
        if log.response_time_ms:
            api_performance[log.api_name]['response_times'].append(log.response_time_ms)
    
    # Calculate per-API stats
    api_stats = []
    for api_name, stats in api_performance.items():
        avg_rt = (
            sum(stats['response_times']) / len(stats['response_times'])
            if stats['response_times'] else 0
        )
        
        api_stats.append({
            'api_name': api_name,
            'total_requests': stats['total'],
            'successful_requests': stats['successful'],
            'success_rate': round(
                (stats['successful'] / stats['total'] * 100)
                if stats['total'] > 0 else 0,
                2
            ),
            'avg_response_time_ms': round(avg_rt, 2)
        })
    
    # Sort by total requests
    api_stats.sort(key=lambda x: x['total_requests'], reverse=True)
    
    return {
        "period_hours": hours,
        "timestamp": datetime.utcnow(),
        "total_requests": total_requests,
        "successful_requests": successful,
        "failed_requests": total_requests - successful,
        "success_rate": round(success_rate, 2),
        "avg_response_time_ms": round(avg_response_time, 2),
        "requests_per_hour": round(requests_per_hour, 2),
        "api_performance": api_stats
    }