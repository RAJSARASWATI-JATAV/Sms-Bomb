@echo off
REM SMS-POWERBOMB v10.0 Launcher for Windows
REM Creator: RAJSARASWATI JATAV

echo.
echo ╔═══════════════════════════════════════════════════════════════════════════╗
echo ║              SMS-POWERBOMB v10.0 - ULTIMATE FINAL EDITION                ║
echo ║                    Launching in 3 seconds...                              ║
echo ╚═══════════════════════════════════════════════════════════════════════════╝
echo.

timeout /t 3 /nobreak >nul

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

REM Check if Rich is installed
python -c "import rich" >nul 2>&1
if errorlevel 1 (
    echo Installing required dependencies...
    pip install rich prompt-toolkit plotext --quiet
)

REM Launch the application
python main_v10.py

pause