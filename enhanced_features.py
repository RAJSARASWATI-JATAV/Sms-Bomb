#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SMS-POWERBOMB v8.5 - Enhanced Features Module
Quick Mode, Favorites, Network Check, etc.
"""

import json
import os
import time
import socket
from typing import List, Dict, Optional
from datetime import datetime

class FavoritesManager:
    """Manage favorite phone numbers"""
    
    def __init__(self, file_path: str = 'favorites.json'):
        self.file_path = file_path
        self.favorites = self.load_favorites()
    
    def load_favorites(self) -> List[Dict]:
        """Load favorites from file"""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as f:
                    return json.load(f)
        except Exception:
            pass
        return []
    
    def save_favorites(self):
        """Save favorites to file"""
        try:
            with open(self.file_path, 'w') as f:
                json.dump(self.favorites, f, indent=2)
        except Exception:
            pass
    
    def add_favorite(self, phone: str, name: str = ""):
        """Add a favorite number"""
        favorite = {
            'phone': phone,
            'name': name or f"Target {len(self.favorites) + 1}",
            'added_date': datetime.now().isoformat(),
            'times_used': 0
        }
        self.favorites.append(favorite)
        self.save_favorites()
        return True
    
    def remove_favorite(self, index: int) -> bool:
        """Remove a favorite by index"""
        try:
            if 0 <= index < len(self.favorites):
                self.favorites.pop(index)
                self.save_favorites()
                return True
        except Exception:
            pass
        return False
    
    def get_favorite(self, index: int) -> Optional[Dict]:
        """Get favorite by index"""
        try:
            if 0 <= index < len(self.favorites):
                return self.favorites[index]
        except Exception:
            pass
        return None
    
    def increment_usage(self, index: int):
        """Increment usage count"""
        try:
            if 0 <= index < len(self.favorites):
                self.favorites[index]['times_used'] += 1
                self.save_favorites()
        except Exception:
            pass
    
    def get_all(self) -> List[Dict]:
        """Get all favorites"""
        return self.favorites


class NetworkChecker:
    """Check network connectivity and speed"""
    
    @staticmethod
    def check_internet() -> bool:
        """Check if internet is available"""
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False
    
    @staticmethod
    def check_speed() -> str:
        """Estimate connection speed"""
        try:
            start = time.time()
            socket.create_connection(("www.google.com", 80), timeout=5)
            elapsed = time.time() - start
            
            if elapsed < 0.5:
                return "Fast"
            elif elapsed < 1.5:
                return "Good"
            elif elapsed < 3.0:
                return "Slow"
            else:
                return "Very Slow"
        except Exception:
            return "Unknown"
    
    @staticmethod
    def get_network_info() -> Dict:
        """Get network information"""
        return {
            'connected': NetworkChecker.check_internet(),
            'speed': NetworkChecker.check_speed(),
            'timestamp': datetime.now().isoformat()
        }


class QuickModeConfig:
    """Quick mode preset configurations"""
    
    PRESETS = {
        'quick': {
            'name': 'Quick Mode',
            'waves': 5,
            'delay': 1,
            'mode': '1',  # Normal
            'description': 'Fast bombing with 5 waves'
        },
        'stealth': {
            'name': 'Stealth Mode',
            'waves': 10,
            'delay': 5,
            'mode': '2',  # Stealth
            'description': 'Stealthy bombing with random delays'
        },
        'turbo': {
            'name': 'Turbo Mode',
            'waves': 15,
            'delay': 0.5,
            'mode': '3',  # Turbo
            'description': 'Maximum speed bombing'
        },
        'smart': {
            'name': 'Smart Mode',
            'waves': 10,
            'delay': 2,
            'mode': '4',  # Smart (if available)
            'description': 'AI-optimized bombing'
        },
        'extreme': {
            'name': 'Extreme Mode',
            'waves': 20,
            'delay': 1,
            'mode': '3',  # Turbo
            'description': 'Maximum waves, maximum speed'
        }
    }
    
    @staticmethod
    def get_preset(preset_name: str) -> Optional[Dict]:
        """Get preset configuration"""
        return QuickModeConfig.PRESETS.get(preset_name)
    
    @staticmethod
    def get_all_presets() -> Dict:
        """Get all presets"""
        return QuickModeConfig.PRESETS


class ConfigManager:
    """Manage user configuration"""
    
    def __init__(self, file_path: str = 'config.json'):
        self.file_path = file_path
        self.config = self.load_config()
    
    def load_config(self) -> Dict:
        """Load configuration from file"""
        default_config = {
            'auto_backup': True,
            'backup_interval_days': 7,
            'auto_cleanup': True,
            'cleanup_days': 30,
            'default_mode': 'normal',
            'default_waves': 10,
            'default_delay': 2,
            'show_animations': True,
            'sound_effects': False,
            'theme': 'cyberpunk',
            'last_used': datetime.now().isoformat()
        }
        
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as f:
                    loaded = json.load(f)
                    default_config.update(loaded)
        except Exception:
            pass
        
        return default_config
    
    def save_config(self):
        """Save configuration to file"""
        try:
            self.config['last_used'] = datetime.now().isoformat()
            with open(self.file_path, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception:
            pass
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value):
        """Set configuration value"""
        self.config[key] = value
        self.save_config()
    
    def update(self, updates: Dict):
        """Update multiple configuration values"""
        self.config.update(updates)
        self.save_config()


class LoadingSpinner:
    """Animated loading spinner"""
    
    SPINNERS = {
        'dots': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
        'line': ['|', '/', '-', '\\'],
        'arrow': ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
        'box': ['◰', '◳', '◲', '◱'],
        'circle': ['◐', '◓', '◑', '◒'],
        'pulse': ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    }
    
    def __init__(self, style: str = 'dots'):
        self.frames = self.SPINNERS.get(style, self.SPINNERS['dots'])
        self.current = 0
    
    def next_frame(self) -> str:
        """Get next frame"""
        frame = self.frames[self.current]
        self.current = (self.current + 1) % len(self.frames)
        return frame


class ErrorHelper:
    """Provide helpful error messages and solutions"""
    
    ERROR_SOLUTIONS = {
        'network': {
            'message': 'Network connection failed',
            'solutions': [
                'Check your internet connection',
                'Try disabling VPN temporarily',
                'Check firewall settings',
                'Restart your router'
            ]
        },
        'api_failed': {
            'message': 'API request failed',
            'solutions': [
                'API might be temporarily down',
                'Try using a different mode',
                'Wait a few minutes and retry',
                'Check if the number is valid'
            ]
        },
        'rate_limit': {
            'message': 'Rate limit exceeded',
            'solutions': [
                'Use Stealth Mode for slower bombing',
                'Increase delay between waves',
                'Wait 5-10 minutes before retrying',
                'Some APIs are rate-limited'
            ]
        },
        'invalid_number': {
            'message': 'Invalid phone number',
            'solutions': [
                'Number must be 10 digits',
                'Must start with 6, 7, 8, or 9',
                'Remove country code (+91)',
                'Check for typos'
            ]
        },
        'database': {
            'message': 'Database error',
            'solutions': [
                'Database might be corrupted',
                'Try deleting sms_bomb_analytics.db',
                'Check disk space',
                'Restart the application'
            ]
        }
    }
    
    @staticmethod
    def get_solution(error_type: str) -> Dict:
        """Get solution for error type"""
        return ErrorHelper.ERROR_SOLUTIONS.get(
            error_type,
            {
                'message': 'Unknown error occurred',
                'solutions': [
                    'Check the error message above',
                    'Try restarting the application',
                    'Check README.md for help',
                    'Report issue on GitHub'
                ]
            }
        )
    
    @staticmethod
    def format_error(error_type: str, colors) -> str:
        """Format error message with solutions"""
        solution = ErrorHelper.get_solution(error_type)
        
        output = f"\n{colors.RED}[ERROR] {solution['message']}{colors.RESET}\n\n"
        output += f"{colors.YELLOW}Possible solutions:{colors.RESET}\n"
        
        for i, sol in enumerate(solution['solutions'], 1):
            output += f"{colors.CYAN}  {i}. {sol}{colors.RESET}\n"
        
        return output


class QuickStats:
    """Quick statistics display"""
    
    @staticmethod
    def get_badge(success_rate: float, colors) -> str:
        """Get success rate badge"""
        if success_rate >= 70:
            return f"{colors.NEON_GREEN}★★★★★ EXCELLENT{colors.RESET}"
        elif success_rate >= 50:
            return f"{colors.YELLOW}★★★★☆ GOOD{colors.RESET}"
        elif success_rate >= 30:
            return f"{colors.NEON_ORANGE}★★★☆☆ AVERAGE{colors.RESET}"
        else:
            return f"{colors.RED}★★☆☆☆ POOR{colors.RESET}"
    
    @staticmethod
    def format_number(num: int) -> str:
        """Format large numbers with K, M suffixes"""
        if num >= 1000000:
            return f"{num/1000000:.1f}M"
        elif num >= 1000:
            return f"{num/1000:.1f}K"
        else:
            return str(num)