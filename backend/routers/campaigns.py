from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc
from typing import List, Optional
from datetime import datetime

from database import get_db
from models import User, Campaign, CampaignLog, CampaignStatus
from schemas import (
    CampaignCreate, CampaignUpdate, CampaignResponse,
    CampaignLogResponse, SuccessResponse
)
from auth import get_current_user
from task_manager import get_task_manager

router = APIRouter(prefix="/campaigns", tags=["Campaigns"])


@router.post("", response_model=CampaignResponse, status_code=status.HTTP_201_CREATED)
async def create_campaign(
    campaign_data: CampaignCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create a new campaign"""
    
    # Create campaign
    new_campaign = Campaign(
        user_id=current_user.id,
        name=campaign_data.name,
        description=campaign_data.description,
        mode=campaign_data.mode,
        targets=campaign_data.targets,
        target_count=len(campaign_data.targets),
        waves=campaign_data.waves,
        delay_seconds=campaign_data.delay_seconds,
        use_proxy=campaign_data.use_proxy,
        use_vpn=campaign_data.use_vpn,
        randomize_apis=campaign_data.randomize_apis,
        status=CampaignStatus.PENDING
    )
    
    db.add(new_campaign)
    await db.commit()
    await db.refresh(new_campaign)
    
    return new_campaign


@router.get("", response_model=List[CampaignResponse])
async def get_campaigns(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    status: Optional[CampaignStatus] = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get all campaigns for current user"""
    
    query = select(Campaign).where(Campaign.user_id == current_user.id)
    
    if status:
        query = query.where(Campaign.status == status)
    
    query = query.order_by(desc(Campaign.created_at)).offset(skip).limit(limit)
    
    result = await db.execute(query)
    campaigns = result.scalars().all()
    
    return campaigns


@router.get("/{campaign_id}", response_model=CampaignResponse)
async def get_campaign(
    campaign_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get a specific campaign"""
    
    result = await db.execute(
        select(Campaign).where(
            Campaign.id == campaign_id,
            Campaign.user_id == current_user.id
        )
    )
    campaign = result.scalar_one_or_none()
    
    if not campaign:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found"
        )
    
    return campaign


@router.patch("/{campaign_id}", response_model=CampaignResponse)
async def update_campaign(
    campaign_id: int,
    campaign_data: CampaignUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update a campaign"""
    
    result = await db.execute(
        select(Campaign).where(
            Campaign.id == campaign_id,
            Campaign.user_id == current_user.id
        )
    )
    campaign = result.scalar_one_or_none()
    
    if not campaign:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found"
        )
    
    # Update fields
    update_data = campaign_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(campaign, field, value)
    
    campaign.updated_at = datetime.utcnow()
    
    await db.commit()
    await db.refresh(campaign)
    
    return campaign


@router.delete("/{campaign_id}", response_model=SuccessResponse)
async def delete_campaign(
    campaign_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Delete a campaign"""
    
    result = await db.execute(
        select(Campaign).where(
            Campaign.id == campaign_id,
            Campaign.user_id == current_user.id
        )
    )
    campaign = result.scalar_one_or_none()
    
    if not campaign:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found"
        )
    
    await db.delete(campaign)
    await db.commit()
    
    return SuccessResponse(
        success=True,
        message="Campaign deleted successfully"
    )


@router.post("/{campaign_id}/start", response_model=CampaignResponse)
async def start_campaign(
    campaign_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Start a campaign"""
    
    result = await db.execute(
        select(Campaign).where(
            Campaign.id == campaign_id,
            Campaign.user_id == current_user.id
        )
    )
    campaign = result.scalar_one_or_none()
    
    if not campaign:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found"
        )
    
    if campaign.status not in [CampaignStatus.PENDING, CampaignStatus.PAUSED]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Cannot start campaign with status: {campaign.status}"
        )
    
    campaign.status = CampaignStatus.RUNNING
    campaign.started_at = datetime.utcnow()
    
    await db.commit()
    await db.refresh(campaign)
    
    # Start campaign execution in background
    task_manager = get_task_manager()
    success = await task_manager.start_campaign(campaign.id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to start campaign execution"
        )
    
    return campaign


