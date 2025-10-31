#!/usr/bin/env python3
"""
SMS-PowerBomb v8.0 - Installation Verification Script
Created by: RAJSARASWATI JATAV
"""

import sys
import os

print("=" * 60)
print("SMS-PowerBomb v8.0 - Installation Verification")
print("=" * 60)
print()

# Check Python version
print("✓ Checking Python version...")
if sys.version_info >= (3, 7):
    print(f"  ✅ Python {sys.version_info.major}.{sys.version_info.minor} - OK")
else:
    print(f"  ❌ Python {sys.version_info.major}.{sys.version_info.minor} - Need 3.7+")
    sys.exit(1)

# Check required files
print("\n✓ Checking required files...")
required_files = [
    'main.py',
    'ai_engine.py',
    'analytics.py',
    'dashboard.py',
    'config.py',
    'requirements.txt'
]

all_files_present = True
for file in required_files:
    if os.path.exists(file):
        print(f"  ✅ {file}")
    else:
        print(f"  ❌ {file} - MISSING")
        all_files_present = False

if not all_files_present:
    print("\n❌ Some files are missing!")
    sys.exit(1)

# Check dependencies
print("\n✓ Checking dependencies...")
dependencies = {
    'aiohttp': 'Async HTTP client',
    'requests': 'HTTP library',
    'numpy': 'Numerical operations',
    'scikit-learn': 'Machine learning'
}

all_deps_installed = True
for module, description in dependencies.items():
    try:
        __import__(module.replace('-', '_'))
        print(f"  ✅ {module} - {description}")
    except ImportError:
        print(f"  ❌ {module} - NOT INSTALLED")
        all_deps_installed = False

if not all_deps_installed:
    print("\n⚠️  Some dependencies are missing!")
    print("Run: pip install -r requirements.txt")
    sys.exit(1)

# Check v8.0 modules
print("\n✓ Checking v8.0 modules...")
try:
    from ai_engine import AIEngine
    print("  ✅ AI Engine")
except ImportError as e:
    print(f"  ❌ AI Engine - {e}")
    all_deps_installed = False

try:
    from analytics import AnalyticsEngine
    print("  ✅ Analytics Engine")
except ImportError as e:
    print(f"  ❌ Analytics Engine - {e}")
    all_deps_installed = False

try:
    from dashboard import LiveDashboard
    print("  ✅ Live Dashboard")
except ImportError as e:
    print(f"  ❌ Live Dashboard - {e}")
    all_deps_installed = False

# Final status
print("\n" + "=" * 60)
if all_files_present and all_deps_installed:
    print("✅ ALL CHECKS PASSED!")
    print("=" * 60)
    print("\n🚀 SMS-PowerBomb v8.0 is ready to use!")
    print("\nRun: python main.py")
    print("\n🟢 Stay dark, stay ethical. Upgrade yourself! 🟢")
else:
    print("❌ INSTALLATION INCOMPLETE")
    print("=" * 60)
    print("\nPlease fix the issues above and try again.")
    sys.exit(1)