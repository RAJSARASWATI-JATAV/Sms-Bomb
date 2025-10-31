#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# ☠️ SMS-POWERBOMB UPDATE SCRIPT ☠️
# ═══════════════════════════════════════════════════════════════════
# Creator: RAJSARASWATI JATAV
# Team: RAJSARASWATI JATAV CYBER CREW
# Purpose: Auto-update script for SMS-PowerBomb
# ═══════════════════════════════════════════════════════════════════
# [ALERT] Updating system files...
# [WARN] Ghost protocol active
# [CRIT] Kernel sync initiated
# ═══════════════════════════════════════════════════════════════════

# Colors - Cyberpunk Theme
r = "\033[1;31m"  # Red
g = "\033[1;32m"  # Green
y = "\033[1;33m"  # Yellow
b = "\033[1;34m"  # Blue
d = "\033[2;37m"  # Dark
R = "\033[1;41m"  # Red BG
Y = "\033[1;43m"  # Yellow BG
B = "\033[1;44m"  # Blue BG
w = "\033[1;37m"  # White
cy = "\033[1;36m" # Cyan
m = "\033[1;35m"  # Magenta
ng = "\033[38;5;46m"  # Neon Green
np = "\033[38;5;201m" # Neon Pink
reset = "\033[0m" # Reset

# ----------------modules
from os import system, name
from time import sleep

# -----clear screen
system('cls' if name == 'nt' else 'clear')

# Cyberpunk Banner
print(f"""{ng}
╔═══════════════════════════════════════════════════════════════════════════╗
║  ☠️  SMS-POWERBOMB UPDATE PROTOCOL  ☠️                                    ║
║                                                                           ║
║  Creator: {np}RAJSARASWATI JATAV{ng}                                              ║
║  Team: {np}RAJSARASWATI JATAV CYBER CREW{ng}                                  ║
║  Version: {cy}6.0 ULTIMATE EDITION{ng}                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
{reset}""")

print(f"{y}[►] System Breach{w} [███████████████████░] 99%")
sleep(0.3)
print(f"{y}[►] Update Protocol{w} [██████████████████░░] 96%")
sleep(0.3)
print(f"{y}[►] Ghost Protocol{w} [████████████████░░░░] 90%{reset}")
sleep(0.3)
print(f"{y}[►] Kernel Sync{w} [▰▰▰▰▰▰▰▰▰▱] 97%{reset}")
sleep(0.3)

print(f"\n{r}[ALERT]{w} Initiating update sequence...{reset}")
sleep(0.5)

# -------update main.py
print(f"{cy}[>>]{w} Removing old main.py...{reset}")
system('del /f main.py 2>nul' if name == 'nt' else 'rm -rf main.py')
sleep(0.2)

print(f"{cy}[>>]{w} Downloading latest version from GitHub...{reset}")
system('curl -o main.py https://raw.githubusercontent.com/RAJSARASWATI-JATAV/Sms-Bomb/main/main.py' if name == 'nt' else 'wget https://raw.githubusercontent.com/RAJSARASWATI-JATAV/Sms-Bomb/main/main.py')
sleep(0.5)

print(f"\n{g}[✓]{w} Script Updated Successfully!{reset}")
print(f"{g}[✓]{w} SMS-PowerBomb v6.0 ULTIMATE - Ready to dominate{reset}")
sleep(0.5)

print(f"\n{np}╔═══════════════════════════════════════════════════════════════════════════╗")
print(f"║  {w}Update Complete - Returning to main script...{np}                         ║")
print(f"║  {w}Created by: {cy}RAJSARASWATI JATAV{np}                                            ║")
print(f"╚═══════════════════════════════════════════════════════════════════════════╝{reset}\n")
sleep(0.5)

# ---------return to main.py file 
system('python main.py' if name == 'nt' else 'python3 main.py')