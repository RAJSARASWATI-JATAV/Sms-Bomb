from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, List, Dict, Any
from datetime import datetime
from models import UserRole, CampaignStatus, CampaignMode, APIStatus


# ============= User Schemas =============

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=100)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int
    role: UserRole
    is_active: bool
    is_verified: bool
    created_at: datetime
    last_login: Optional[datetime] = None
    
    model_config = {"from_attributes": True}


# ============= Auth Schemas =============

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None


class LoginRequest(BaseModel):
    username: str
    password: str
    remember_me: bool = False


# ============= Settings Schemas =============

class UserSettingsBase(BaseModel):
    theme: str = "dark"
    language: str = "en"
    timezone: str = "UTC"
    email_notifications: bool = True
    push_notifications: bool = True
    telegram_notifications: bool = False
    telegram_chat_id: Optional[str] = None
    two_factor_enabled: bool = False
    session_timeout: int = 30
    default_mode: CampaignMode = CampaignMode.NORMAL
    default_waves: int = 1
    default_delay: int = 5


class UserSettingsUpdate(BaseModel):
    theme: Optional[str] = None
    language: Optional[str] = None
    timezone: Optional[str] = None
    email_notifications: Optional[bool] = None
    push_notifications: Optional[bool] = None
    telegram_notifications: Optional[bool] = None
    telegram_chat_id: Optional[str] = None
    two_factor_enabled: Optional[bool] = None
    session_timeout: Optional[int] = None
    default_mode: Optional[CampaignMode] = None
    default_waves: Optional[int] = None
    default_delay: Optional[int] = None


class UserSettingsResponse(UserSettingsBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = {"from_attributes": True}


# ============= Campaign Schemas =============

class CampaignBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    mode: CampaignMode = CampaignMode.NORMAL
    targets: List[str] = Field(..., min_length=1)
    waves: int = Field(default=1, ge=1, le=100)
    delay_seconds: int = Field(default=5, ge=1, le=60)
    use_proxy: bool = False
    use_vpn: bool = False
    randomize_apis: bool = True
    
    @field_validator('targets')
    @classmethod
    def validate_targets(cls, v):
        if not v:
            raise ValueError('At least one target is required')
        if len(v) > 1000:
            raise ValueError('Maximum 1000 targets allowed')
        return v


class CampaignCreate(CampaignBase):
    pass


class CampaignUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[CampaignStatus] = None


class CampaignResponse(CampaignBase):
    id: int
    user_id: int
    status: CampaignStatus
    target_count: int
    total_requests: int
    successful_requests: int
    failed_requests: int
    success_rate: float
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    estimated_completion: Optional[datetime] = None
    duration_seconds: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = {"from_attributes": True}


# ============= Campaign Log Schemas =============

class CampaignLogResponse(BaseModel):
    id: int
    campaign_id: int
    target: str
    api_name: str
    status: str
    response_code: Optional[int] = None
    response_message: Optional[str] = None
    response_time_ms: Optional[int] = None
    error_type: Optional[str] = None
    error_message: Optional[str] = None
    created_at: datetime
    
    model_config = {"from_attributes": True}


# ============= API Gateway Schemas =============

class APIGatewayBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    url: str = Field(..., min_length=1, max_length=500)
    method: str = Field(default="POST", pattern="^(GET|POST|PUT|DELETE)$")
    headers: Optional[Dict[str, str]] = None
    payload_template: Optional[Dict[str, Any]] = None
    is_enabled: bool = True
    rate_limit_per_minute: int = Field(default=60, ge=1)
    rate_limit_per_hour: int = Field(default=1000, ge=1)
    country: Optional[str] = None
    provider: Optional[str] = None
    priority: int = Field(default=5, ge=1, le=10)
    notes: Optional[str] = None


class APIGatewayCreate(APIGatewayBase):
    pass


class APIGatewayUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    method: Optional[str] = None
    headers: Optional[Dict[str, str]] = None
    payload_template: Optional[Dict[str, Any]] = None
    is_enabled: Optional[bool] = None
    status: Optional[APIStatus] = None
    rate_limit_per_minute: Optional[int] = None
    rate_limit_per_hour: Optional[int] = None
    country: Optional[str] = None
    provider: Optional[str] = None
    priority: Optional[int] = None
    notes: Optional[str] = None


class APIGatewayResponse(APIGatewayBase):
    id: int
    status: APIStatus
    total_requests: int
    successful_requests: int
    failed_requests: int
    success_rate: float
    avg_response_time_ms: int
    last_checked: Optional[datetime] = None
    last_success: Optional[datetime] = None
    last_failure: Optional[datetime] = None
    consecutive_failures: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = {"from_attributes": True}


# ============= Analytics Schemas =============

class AnalyticsResponse(BaseModel):
    id: int
    date: datetime
    hour: Optional[int] = None
    total_campaigns: int
    active_campaigns: int
    completed_campaigns: int
    failed_campaigns: int
    total_requests: int
    successful_requests: int
    failed_requests: int
    success_rate: float
    active_apis: int
    total_apis: int
    avg_response_time_ms: int
    normal_mode_count: int
    stealth_mode_count: int
    turbo_mode_count: int
    smart_mode_count: int
    created_at: datetime
    
    model_config = {"from_attributes": True}


# ============= Dashboard Schemas =============

class DashboardStats(BaseModel):
    total_campaigns: int
    active_campaigns: int
    completed_campaigns: int
    success_rate: float
    total_sms_sent: int
    sms_sent_today: int
    active_apis: int
    total_apis: int


class RecentCampaign(BaseModel):
    id: int
    name: str
    mode: CampaignMode
    status: CampaignStatus
    target_count: int
    success_rate: float
    created_at: datetime


# ============= WebSocket Schemas =============

class WSMessage(BaseModel):
    type: str
    data: Dict[str, Any]
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# ============= Response Schemas =============

class SuccessResponse(BaseModel):
    success: bool = True
    message: str
    data: Optional[Any] = None


class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    detail: Optional[str] = None