#!/usr/bin/env python3
"""
SMS-POWERBOMB v8.0 - Module Test Script
Tests all modules for errors
"""

import sys

print("=" * 60)
print("SMS-POWERBOMB v8.0 - MODULE TEST")
print("=" * 60)
print()

# Test imports
modules_to_test = [
    ('main', 'Main Application'),
    ('ai_engine', 'AI Engine'),
    ('analytics', 'Analytics & Database'),
    ('dashboard', 'Live Dashboard')
]

all_passed = True

for module_name, description in modules_to_test:
    try:
        print(f"Testing {description}...", end=" ")
        __import__(module_name)
        print("✓ PASS")
    except Exception as e:
        print(f"✗ FAIL: {str(e)}")
        all_passed = False

print()
print("=" * 60)

if all_passed:
    print("✅ ALL MODULES LOADED SUCCESSFULLY!")
    print()
    print("🚀 Ready to use: python main.py")
    print("   or for Windows: python run.py")
else:
    print("❌ SOME MODULES FAILED TO LOAD")
    print()
    print("Please install requirements:")
    print("   pip install -r requirements.txt")

print("=" * 60)