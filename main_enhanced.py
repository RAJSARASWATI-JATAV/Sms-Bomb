#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SMS-POWERBOMB v8.5 - Enhanced Main Launcher
Includes Quick Mode, Favorites, Network Check, and more!
"""

import sys
import os

# Import the original main
from main import *

# Import enhanced features
try:
    from enhanced_features import (
        FavoritesManager, NetworkChecker, QuickModeConfig,
        ConfigManager, LoadingSpinner, ErrorHelper, QuickStats
    )
    ENHANCED = True
except ImportError:
    ENHANCED = False
    print("⚠️ Enhanced features not available. Using standard version.")
    print("Run: python main.py")
    sys.exit(1)

def print_enhanced_menu():
    """Display enhanced main menu"""
    network_status = "🟢 ONLINE" if NetworkChecker.check_internet() else "🔴 OFFLINE"
    
    menu = f"""{c.NEON_BLUE}
╔═══════════════════════════════════════════════════════════════════════════╗
║                         MAIN MENU - v8.5 ENHANCED                         ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  {c.NEON_ORANGE}[1]{c.WHITE} 🚀 Quick Mode (Fast Start)                                            {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[2]{c.WHITE} 💥 Start SMS Bombing (AI-Powered)                                     {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[3]{c.WHITE} ⭐ Manage Favorites                                                    {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[4]{c.WHITE} 📊 View Analytics & History                                           {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[5]{c.WHITE} 🔍 Check API Status                                                   {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[6]{c.WHITE} ℹ️  About Tool                                                         {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[7]{c.WHITE} ⚙️  Settings                                                           {c.NEON_BLUE}║
║  {c.NEON_ORANGE}[0]{c.WHITE} 🚪 Exit                                                                {c.NEON_BLUE}║
╠═══════════════════════════════════════════════════════════════════════════╣
║  {c.WHITE}Network: {c.NEON_GREEN if "ONLINE" in network_status else c.RED}{network_status}{c.RESET}  |  AI: {f"{c.NEON_GREEN}✓ ON{c.RESET}" if AI_ENABLED else f"{c.RED}✗ OFF{c.RESET}"}  |  Enhanced: {c.NEON_GREEN}✓ v8.5{c.RESET}              {c.NEON_BLUE}║
╚═══════════════════════════════════════════════════════════════════════════╝
{c.RESET}"""
    print(menu)


def quick_mode():
    """Quick mode with presets"""
    clear_screen()
    print_main_banner()
    
    print(f"\n{c.NEON_PURPLE}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
    print(f"{c.NEON_PURPLE}║{c.BOLD}{c.WHITE}                          QUICK MODE SELECTION                             {c.NEON_PURPLE}║{c.RESET}")
    print(f"{c.NEON_PURPLE}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
    
    presets = QuickModeConfig.get_all_presets()
    
    for i, (key, preset) in enumerate(presets.items(), 1):
        print(f"{c.NEON_ORANGE}[{i}]{c.WHITE} {preset['name']:<15} - {c.DARK}{preset['description']}{c.RESET}")
    
    print(f"\n{c.NEON_BLUE}[?]{c.WHITE} Select (1-{len(presets)}) or 0 to cancel: {c.NEON_ORANGE}", end="")
    choice = input().strip()
    print(c.RESET, end="")
    
    if choice == '0':
        return None
    
    try:
        idx = int(choice) - 1
        preset_key = list(presets.keys())[idx]
        return presets[preset_key]
    except (ValueError, IndexError):
        print(f"\n{c.RED}[!]{c.WHITE} Invalid selection!{c.RESET}")
        time.sleep(1.5)
        return None


def manage_favorites():
    """Manage favorite numbers"""
    favorites_mgr = FavoritesManager()
    
    while True:
        clear_screen()
        print_main_banner()
        
        print(f"\n{c.NEON_GREEN}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
        print(f"{c.NEON_GREEN}║{c.BOLD}{c.WHITE}                         MANAGE FAVORITES                                  {c.NEON_GREEN}║{c.RESET}")
        print(f"{c.NEON_GREEN}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
        
        favorites = favorites_mgr.get_all()
        
        if favorites:
            print(f"{c.WHITE}Your Favorite Numbers:{c.RESET}\n")
            for i, fav in enumerate(favorites):
                print(f"{c.NEON_ORANGE}[{i+1}]{c.WHITE} {fav['name']:<20} {c.NEON_BLUE}{fav['phone']}{c.DARK} (Used: {fav['times_used']}x){c.RESET}")
        else:
            print(f"{c.YELLOW}[!]{c.WHITE} No favorites saved yet.{c.RESET}\n")
        
        print(f"\n{c.NEON_BLUE}Options:{c.RESET}")
        print(f"{c.NEON_ORANGE}[A]{c.WHITE} Add new favorite")
        if favorites:
            print(f"{c.NEON_ORANGE}[D]{c.WHITE} Delete favorite")
            print(f"{c.NEON_ORANGE}[U]{c.WHITE} Use favorite for bombing")
        print(f"{c.NEON_ORANGE}[B]{c.WHITE} Back to main menu")
        
        print(f"\n{c.NEON_BLUE}[?]{c.WHITE} Select: {c.NEON_ORANGE}", end="")
        choice = input().strip().upper()
        print(c.RESET, end="")
        
        if choice == 'A':
            print(f"\n{c.NEON_BLUE}[?]{c.WHITE} Enter phone number: {c.NEON_ORANGE}", end="")
            phone = input().strip()
            print(c.RESET, end="")
            
            if validate_phone(phone):
                phone = normalize_phone(phone)
                print(f"{c.NEON_BLUE}[?]{c.WHITE} Enter name (optional): {c.NEON_ORANGE}", end="")
                name = input().strip()
                print(c.RESET, end="")
                
                favorites_mgr.add_favorite(phone, name)
                print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Favorite added!{c.RESET}")
                time.sleep(1.5)
            else:
                print(ErrorHelper.format_error('invalid_number', c))
                time.sleep(2)
        
        elif choice == 'D' and favorites:
            print(f"\n{c.NEON_BLUE}[?]{c.WHITE} Enter number to delete (1-{len(favorites)}): {c.NEON_ORANGE}", end="")
            try:
                idx = int(input().strip()) - 1
                print(c.RESET, end="")
                if favorites_mgr.remove_favorite(idx):
                    print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Deleted!{c.RESET}")
                else:
                    print(f"\n{c.RED}[!]{c.WHITE} Invalid!{c.RESET}")
            except ValueError:
                print(f"\n{c.RED}[!]{c.WHITE} Invalid input!{c.RESET}")
            time.sleep(1.5)
        
        elif choice == 'U' and favorites:
            print(f"\n{c.NEON_BLUE}[?]{c.WHITE} Select (1-{len(favorites)}): {c.NEON_ORANGE}", end="")
            try:
                idx = int(input().strip()) - 1
                print(c.RESET, end="")
                fav = favorites_mgr.get_favorite(idx)
                if fav:
                    favorites_mgr.increment_usage(idx)
                    return fav['phone']
            except ValueError:
                pass
            print(f"\n{c.RED}[!]{c.WHITE} Invalid!{c.RESET}")
            time.sleep(1.5)
        
        elif choice == 'B':
            return None


def settings_menu():
    """Settings menu"""
    config_mgr = ConfigManager()
    
    while True:
        clear_screen()
        print_main_banner()
        
        print(f"\n{c.NEON_PURPLE}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
        print(f"{c.NEON_PURPLE}║{c.BOLD}{c.WHITE}                    SETTINGS & CONFIGURATION                               {c.NEON_PURPLE}║{c.RESET}")
        print(f"{c.NEON_PURPLE}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
        
        print(f"{c.WHITE}Current Settings:{c.RESET}\n")
        print(f"{c.NEON_BLUE}[1]{c.WHITE} Auto Backup: {c.NEON_GREEN if config_mgr.get('auto_backup') else c.RED}{config_mgr.get('auto_backup')}{c.RESET}")
        print(f"{c.NEON_BLUE}[2]{c.WHITE} Auto Cleanup: {c.NEON_GREEN if config_mgr.get('auto_cleanup') else c.RED}{config_mgr.get('auto_cleanup')}{c.RESET}")
        print(f"{c.NEON_BLUE}[3]{c.WHITE} Animations: {c.NEON_GREEN if config_mgr.get('show_animations') else c.RED}{config_mgr.get('show_animations')}{c.RESET}")
        print(f"{c.NEON_BLUE}[4]{c.WHITE} Default Waves: {c.NEON_ORANGE}{config_mgr.get('default_waves')}{c.RESET}")
        print(f"\n{c.NEON_BLUE}[0]{c.WHITE} Back")
        
        print(f"\n{c.NEON_BLUE}[?]{c.WHITE} Select: {c.NEON_ORANGE}", end="")
        choice = input().strip()
        print(c.RESET, end="")
        
        if choice == '0':
            break
        elif choice in ['1', '2', '3']:
            key_map = {'1': 'auto_backup', '2': 'auto_cleanup', '3': 'show_animations'}
            key = key_map[choice]
            config_mgr.set(key, not config_mgr.get(key))
            print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Updated!{c.RESET}")
            time.sleep(1)


def enhanced_main_menu():
    """Enhanced main menu loop"""
    engine = AdvancedBomberEngine(SMS_APIS)
    
    while True:
        clear_screen()
        print_main_banner()
        print_loading_animation()
        print_creator_info()
        print_enhanced_menu()
        
        print(f"{c.NEON_BLUE}[?]{c.WHITE} Select: {c.NEON_ORANGE}", end="")
        choice = input().strip()
        print(c.RESET, end="")
        
        if choice == "1":
            # Quick Mode
            if not NetworkChecker.check_internet():
                print(ErrorHelper.format_error('network', c))
                print(f"{c.YELLOW}[!]{c.WHITE} Continue anyway? (yes/no): {c.NEON_ORANGE}", end="")
                cont = input().strip().lower()
                print(c.RESET, end="")
                if cont not in ["yes", "y"]:
                    continue
            
            preset = quick_mode()
            if not preset:
                continue
            
            clear_screen()
            print_main_banner()
            print_disclaimer()
            
            print(f"\n{c.YELLOW}[!]{c.WHITE} Accept terms? (yes/no): {c.NEON_ORANGE}", end="")
            accept = input().strip().lower()
            print(c.RESET, end="")
            
            if accept in ["yes", "y"]:
                phone = get_phone_input()
                
                print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Quick Mode: {c.NEON_ORANGE}{preset['name']}{c.RESET}")
                print(f"{c.NEON_GREEN}[✓]{c.WHITE} Waves: {c.NEON_ORANGE}{preset['waves']}{c.RESET}\n")
                
                print(f"{c.RED}[!]{c.WHITE} Start? (yes/no): {c.NEON_ORANGE}", end="")
                confirm = input().strip().lower()
                print(c.RESET, end="")
                
                if confirm in ["yes", "y"]:
                    try:
                        mode = preset['mode']
                        count = preset['waves']
                        delay = preset.get('delay', 2)
                        
                        if mode == '1':
                            asyncio.run(normal_mode_bombing(engine, phone, count, delay))
                        elif mode == '2':
                            asyncio.run(stealth_mode_bombing(engine, phone, count))
                        elif mode == '3':
                            asyncio.run(turbo_mode_bombing(engine, phone, count))
                    except KeyboardInterrupt:
                        print(f"\n\n{c.RED}[!]{c.WHITE} Interrupted.{c.RESET}")
                    
                    print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Press Enter...{c.RESET}")
                    input()
        
        elif choice == "2":
            # Normal bombing (use existing function from main.py)
            clear_screen()
            print_main_banner()
            print_disclaimer()
            
            print(f"\n{c.YELLOW}[!]{c.WHITE} Accept terms? (yes/no): {c.NEON_ORANGE}", end="")
            accept = input().strip().lower()
            print(c.RESET, end="")
            
            if accept in ["yes", "y"]:
                phone = get_phone_input()
                count = get_count_input()
                mode = get_mode_input()
                
                delay = 2
                if mode == '1':
                    delay = get_delay_input()
                
                print(f"\n{c.RED}[!]{c.WHITE} Start bombing {c.NEON_ORANGE}{phone}{c.WHITE}? (yes/no): {c.NEON_ORANGE}", end="")
                confirm = input().strip().lower()
                print(c.RESET, end="")
                
                if confirm in ["yes", "y"]:
                    try:
                        if mode == '1':
                            asyncio.run(normal_mode_bombing(engine, phone, count, delay))
                        elif mode == '2':
                            asyncio.run(stealth_mode_bombing(engine, phone, count))
                        elif mode == '3':
                            asyncio.run(turbo_mode_bombing(engine, phone, count))
                    except KeyboardInterrupt:
                        print(f"\n\n{c.RED}[!]{c.WHITE} Interrupted.{c.RESET}")
                    
                    print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Press Enter...{c.RESET}")
                    input()
        
        elif choice == "3":
            # Manage Favorites
            manage_favorites()
        
        elif choice == "4":
            # Analytics (placeholder)
            clear_screen()
            print_main_banner()
            print(f"\n{c.NEON_BLUE}[📊]{c.WHITE} Analytics & History{c.RESET}\n")
            print(f"{c.YELLOW}[!]{c.WHITE} Feature under development.{c.RESET}")
            print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Press Enter...{c.RESET}")
            input()
        
        elif choice == "5":
            # API Status
            clear_screen()
            print_main_banner()
            check_api_status(engine)
            print(f"{c.NEON_GREEN}[✓]{c.WHITE} Press Enter...{c.RESET}")
            input()
        
        elif choice == "6":
            # About
            clear_screen()
            print_main_banner()
            print_about()
            print(f"\n{c.NEON_GREEN}[✓]{c.WHITE} Press Enter...{c.RESET}")
            input()
        
        elif choice == "7":
            # Settings
            settings_menu()
        
        elif choice == "0":
            # Exit
            clear_screen()
            print(f"\n{c.NEON_PINK}╔═══════════════════════════════════════════════════════════════════════════╗{c.RESET}")
            print(f"{c.NEON_PINK}║{c.BOLD}{c.WHITE}                         EXITING SMS-POWERBOMB v8.5                        {c.NEON_PINK}║{c.RESET}")
            print(f"{c.NEON_PINK}╚═══════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
            print(f"{c.NEON_GREEN}[✓]{c.WHITE} Thank you for using SMS-PowerBomb v8.5!{c.RESET}")
            print(f"{c.NEON_PINK}[✓]{c.WHITE} Created by: {c.NEON_BLUE}RAJSARASWATI JATAV{c.RESET}")
            print(f"{c.NEON_ORANGE}[✓]{c.WHITE} Stay dark, stay ethical. Upgrade yourself!{c.RESET}\n")
            time.sleep(2)
            sys.exit(0)
        
        else:
            print(f"\n{c.RED}[!]{c.WHITE} Invalid option!{c.RESET}")
            time.sleep(1.5)


if __name__ == "__main__":
    try:
        enhanced_main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{c.RED}[!]{c.WHITE} Interrupted by user (Ctrl+C).{c.RESET}")
        print(f"{c.NEON_GREEN}[✓]{c.WHITE} Stay dark, stay ethical. Upgrade yourself!{c.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{c.RED}[ERROR]{c.WHITE} {str(e)}{c.RESET}\n")
        sys.exit(1)