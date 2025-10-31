#!/usr/bin/env python3
"""
Configuration module for SMS-POWERBOMB CLI
"""

import os
from typing import Dict, Any

class CLIConfig:
    """CLI Configuration"""
    
    # Application Info
    APP_NAME = "SMS-POWERBOMB"
    VERSION = "10.0"
    EDITION = "ULTIMATE FINAL EDITION"
    
    # Creator Info
    CREATOR = "RAJSARASWATI JATAV"
    TEAM = "RAJSARASWATI JATAV CYBER CREW"
    GITHUB = "https://github.com/RAJSARASWATI-JATAV"
    TELEGRAM = "https://t.me/rajsaraswatijatav"
    INSTAGRAM = "@official_rajsaraswati_jatav"
    YOUTUBE = "@RajsaraswatiJatav"
    
    # Database
    DB_PATH = os.path.join(os.path.dirname(__file__), "..", "sms_bomb_analytics.db")
    
    # API Configuration
    MAX_RETRIES = 3
    REQUEST_TIMEOUT = 15
    DEFAULT_DELAY = 2
    
    # Bombing Modes
    MODES = {
        '1': 'Normal',
        '2': 'Stealth',
        '3': 'Turbo',
        '4': 'Smart'
    }
    
    # API Health Thresholds
    API_DISABLE_THRESHOLD = 0.9  # Disable if fail rate > 90%
    API_MIN_ATTEMPTS = 5  # Minimum attempts before health check
    
    # Backend API (if available)
    BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
    BACKEND_ENABLED = os.getenv("BACKEND_ENABLED", "false").lower() == "true"
    
    @classmethod
    def get_full_version(cls) -> str:
        """Get full version string"""
        return f"{cls.APP_NAME} v{cls.VERSION} - {cls.EDITION}"
    
    @classmethod
    def get_creator_info(cls) -> Dict[str, str]:
        """Get creator information"""
        return {
            "creator": cls.CREATOR,
            "team": cls.TEAM,
            "github": cls.GITHUB,
            "telegram": cls.TELEGRAM,
            "instagram": cls.INSTAGRAM,
            "youtube": cls.YOUTUBE
        }