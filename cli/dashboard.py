#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# ☠️ SMS-POWERBOMB v8.0 - LIVE DASHBOARD MODULE ☠️
# ═══════════════════════════════════════════════════════════════════
# Creator: RAJSARASWATI JATAV
# Team: RAJSARASWATI JATAV CYBER CREW
# ═══════════════════════════════════════════════════════════════════
# Real-time Live Dashboard with Advanced Visualizations
# ═══════════════════════════════════════════════════════════════════

import time
import os
from typing import Dict, List
from datetime import datetime

class CyberColors:
    """Enhanced Cyberpunk color palette"""
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
    NEON_YELLOW = "\033[38;5;226m"
    
    # Special Effects
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    RESET = "\033[0m"

c = CyberColors()


class LiveDashboard:
    """Real-time live dashboard for bombing operations"""
    
    def __init__(self):
        self.start_time = None
        self.current_wave = 0
        self.total_waves = 0
        self.stats = {
            'total_attempts': 0,
            'success': 0,
            'failed': 0,
            'success_rate': 0,
            'active_apis': 0,
            'elapsed_time': 0
        }
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def draw_progress_bar(self, current: int, total: int, width: int = 50, 
                         color: str = c.NEON_GREEN) -> str:
        """Draw a fancy progress bar"""
        if total == 0:
            percent = 0
        else:
            percent = current / total
        
        filled = int(width * percent)
        bar = "█" * filled + "░" * (width - filled)
        percentage = int(percent * 100)
        
        return f"{color}[{bar}] {percentage}%{c.RESET}"
    
    def draw_mini_graph(self, values: List[int], width: int = 30, height: int = 5) -> List[str]:
        """Draw a mini ASCII graph"""
        if not values or max(values) == 0:
            return [f"{c.DARK}{'─' * width}{c.RESET}" for _ in range(height)]
        
        max_val = max(values)
        lines = []
        
        for h in range(height, 0, -1):
            line = ""
            threshold = (h / height) * max_val
            for val in values[-width:]:
                if val >= threshold:
                    line += f"{c.NEON_GREEN}▓{c.RESET}"
                else:
                    line += f"{c.DARK}░{c.RESET}"
            lines.append(line)
        
        return lines
    
    def format_time(self, seconds: float) -> str:
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
    
    def draw_header(self, phone: str, mode: str):
        """Draw dashboard header"""
        print(f"{c.NEON_PINK}{'═' * 80}{c.RESET}")
        print(f"{c.NEON_PINK}║{c.BOLD}{c.WHITE}{'SMS-POWERBOMB v8.0 - LIVE DASHBOARD':^78}{c.NEON_PINK}║{c.RESET}")
        print(f"{c.NEON_PINK}║{c.NEON_BLUE}{'AI DOMINATION EDITION':^78}{c.NEON_PINK}║{c.RESET}")
        print(f"{c.NEON_PINK}{'═' * 80}{c.RESET}")
        print(f"{c.WHITE}Target: {c.NEON_ORANGE}{phone:<20}{c.WHITE}Mode: {c.NEON_PURPLE}{mode:<15}{c.WHITE}Time: {c.CYAN}{datetime.now().strftime('%H:%M:%S')}{c.RESET}")
        print(f"{c.NEON_PINK}{'─' * 80}{c.RESET}\n")
    
    def draw_stats_panel(self):
        """Draw statistics panel"""
        print(f"{c.NEON_BLUE}╔══════════════════════════════════════╗{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.BOLD}{c.WHITE}{'STATISTICS':^38}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}╠══════════════════════════════════════╣{c.RESET}")
        
        # Wave progress
        wave_progress = self.draw_progress_bar(self.current_wave, self.total_waves, 30)
        print(f"{c.NEON_BLUE}║{c.WHITE} Waves: {wave_progress} {c.NEON_BLUE}║{c.RESET}")
        
        # Success rate
        success_progress = self.draw_progress_bar(self.stats['success'], 
                                                  self.stats['total_attempts'], 30,
                                                  c.NEON_GREEN)
        print(f"{c.NEON_BLUE}║{c.WHITE} Success: {success_progress} {c.NEON_BLUE}║{c.RESET}")
        
        print(f"{c.NEON_BLUE}╠══════════════════════════════════════╣{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.WHITE} Total Attempts: {c.YELLOW}{self.stats['total_attempts']:<21}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.WHITE} Successful: {c.NEON_GREEN}{self.stats['success']:<25}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.WHITE} Failed: {c.RED}{self.stats['failed']:<29}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.WHITE} Success Rate: {c.NEON_ORANGE}{self.stats['success_rate']:.1f}%{' ' * 19}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.WHITE} Active APIs: {c.NEON_PURPLE}{self.stats['active_apis']:<23}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.WHITE} Elapsed Time: {c.CYAN}{self.format_time(self.stats['elapsed_time']):<21}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}╚══════════════════════════════════════╝{c.RESET}\n")
    
    def draw_live_feed(self, recent_results: List[tuple]):
        """Draw live API results feed"""
        print(f"{c.NEON_GREEN}╔══════════════════════════════════════╗{c.RESET}")
        print(f"{c.NEON_GREEN}║{c.BOLD}{c.WHITE}{'LIVE FEED':^38}{c.NEON_GREEN}║{c.RESET}")
        print(f"{c.NEON_GREEN}╠══════════════════════════════════════╣{c.RESET}")
        
        if not recent_results:
            print(f"{c.NEON_GREEN}║{c.DARK}{'Waiting for results...':^38}{c.NEON_GREEN}║{c.RESET}")
        else:
            for api_name, success, msg in recent_results[-8:]:
                status = f"{c.NEON_GREEN}✓ SENT{c.RESET}" if success else f"{c.RED}✗ FAIL{c.RESET}"
                api_display = f"{api_name[:15]:<15}"
                print(f"{c.NEON_GREEN}║{c.WHITE} {api_display} {status}{' ' * 10}{c.NEON_GREEN}║{c.RESET}")
        
        print(f"{c.NEON_GREEN}╚══════════════════════════════════════╝{c.RESET}\n")
    
    def draw_performance_graph(self, success_history: List[int]):
        """Draw performance trend graph"""
        print(f"{c.NEON_PURPLE}╔══════════════════════════════════════╗{c.RESET}")
        print(f"{c.NEON_PURPLE}║{c.BOLD}{c.WHITE}{'SUCCESS RATE TREND':^38}{c.NEON_PURPLE}║{c.RESET}")
        print(f"{c.NEON_PURPLE}╠══════════════════════════════════════╣{c.RESET}")
        
        graph_lines = self.draw_mini_graph(success_history, width=36, height=5)
        for line in graph_lines:
            print(f"{c.NEON_PURPLE}║{c.RESET} {line} {c.NEON_PURPLE}║{c.RESET}")
        
        print(f"{c.NEON_PURPLE}╚══════════════════════════════════════╝{c.RESET}\n")
    
    def draw_ai_insights(self, ai_stats: Dict):
        """Draw AI insights panel"""
        print(f"{c.NEON_ORANGE}╔══════════════════════════════════════╗{c.RESET}")
        print(f"{c.NEON_ORANGE}║{c.BOLD}{c.WHITE}{'AI INSIGHTS':^38}{c.NEON_ORANGE}║{c.RESET}")
        print(f"{c.NEON_ORANGE}╠══════════════════════════════════════╣{c.RESET}")
        
        learning_bar = self.draw_progress_bar(int(ai_stats.get('learning_progress', 0)), 
                                             100, 30, c.NEON_YELLOW)
        print(f"{c.NEON_ORANGE}║{c.WHITE} Learning: {learning_bar} {c.NEON_ORANGE}║{c.RESET}")
        
        print(f"{c.NEON_ORANGE}║{c.WHITE} AI Status: {c.NEON_GREEN}{'ACTIVE' if ai_stats.get('active_apis', 0) > 0 else 'STANDBY':<24}{c.NEON_ORANGE}║{c.RESET}")
        
        if ai_stats.get('recommendations'):
            print(f"{c.NEON_ORANGE}║{c.WHITE} Recommendation:{' ' * 22}{c.NEON_ORANGE}║{c.RESET}")
            rec = ai_stats['recommendations'][0][:34]
            print(f"{c.NEON_ORANGE}║{c.CYAN}  {rec:<36}{c.NEON_ORANGE}║{c.RESET}")
        
        print(f"{c.NEON_ORANGE}╚══════════════════════════════════════╝{c.RESET}\n")
    
    def update_dashboard(self, phone: str, mode: str, current_wave: int, 
                        total_waves: int, stats: Dict, recent_results: List[tuple],
                        success_history: List[int], ai_stats: Dict = None):
        """Update the entire dashboard"""
        self.clear_screen()
        self.current_wave = current_wave
        self.total_waves = total_waves
        self.stats = stats
        
        # Draw all panels
        self.draw_header(phone, mode)
        
        # Two column layout
        print(f"{c.WHITE}{'─' * 80}{c.RESET}")
        
        # Left column: Stats and Live Feed
        self.draw_stats_panel()
        self.draw_live_feed(recent_results)
        
        # Right column: Graph and AI Insights
        self.draw_performance_graph(success_history)
        
        if ai_stats:
            self.draw_ai_insights(ai_stats)
        
        # Footer
        print(f"{c.NEON_PINK}{'─' * 80}{c.RESET}")
        print(f"{c.DARK}Press Ctrl+C to stop bombing{' ' * 46}{c.RESET}")
        print(f"{c.NEON_PINK}{'═' * 80}{c.RESET}")
    
    def show_final_summary(self, phone: str, stats: Dict, ai_patterns: Dict):
        """Show final summary after bombing"""
        self.clear_screen()
        
        print(f"\n{c.NEON_PINK}{'═' * 80}{c.RESET}")
        print(f"{c.NEON_PINK}║{c.BOLD}{c.WHITE}{'BOMBING COMPLETE - FINAL SUMMARY':^78}{c.NEON_PINK}║{c.RESET}")
        print(f"{c.NEON_PINK}{'═' * 80}{c.RESET}\n")
        
        # Main stats
        print(f"{c.NEON_BLUE}╔══════════════════════════════════════════════════════════════════════════════╗{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.BOLD}{c.WHITE}{'STATISTICS':^78}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}╠══════════════════════════════════════════════════════════════════════════════╣{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.WHITE}  Target Number: {c.NEON_ORANGE}{phone:<60}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.WHITE}  Total Attempts: {c.YELLOW}{stats['total_attempts']:<59}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.WHITE}  Successful: {c.NEON_GREEN}{stats['success']:<63}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.WHITE}  Failed: {c.RED}{stats['failed']:<67}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.WHITE}  Success Rate: {c.NEON_ORANGE}{stats['success_rate']:.1f}%{' ' * 57}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}║{c.WHITE}  Total Time: {c.CYAN}{self.format_time(stats['elapsed_time']):<62}{c.NEON_BLUE}║{c.RESET}")
        print(f"{c.NEON_BLUE}╚══════════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
        
        # AI Insights
        if ai_patterns:
            print(f"{c.NEON_GREEN}╔══════════════════════════════════════════════════════════════════════════════╗{c.RESET}")
            print(f"{c.NEON_GREEN}║{c.BOLD}{c.WHITE}{'AI ANALYSIS':^78}{c.NEON_GREEN}║{c.RESET}")
            print(f"{c.NEON_GREEN}╠══════════════════════════════════════════════════════════════════════════════╣{c.RESET}")
            
            if ai_patterns.get('best_apis'):
                print(f"{c.NEON_GREEN}║{c.WHITE}  Top Performing APIs:{' ' * 55}{c.NEON_GREEN}║{c.RESET}")
                for i, api in enumerate(ai_patterns['best_apis'][:5], 1):
                    print(f"{c.NEON_GREEN}║{c.CYAN}    {i}. {api:<70}{c.NEON_GREEN}║{c.RESET}")
            
            if ai_patterns.get('recommendations'):
                print(f"{c.NEON_GREEN}║{c.WHITE}  Recommendations:{' ' * 59}{c.NEON_GREEN}║{c.RESET}")
                for rec in ai_patterns['recommendations'][:3]:
                    print(f"{c.NEON_GREEN}║{c.YELLOW}    • {rec[:72]:<72}{c.NEON_GREEN}║{c.RESET}")
            
            print(f"{c.NEON_GREEN}╚══════════════════════════════════════════════════════════════════════════════╝{c.RESET}\n")
        
        # Performance rating
        if stats['success_rate'] > 60:
            rating = f"{c.NEON_GREEN}★★★★★ EXCELLENT{c.RESET}"
            message = f"{c.NEON_GREEN}Outstanding performance! Target dominated successfully.{c.RESET}"
        elif stats['success_rate'] > 40:
            rating = f"{c.YELLOW}★★★★☆ GOOD{c.RESET}"
            message = f"{c.YELLOW}Good performance! Most APIs worked well.{c.RESET}"
        elif stats['success_rate'] > 20:
            rating = f"{c.NEON_ORANGE}★★★☆☆ AVERAGE{c.RESET}"
            message = f"{c.NEON_ORANGE}Average performance. Some APIs failed.{c.RESET}"
        else:
            rating = f"{c.RED}★★☆☆☆ POOR{c.RESET}"
            message = f"{c.RED}Low success rate. Most APIs failed or rate-limited.{c.RESET}"
        
        print(f"{c.WHITE}Performance Rating: {rating}")
        print(f"{message}\n")
        
        print(f"{c.NEON_PINK}{'═' * 80}{c.RESET}")
        print(f"{c.NEON_GREEN}[✓]{c.WHITE} Data saved to database for future AI learning{c.RESET}")
        print(f"{c.NEON_PINK}{'═' * 80}{c.RESET}\n")