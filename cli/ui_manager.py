#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# ☠️ SMS-POWERBOMB v10.0 - RICH UI MANAGER ☠️
# ═══════════════════════════════════════════════════════════════════
# Creator: RAJSARASWATI JATAV
# Team: RAJSARASWATI JATAV CYBER CREW
# ═══════════════════════════════════════════════════════════════════
# Modern Terminal UI with Rich Library
# ═══════════════════════════════════════════════════════════════════

import time
from typing import List, Dict, Optional, Tuple
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.tree import Tree
from rich.align import Align
from rich import box
from rich.columns import Columns
from rich.markdown import Markdown

console = Console()

class RichUI:
    """Modern Rich UI Manager"""
    
    def __init__(self):
        self.console = console
        self.theme_colors = {
            'primary': '#00ff41',
            'secondary': '#ff006e',
            'accent': '#00d9ff',
            'warning': '#ff9500',
            'error': '#ff0000',
            'success': '#00ff41',
            'info': '#00d9ff'
        }
    
    def clear(self):
        """Clear screen"""
        self.console.clear()
    
    def print_banner(self):
        """Display main banner"""
        banner_text = """
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
║              ☠️  v10.0 ULTIMATE FINAL EDITION  ☠️                         ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
        """
        
        panel = Panel(
            Text(banner_text, style="bold green"),
            border_style="bright_magenta",
            box=box.DOUBLE
        )
        self.console.print(panel)
    
    def print_creator_info(self):
        """Display creator information"""
        info_table = Table(show_header=False, box=box.ROUNDED, border_style="cyan")
        info_table.add_column("Key", style="bold white")
        info_table.add_column("Value", style="bright_cyan")
        
        info_table.add_row("👨‍💻 Creator", "RAJSARASWATI JATAV")
        info_table.add_row("👥 Team", "RAJSARASWATI JATAV CYBER CREW")
        info_table.add_row("🐙 GitHub", "github.com/RAJSARASWATI-JATAV")
        info_table.add_row("📱 Telegram", "t.me/rajsaraswatijatav")
        info_table.add_row("📷 Instagram", "@official_rajsaraswati_jatav")
        info_table.add_row("🎥 YouTube", "@RajsaraswatiJatav")
        info_table.add_row("🚀 Version", "10.0 ULTIMATE FINAL EDITION")
        info_table.add_row("⚡ Status", "[bold green]HUNTING | DOMINATING | EXTREME[/bold green]")
        
        self.console.print(Panel(info_table, title="[bold magenta]Creator Info[/bold magenta]", border_style="magenta"))
        self.console.print()
    
    def print_disclaimer(self):
        """Display disclaimer"""
        disclaimer_text = """
[bold yellow]⚠️  DISCLAIMER  ⚠️[/bold yellow]

[bold red]This tool is for EDUCATIONAL & ETHICAL purposes ONLY![/bold red]

[green]✓[/green] Use for learning SMS automation & security research
[green]✓[/green] Use for pranking friends (with explicit consent)
[green]✓[/green] Use for testing your own systems

[red]✗[/red] DO NOT use for harassment or illegal activities
[red]✗[/red] DO NOT use without consent
[red]✗[/red] Creator is NOT responsible for any misuse

[bold magenta]By using this tool, you accept full responsibility for your actions.[/bold magenta]
        """
        
        panel = Panel(
            Markdown(disclaimer_text),
            title="[bold red]⚠️  IMPORTANT  ⚠️[/bold red]",
            border_style="red",
            box=box.DOUBLE
        )
        self.console.print(panel)
    
    def create_menu(self, title: str, options: List[Tuple[str, str]], show_ai_status: bool = False) -> Table:
        """Create a menu table"""
        table = Table(show_header=False, box=box.ROUNDED, border_style="bright_blue", padding=(0, 2))
        table.add_column("Option", style="bold yellow", width=8)
        table.add_column("Description", style="white")
        
        for option, description in options:
            table.add_row(f"[{option}]", description)
        
        if show_ai_status:
            table.add_row("", "")
            table.add_row("AI Status:", "[bold green]ENABLED ✓[/bold green]")
        
        return Panel(table, title=f"[bold cyan]{title}[/bold cyan]", border_style="cyan")
    
    def get_input(self, prompt: str, default: str = None, password: bool = False) -> str:
        """Get user input with Rich prompt"""
        if password:
            return Prompt.ask(f"[cyan]{prompt}[/cyan]", password=True)
        return Prompt.ask(f"[cyan]{prompt}[/cyan]", default=default)
    
    def get_confirmation(self, prompt: str, default: bool = False) -> bool:
        """Get yes/no confirmation"""
        return Confirm.ask(f"[yellow]{prompt}[/yellow]", default=default)
    
    def print_success(self, message: str):
        """Print success message"""
        self.console.print(f"[bold green]✓[/bold green] {message}")
    
    def print_error(self, message: str):
        """Print error message"""
        self.console.print(f"[bold red]✗[/bold red] {message}")
    
    def print_warning(self, message: str):
        """Print warning message"""
        self.console.print(f"[bold yellow]![/bold yellow] {message}")
    
    def print_info(self, message: str):
        """Print info message"""
        self.console.print(f"[bold cyan]ℹ[/bold cyan] {message}")
    
    def create_stats_table(self, stats: Dict) -> Table:
        """Create statistics table"""
        table = Table(show_header=True, box=box.ROUNDED, border_style="green")
        table.add_column("Metric", style="bold white", width=20)
        table.add_column("Value", style="bright_green", justify="right")
        
        for key, value in stats.items():
            formatted_key = key.replace('_', ' ').title()
            if isinstance(value, float):
                formatted_value = f"{value:.2f}"
            else:
                formatted_value = str(value)
            table.add_row(formatted_key, formatted_value)
        
        return table
    
    def create_api_status_table(self, api_health: Dict) -> Table:
        """Create API status table"""
        table = Table(show_header=True, box=box.ROUNDED, border_style="cyan")
        table.add_column("#", style="dim", width=4)
        table.add_column("API Name", style="bold white", width=20)
        table.add_column("Status", width=12)
        table.add_column("Success", style="green", justify="right", width=8)
        table.add_column("Failed", style="red", justify="right", width=8)
        table.add_column("Rate", justify="right", width=10)
        
        for idx, (api_name, health) in enumerate(api_health.items(), 1):
            total = health['success'] + health['fail']
            success_rate = (health['success'] / total * 100) if total > 0 else 0
            
            status = "[green]●[/green] ACTIVE" if health['active'] else "[red]●[/red] INACTIVE"
            rate_color = "green" if success_rate > 50 else "yellow" if success_rate > 20 else "red"
            
            table.add_row(
                str(idx),
                api_name,
                status,
                str(health['success']),
                str(health['fail']),
                f"[{rate_color}]{success_rate:.1f}%[/{rate_color}]"
            )
        
        return table
    
    def create_progress_bar(self, total: int, description: str = "Processing"):
        """Create a progress bar context"""
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=self.console
        )
    
    def print_session_summary(self, phone: str, stats: Dict):
        """Print final session summary"""
        # Create summary panel
        summary = Table(show_header=False, box=None, padding=(0, 2))
        summary.add_column("Key", style="bold white")
        summary.add_column("Value", style="bright_cyan")
        
        summary.add_row("📱 Target", phone)
        summary.add_row("📊 Total Attempts", str(stats['total_attempts']))
        summary.add_row("✅ Successful", f"[green]{stats['success']}[/green]")
        summary.add_row("❌ Failed", f"[red]{stats['failed']}[/red]")
        summary.add_row("📈 Success Rate", f"[yellow]{stats['success_rate']:.1f}%[/yellow]")
        summary.add_row("⏱️  Total Time", self._format_time(stats['elapsed_time']))
        summary.add_row("🔌 Active APIs", str(stats['active_apis']))
        
        # Performance rating
        if stats['success_rate'] > 60:
            rating = "[green]★★★★★ EXCELLENT[/green]"
            message = "[green]Outstanding performance! Target dominated successfully.[/green]"
        elif stats['success_rate'] > 40:
            rating = "[yellow]★★★★☆ GOOD[/yellow]"
            message = "[yellow]Good performance! Most APIs worked well.[/yellow]"
        elif stats['success_rate'] > 20:
            rating = "[orange1]★★★☆☆ AVERAGE[/orange1]"
            message = "[orange1]Average performance. Some APIs failed.[/orange1]"
        else:
            rating = "[red]★★☆☆☆ POOR[/red]"
            message = "[red]Low success rate. Most APIs failed or rate-limited.[/red]"
        
        summary.add_row("⭐ Rating", rating)
        
        panel = Panel(
            summary,
            title="[bold magenta]🎯 BOMBING COMPLETE - FINAL SUMMARY[/bold magenta]",
            border_style="magenta",
            box=box.DOUBLE
        )
        
        self.console.print()
        self.console.print(panel)
        self.console.print(f"\n{message}\n")
    
    def _format_time(self, seconds: float) -> str:
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
    
    def print_loading_animation(self):
        """Display loading animation"""
        animations = [
            ("System Breach", 99),
            ("SMS Infiltration", 96),
            ("Ghost Protocol", 90),
            ("AI Engine Loading", 85),
            ("Kernel Takeover", 97),
            ("Zero-Day Arsenal", 89),
        ]
        
        with self.create_progress_bar(len(animations), "Initializing") as progress:
            task = progress.add_task("[cyan]Loading modules...", total=len(animations))
            
            for label, percent in animations:
                progress.update(task, description=f"[cyan]{label}... {percent}%")
                time.sleep(0.15)
                progress.advance(task)
        
        self.console.print()
    
    def create_live_dashboard_layout(self) -> Layout:
        """Create live dashboard layout"""
        layout = Layout()
        
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="body"),
            Layout(name="footer", size=3)
        )
        
        layout["body"].split_row(
            Layout(name="left"),
            Layout(name="right")
        )
        
        return layout
    
    def print_favorites_table(self, favorites: List[Dict]) -> Table:
        """Create favorites table"""
        table = Table(show_header=True, box=box.ROUNDED, border_style="yellow")
        table.add_column("#", style="dim", width=4)
        table.add_column("Name", style="bold white", width=20)
        table.add_column("Phone", style="cyan", width=15)
        table.add_column("Times Used", style="green", justify="right", width=12)
        table.add_column("Added", style="dim", width=20)
        
        for idx, fav in enumerate(favorites, 1):
            table.add_row(
                str(idx),
                fav['name'],
                fav['phone'],
                str(fav.get('times_used', 0)),
                fav.get('added_date', 'Unknown')[:10]
            )
        
        return table
    
    def print_analytics_summary(self, trends: Dict):
        """Print analytics summary"""
        # Create summary cards
        cards = []
        
        # Total sessions card
        sessions_text = Text()
        sessions_text.append(f"{trends['total_sessions']}\n", style="bold cyan")
        sessions_text.append("Total Sessions", style="dim")
        cards.append(Panel(sessions_text, border_style="cyan", box=box.ROUNDED))
        
        # Total attempts card
        attempts_text = Text()
        attempts_text.append(f"{trends['total_attempts']}\n", style="bold yellow")
        attempts_text.append("Total Attempts", style="dim")
        cards.append(Panel(attempts_text, border_style="yellow", box=box.ROUNDED))
        
        # Success rate card
        success_text = Text()
        success_text.append(f"{trends['avg_success_rate']:.1f}%\n", style="bold green")
        success_text.append("Avg Success Rate", style="dim")
        cards.append(Panel(success_text, border_style="green", box=box.ROUNDED))
        
        # Total success card
        total_success_text = Text()
        total_success_text.append(f"{trends['total_success']}\n", style="bold magenta")
        total_success_text.append("Total Success", style="dim")
        cards.append(Panel(total_success_text, border_style="magenta", box=box.ROUNDED))
        
        self.console.print(Columns(cards, equal=True, expand=True))
        self.console.print()

# Global UI instance
ui = RichUI()