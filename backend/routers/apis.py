from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc
from typing import List, Optional

from database import get_db
from models import User, APIGateway, APIStatus
from schemas import (
    APIGatewayCreate, APIGatewayUpdate, APIGatewayResponse,
    SuccessResponse
)
from auth import get_current_admin_user, get_current_user

router = APIRouter(prefix="/apis", tags=["API Gateways"])


@router.post("", response_model=APIGatewayResponse, status_code=status.HTTP_201_CREATED)
async def create_api_gateway(
    api_data: APIGatewayCreate,
    current_user: User = Depends(get_current_admin_user),
    db: AsyncSession = Depends(get_db)
):
    """Create a new API gateway (Admin only)"""
    
    # Check if name exists
    result = await db.execute(select(APIGateway).where(APIGateway.name == api_data.name))
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="API gateway with this name already exists"
        )
    
    # Create API gateway
    new_api = APIGateway(**api_data.model_dump())
    
    db.add(new_api)
    await db.commit()
    await db.refresh(new_api)
    
    return new_api


@router.get("", response_model=List[APIGatewayResponse])
async def get_api_gateways(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status: Optional[APIStatus] = None,
    is_enabled: Optional[bool] = None,
    search: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get all API gateways"""
    
    query = select(APIGateway)
    
    if status:
        query = query.where(APIGateway.status == status)
    
    if is_enabled is not None:
        query = query.where(APIGateway.is_enabled == is_enabled)
    
    if search:
        query = query.where(
            (APIGateway.name.ilike(f"%{search}%")) |
            (APIGateway.provider.ilike(f"%{search}%")) |
            (APIGateway.country.ilike(f"%{search}%"))
        )
    
    query = query.order_by(desc(APIGateway.priority), APIGateway.name).offset(skip).limit(limit)
    
    result = await db.execute(query)
    apis = result.scalars().all()
    
    return apis


@router.get("/{api_id}", response_model=APIGatewayResponse)
async def get_api_gateway(
    api_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get a specific API gateway"""
    
    result = await db.execute(select(APIGateway).where(APIGateway.id == api_id))
    api = result.scalar_one_or_none()
    
    if not api:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="API gateway not found"
        )
    
    return api


@router.patch("/{api_id}", response_model=APIGatewayResponse)
async def update_api_gateway(
    api_id: int,
    api_data: APIGatewayUpdate,
    current_user: User = Depends(get_current_admin_user),
    db: AsyncSession = Depends(get_db)
):
    """Update an API gateway (Admin only)"""
    
    result = await db.execute(select(APIGateway).where(APIGateway.id == api_id))
    api = result.scalar_one_or_none()
    
    if not api:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="API gateway not found"
        )
    
    # Update fields
    update_data = api_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(api, field, value)
    
    await db.commit()
    await db.refresh(api)
    
    return api


@router.delete("/{api_id}", response_model=SuccessResponse)
async def delete_api_gateway(
    api_id: int,
    current_user: User = Depends(get_current_admin_user),
    db: AsyncSession = Depends(get_db)
):
    """Delete an API gateway (Admin only)"""
    
    result = await db.execute(select(APIGateway).where(APIGateway.id == api_id))
    api = result.scalar_one_or_none()
    
    if not api:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="API gateway not found"
        )
    
    await db.delete(api)
    await db.commit()
    
    return SuccessResponse(
        success=True,
        message="API gateway deleted successfully"
    )


@router.get("/stats/summary")
async def get_api_stats_summary(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get API statistics summary"""
    
    # Total APIs
    total_result = await db.execute(select(func.count(APIGateway.id)))
    total_apis = total_result.scalar()
    
    # Active APIs
    active_result = await db.execute(
        select(func.count(APIGateway.id)).where(
            APIGateway.status == APIStatus.ACTIVE,
            APIGateway.is_enabled == True
        )
    )
    active_apis = active_result.scalar()
    
    # Average success rate
    avg_success_result = await db.execute(
        select(func.avg(APIGateway.success_rate)).where(
            APIGateway.is_enabled == True
        )
    )
    avg_success_rate = avg_success_result.scalar() or 0.0
    
    # Average response time
    avg_response_result = await db.execute(
        select(func.avg(APIGateway.avg_response_time_ms)).where(
            APIGateway.is_enabled == True
        )
    )
    avg_response_time = avg_response_result.scalar() or 0
    
    return {
        "total_apis": total_apis,
        "active_apis": active_apis,
        "inactive_apis": total_apis - active_apis,
        "avg_success_rate": round(avg_success_rate, 2),
        "avg_response_time_ms": int(avg_response_time)
    }