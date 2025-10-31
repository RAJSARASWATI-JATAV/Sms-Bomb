@echo off
REM SMS-POWERBOMB v10.0 - Development Run Script (Windows)
REM Created by: RAJSARASWATI JATAV

echo.
echo ========================================================
echo   SMS-POWERBOMB v10.0 - Development Environment
echo ========================================================
echo.

REM Start Backend
echo [1/2] Starting Backend...
cd backend
start "SMS-POWERBOMB Backend" cmd /k "python main.py"
cd ..
timeout /t 3 /nobreak >nul
echo [OK] Backend started

REM Start Frontend
echo [2/2] Starting Frontend...
cd frontend
start "SMS-POWERBOMB Frontend" cmd /k "npm run dev"
cd ..
timeout /t 2 /nobreak >nul
echo [OK] Frontend started

echo.
echo ========================================================
echo   Services Started Successfully!
echo ========================================================
echo.
echo   Frontend: http://localhost:5173
echo   Backend:  http://localhost:8000
echo   API Docs: http://localhost:8000/docs
echo.
echo   Close the terminal windows to stop services
echo.
echo   Created by: RAJSARASWATI JATAV
echo ========================================================
echo.

pause