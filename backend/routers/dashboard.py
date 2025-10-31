from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, desc
from datetime import datetime, timedelta

from database import get_db
from models import User, Campaign, CampaignStatus, APIGateway, APIStatus
from schemas import DashboardStats, RecentCampaign
from auth import get_current_user
from typing import List

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/stats", response_model=DashboardStats)
async def get_dashboard_stats(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get dashboard statistics"""
    
    # Total campaigns
    total_campaigns_result = await db.execute(
        select(func.count(Campaign.id)).where(Campaign.user_id == current_user.id)
    )
    total_campaigns = total_campaigns_result.scalar()
    
    # Active campaigns
    active_campaigns_result = await db.execute(
        select(func.count(Campaign.id)).where(
            Campaign.user_id == current_user.id,
            Campaign.status == CampaignStatus.RUNNING
        )
    )
    active_campaigns = active_campaigns_result.scalar()
    
    # Completed campaigns
    completed_campaigns_result = await db.execute(
        select(func.count(Campaign.id)).where(
            Campaign.user_id == current_user.id,
            Campaign.status == CampaignStatus.COMPLETED
        )
    )
    completed_campaigns = completed_campaigns_result.scalar()
    
    # Success rate
    success_rate_result = await db.execute(
        select(func.avg(Campaign.success_rate)).where(
            Campaign.user_id == current_user.id,
            Campaign.status == CampaignStatus.COMPLETED
        )
    )
    success_rate = success_rate_result.scalar() or 0.0
    
    # Total SMS sent
    total_sms_result = await db.execute(
        select(func.sum(Campaign.successful_requests)).where(
            Campaign.user_id == current_user.id
        )
    )
    total_sms_sent = total_sms_result.scalar() or 0
    
    # SMS sent today
    today = datetime.utcnow().date()
    sms_today_result = await db.execute(
        select(func.sum(Campaign.successful_requests)).where(
            Campaign.user_id == current_user.id,
            func.date(Campaign.created_at) == today
        )
    )
    sms_sent_today = sms_today_result.scalar() or 0
    
    # Active APIs
    active_apis_result = await db.execute(
        select(func.count(APIGateway.id)).where(
            APIGateway.status == APIStatus.ACTIVE,
            APIGateway.is_enabled == True
        )
    )
    active_apis = active_apis_result.scalar()
    
    # Total APIs
    total_apis_result = await db.execute(select(func.count(APIGateway.id)))
    total_apis = total_apis_result.scalar()
    
    return DashboardStats(
        total_campaigns=total_campaigns,
        active_campaigns=active_campaigns,
        completed_campaigns=completed_campaigns,
        success_rate=round(success_rate, 2),
        total_sms_sent=total_sms_sent,
        sms_sent_today=sms_sent_today,
        active_apis=active_apis,
        total_apis=total_apis
    )


@router.get("/recent-campaigns", response_model=List[RecentCampaign])
async def get_recent_campaigns(
    limit: int = 10,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get recent campaigns"""
    
    result = await db.execute(
        select(Campaign)
        .where(Campaign.user_id == current_user.id)
        .order_by(desc(Campaign.created_at))
        .limit(limit)
    )
    campaigns = result.scalars().all()
    
    return [
        RecentCampaign(
            id=c.id,
            name=c.name,
            mode=c.mode,
            status=c.status,
            target_count=c.target_count,
            success_rate=c.success_rate,
            created_at=c.created_at
        )
        for c in campaigns
    ]


@router.get("/activity-chart")
async def get_activity_chart(
    days: int = 7,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get activity chart data for the last N days"""
    
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    
    # Get campaigns per day
    result = await db.execute(
        select(
            func.date(Campaign.created_at).label('date'),
            func.count(Campaign.id).label('count'),
            func.sum(Campaign.successful_requests).label('sms_sent')
        )
        .where(
            Campaign.user_id == current_user.id,
            Campaign.created_at >= start_date
        )
        .group_by(func.date(Campaign.created_at))
        .order_by(func.date(Campaign.created_at))
    )
    
    data = result.all()
    
    return {
        "labels": [str(row.date) for row in data],
        "campaigns": [row.count for row in data],
        "sms_sent": [row.sms_sent or 0 for row in data]
    }