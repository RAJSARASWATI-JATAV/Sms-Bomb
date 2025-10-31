#!/bin/bash
# SMS-POWERBOMB v10.0 Launcher for Linux/Mac
# Creator: RAJSARASWATI JATAV

echo ""
echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║              SMS-POWERBOMB v10.0 - ULTIMATE FINAL EDITION                ║"
echo "║                    Launching in 3 seconds...                              ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

sleep 3

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed!"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Check if Rich is installed
python3 -c "import rich" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing required dependencies..."
    pip3 install rich prompt-toolkit plotext --quiet
fi

# Launch the application
python3 main_v10.py