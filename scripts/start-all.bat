@echo off
echo ========================================
echo SMS-POWERBOMB - Start All Services
echo ========================================
echo.

cd /d "%~dp0.."

echo [1/3] Starting Backend Server...
start "SMS-POWERBOMB Backend" cmd /k "cd backend && python main.py"
timeout /t 3 /nobreak >nul

echo [2/3] Starting Frontend Dev Server...
start "SMS-POWERBOMB Frontend" cmd /k "cd frontend && npm run dev"
timeout /t 3 /nobreak >nul

echo.
echo ========================================
echo All Services Started!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:5173
echo API Docs: http://localhost:8000/docs
echo.
echo Press any key to open browser...
pause >nul

start http://localhost:5173
start http://localhost:8000/docs

echo.
echo Services are running in separate windows.
echo Close those windows to stop the services.
echo.
pause