from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, Text, ForeignKey, Enum, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import enum


class UserRole(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class CampaignStatus(str, enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class CampaignMode(str, enum.Enum):
    NORMAL = "normal"
    STEALTH = "stealth"
    TURBO = "turbo"
    SMART = "smart"


class APIStatus(str, enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    RATE_LIMITED = "rate_limited"
    ERROR = "error"


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100))
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True))
    
    # Relationships
    campaigns = relationship("Campaign", back_populates="user", cascade="all, delete-orphan")
    settings = relationship("UserSettings", back_populates="user", uselist=False, cascade="all, delete-orphan")


class UserSettings(Base):
    __tablename__ = "user_settings"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    
    # General Settings
    theme = Column(String(20), default="dark")
    language = Column(String(10), default="en")
    timezone = Column(String(50), default="UTC")
    
    # Notification Settings
    email_notifications = Column(Boolean, default=True)
    push_notifications = Column(Boolean, default=True)
    telegram_notifications = Column(Boolean, default=False)
    telegram_chat_id = Column(String(100))
    
    # Security Settings
    two_factor_enabled = Column(Boolean, default=False)
    two_factor_secret = Column(String(100))
    session_timeout = Column(Integer, default=30)
    
    # Campaign Defaults
    default_mode = Column(Enum(CampaignMode), default=CampaignMode.NORMAL)
    default_waves = Column(Integer, default=1)
    default_delay = Column(Integer, default=5)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="settings")


class Campaign(Base):
    __tablename__ = "campaigns"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Campaign Info
    name = Column(String(100), nullable=False)
    description = Column(Text)
    mode = Column(Enum(CampaignMode), default=CampaignMode.NORMAL, nullable=False)
    status = Column(Enum(CampaignStatus), default=CampaignStatus.PENDING, nullable=False)
    
    # Targets
    targets = Column(JSON, nullable=False)  # List of phone numbers
    target_count = Column(Integer, nullable=False)
    
    # Configuration
    waves = Column(Integer, default=1, nullable=False)
    delay_seconds = Column(Integer, default=5, nullable=False)
    use_proxy = Column(Boolean, default=False)
    use_vpn = Column(Boolean, default=False)
    randomize_apis = Column(Boolean, default=True)
    
    # Statistics
    total_requests = Column(Integer, default=0)
    successful_requests = Column(Integer, default=0)
    failed_requests = Column(Integer, default=0)
    success_rate = Column(Float, default=0.0)
    
    # Timing
    started_at = Column(DateTime(timezone=True))
    completed_at = Column(DateTime(timezone=True))
    estimated_completion = Column(DateTime(timezone=True))
    duration_seconds = Column(Integer)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="campaigns")
    logs = relationship("CampaignLog", back_populates="campaign", cascade="all, delete-orphan")


class CampaignLog(Base):
    __tablename__ = "campaign_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    
    # Log Details
    target = Column(String(20), nullable=False)
    api_name = Column(String(100), nullable=False)
    status = Column(String(20), nullable=False)  # success, failed, error
    response_code = Column(Integer)
    response_message = Column(Text)
    response_time_ms = Column(Integer)
    
    # Error Info
    error_type = Column(String(50))
    error_message = Column(Text)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    campaign = relationship("Campaign", back_populates="logs")


class APIGateway(Base):
    __tablename__ = "api_gateways"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # API Info
    name = Column(String(100), unique=True, nullable=False, index=True)
    url = Column(String(500), nullable=False)
    method = Column(String(10), default="POST", nullable=False)
    headers = Column(JSON)
    payload_template = Column(JSON)
    
    # Status
    status = Column(Enum(APIStatus), default=APIStatus.ACTIVE, nullable=False)
    is_enabled = Column(Boolean, default=True, nullable=False)
    
    # Statistics
    total_requests = Column(Integer, default=0)
    successful_requests = Column(Integer, default=0)
    failed_requests = Column(Integer, default=0)
    success_rate = Column(Float, default=0.0)
    avg_response_time_ms = Column(Integer, default=0)
    
    # Rate Limiting
    rate_limit_per_minute = Column(Integer, default=60)
    rate_limit_per_hour = Column(Integer, default=1000)
    current_minute_count = Column(Integer, default=0)
    current_hour_count = Column(Integer, default=0)
    last_reset_minute = Column(DateTime(timezone=True))
    last_reset_hour = Column(DateTime(timezone=True))
    
    # Health Check
    last_checked = Column(DateTime(timezone=True))
    last_success = Column(DateTime(timezone=True))
    last_failure = Column(DateTime(timezone=True))
    consecutive_failures = Column(Integer, default=0)
    
    # Metadata
    country = Column(String(50))
    provider = Column(String(100))
    priority = Column(Integer, default=5)
    notes = Column(Text)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Analytics(Base):
    __tablename__ = "analytics"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Time Period
    date = Column(DateTime(timezone=True), nullable=False, index=True)
    hour = Column(Integer)
    
    # Metrics
    total_campaigns = Column(Integer, default=0)
    active_campaigns = Column(Integer, default=0)
    completed_campaigns = Column(Integer, default=0)
    failed_campaigns = Column(Integer, default=0)
    
    total_requests = Column(Integer, default=0)
    successful_requests = Column(Integer, default=0)
    failed_requests = Column(Integer, default=0)
    success_rate = Column(Float, default=0.0)
    
    # API Stats
    active_apis = Column(Integer, default=0)
    total_apis = Column(Integer, default=0)
    avg_response_time_ms = Column(Integer, default=0)
    
    # Mode Distribution
    normal_mode_count = Column(Integer, default=0)
    stealth_mode_count = Column(Integer, default=0)
    turbo_mode_count = Column(Integer, default=0)
    smart_mode_count = Column(Integer, default=0)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())