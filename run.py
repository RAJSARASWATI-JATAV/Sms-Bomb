#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SMS-POWERBOMB v8.0 - Windows Compatible Launcher
Fixes encoding issues on Windows systems
"""

import sys
import os

# Fix Windows encoding issues
if sys.platform == 'win32':
    # Set UTF-8 encoding for Windows
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    
    # Enable ANSI color support on Windows 10+
    os.system('')

# Import and run main program
if __name__ == "__main__":
    try:
        from main import main_menu
        main_menu()
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user (Ctrl+C).")
        print("[✓] Stay dark, stay ethical. Upgrade yourself!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] {str(e)}\n")
        sys.exit(1)