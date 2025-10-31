@echo off
REM SMS-POWERBOMB v10.0 - Quick Launcher
REM Double-click this file to run!

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║     SMS-POWERBOMB v10.0 - ULTIMATE FINAL EDITION              ║
echo ║     Quick Launcher - Starting in 2 seconds...                 ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

timeout /t 2 /nobreak >nul

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

REM Check Rich
python -c "import rich" >nul 2>&1
if errorlevel 1 (
    echo Installing Rich UI...
    pip install rich --quiet
)

REM Run the tool
echo Starting SMS-POWERBOMB v10.0...
echo.
python main_v10_fixed.py

pause