@router.post("/{campaign_id}/pause", response_model=CampaignResponse)
async def pause_campaign(
    campaign_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Pause a running campaign"""
    
    result = await db.execute(
        select(Campaign).where(
            Campaign.id == campaign_id,
            Campaign.user_id == current_user.id
        )
    )
    campaign = result.scalar_one_or_none()
    
    if not campaign:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found"
        )
    
    if campaign.status != CampaignStatus.RUNNING:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can only pause running campaigns"
        )
    
    campaign.status = CampaignStatus.PAUSED
    
    await db.commit()
    await db.refresh(campaign)
    
    return campaign


@router.post("/{campaign_id}/cancel", response_model=CampaignResponse)
async def cancel_campaign(
    campaign_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Cancel a campaign"""
    
    result = await db.execute(
        select(Campaign).where(
            Campaign.id == campaign_id,
            Campaign.user_id == current_user.id
        )
    )
    campaign = result.scalar_one_or_none()
    
    if not campaign:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found"
        )
    
    if campaign.status in [CampaignStatus.COMPLETED, CampaignStatus.CANCELLED]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Cannot cancel campaign with status: {campaign.status}"
        )
    
    campaign.status = CampaignStatus.CANCELLED
    campaign.completed_at = datetime.utcnow()
    
    if campaign.started_at:
        campaign.duration_seconds = int((campaign.completed_at - campaign.started_at).total_seconds())
    
    await db.commit()
    await db.refresh(campaign)
    
    return campaign


@router.get("/{campaign_id}/logs", response_model=List[CampaignLogResponse])
async def get_campaign_logs(
    campaign_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get logs for a campaign"""
    
    # Verify campaign belongs to user
    result = await db.execute(
        select(Campaign).where(
            Campaign.id == campaign_id,
            Campaign.user_id == current_user.id
        )
    )
    campaign = result.scalar_one_or_none()
    
    if not campaign:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found"
        )
    
    # Get logs
    result = await db.execute(
        select(CampaignLog)
        .where(CampaignLog.campaign_id == campaign_id)
        .order_by(desc(CampaignLog.created_at))
        .offset(skip)
        .limit(limit)
    )
    logs = result.scalars().all()
    
    return logs


@router.get("/{campaign_id}/status")
async def get_campaign_execution_status(
    campaign_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get real-time execution status of a campaign"""
    
    # Verify campaign belongs to user
    result = await db.execute(
        select(Campaign).where(
            Campaign.id == campaign_id,
            Campaign.user_id == current_user.id
        )
    )
    campaign = result.scalar_one_or_none()
    
    if not campaign:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found"
        )
    
    # Check if running in background
    task_manager = get_task_manager()
    is_running = task_manager.is_running(campaign_id)
    
    # Calculate progress
    progress = 0.0
    if campaign.target_count > 0 and campaign.waves > 0:
        total_expected = campaign.target_count * campaign.waves
        progress = (campaign.total_requests / total_expected) * 100 if total_expected > 0 else 0
    
    # Estimate time remaining
    time_remaining = None
    if campaign.started_at and campaign.total_requests > 0:
        elapsed = (datetime.utcnow() - campaign.started_at).total_seconds()
        rate = campaign.total_requests / elapsed if elapsed > 0 else 0
        
        if rate > 0:
            total_expected = campaign.target_count * campaign.waves
            remaining_requests = total_expected - campaign.total_requests
            time_remaining = int(remaining_requests / rate)
    
    return {
        "campaign_id": campaign.id,
        "status": campaign.status,
        "is_running": is_running,
        "progress_percentage": round(progress, 2),
        "total_requests": campaign.total_requests,
        "successful_requests": campaign.successful_requests,
        "failed_requests": campaign.failed_requests,
        "success_rate": round(campaign.success_rate, 2),
        "started_at": campaign.started_at,
        "estimated_time_remaining_seconds": time_remaining,
        "current_wave": min(
            int(campaign.total_requests / campaign.target_count) + 1 if campaign.target_count > 0 else 1,
            campaign.waves
        ),
        "total_waves": campaign.waves
    }


@router.get("/running/list")
async def get_running_campaigns(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get list of currently running campaigns"""
    
    task_manager = get_task_manager()
    running_ids = task_manager.get_running_campaigns()
    
    # Get campaign details
    if running_ids:
        result = await db.execute(
            select(Campaign).where(
                Campaign.id.in_(running_ids),
                Campaign.user_id == current_user.id
            )
        )
        campaigns = result.scalars().all()
    else:
        campaigns = []
    
    return {
        "count": len(campaigns),
        "campaigns": [
            {
                "id": c.id,
                "name": c.name,
                "status": c.status,
                "progress": round(
                    (c.total_requests / (c.target_count * c.waves) * 100)
                    if c.target_count > 0 and c.waves > 0 else 0,
                    2
                )
            }
            for c in campaigns
        ]
    }