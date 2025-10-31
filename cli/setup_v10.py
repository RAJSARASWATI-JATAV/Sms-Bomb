#!/usr/bin/env python3
"""
SMS-POWERBOMB v10.0 Setup Script
Installs all dependencies and prepares the CLI
"""

import subprocess
import sys
import os

def print_banner():
    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                  SMS-POWERBOMB v10.0 SETUP                                ║
║                  ULTIMATE FINAL EDITION                                   ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)

def install_dependencies():
    """Install required dependencies"""
    print("\n[1/3] Installing dependencies...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("✗ Failed to install dependencies!")
        return False

def verify_installation():
    """Verify all modules are installed"""
    print("\n[2/3] Verifying installation...")
    
    required_modules = [
        'rich',
        'aiohttp',
        'requests',
        'numpy',
        'sklearn',
        'prompt_toolkit',
        'plotext'
    ]
    
    missing = []
    for module in required_modules:
        try:
            __import__(module)
            print(f"  ✓ {module}")
        except ImportError:
            print(f"  ✗ {module} - MISSING")
            missing.append(module)
    
    if missing:
        print(f"\n✗ Missing modules: {', '.join(missing)}")
        return False
    
    print("\n✓ All modules verified!")
    return True

def create_directories():
    """Create necessary directories"""
    print("\n[3/3] Creating directories...")
    
    directories = [
        'logs',
        'exports',
        'backups'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"  ✓ {directory}/")
    
    print("\n✓ Directories created!")
    return True

def main():
    """Main setup function"""
    print_banner()
    
    print("This script will install all dependencies for SMS-POWERBOMB v10.0")
    print("Creator: RAJSARASWATI JATAV")
    print("Team: RAJSARASWATI JATAV CYBER CREW\n")
    
    input("Press Enter to continue...")
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed at dependency installation!")
        sys.exit(1)
    
    # Verify installation
    if not verify_installation():
        print("\n❌ Setup failed at verification!")
        sys.exit(1)
    
    # Create directories
    if not create_directories():
        print("\n❌ Setup failed at directory creation!")
        sys.exit(1)
    
    # Success
    print("\n" + "="*75)
    print("✅ SETUP COMPLETE!")
    print("="*75)
    print("\nYou can now run SMS-POWERBOMB v10.0:")
    print("  python main_v10.py")
    print("\nFor the classic version:")
    print("  python main.py")
    print("\n🔥 Stay dark, stay ethical. Upgrade yourself! 🔥\n")

if __name__ == "__main__":
    main()