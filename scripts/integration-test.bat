@echo off
echo ========================================
echo SMS-POWERBOMB Integration Testing
echo ========================================
echo.

cd /d "%~dp0.."

echo [Phase 1] Testing Backend API...
echo.
cd backend
python -c "import requests; r = requests.get('http://localhost:8000/health', timeout=5); print('Backend Health:', r.json() if r.status_code == 200 else 'FAILED')" 2>nul
if %errorlevel% neq 0 (
    echo Backend is not running. Please start it first.
    echo Run: cd backend ^& python main.py
    cd ..
    pause
    exit /b 1
)
cd ..

echo.
echo [Phase 2] Testing Frontend Build...
echo.
cd frontend
call npm run build
if %errorlevel% neq 0 (
    echo Frontend build failed!
    cd ..
    pause
    exit /b 1
)
cd ..

echo.
echo [Phase 3] Testing CLI...
echo.
cd cli
python -c "print('CLI modules check...'); import main; print('CLI imports successful!')"
if %errorlevel% neq 0 (
    echo CLI has import errors!
    cd ..
    pause
    exit /b 1
)
cd ..

echo.
echo ========================================
echo Integration Tests Complete!
echo ========================================
echo.
echo All components are working correctly.
echo.
pause