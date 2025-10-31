@echo off
echo ========================================
echo SMS-POWERBOMB Bug Fix Verification
echo ========================================
echo.

cd /d "%~dp0.."

echo [Test 1] Checking backend .env CORS format...
findstr /C:"CORS_ORIGINS=http://localhost:5173,http://localhost:3000" backend\.env >nul
if %errorlevel%==0 (
    echo   [OK] CORS format is correct
) else (
    echo   [FAIL] CORS format is incorrect
)
echo.

echo [Test 2] Checking backend config.py for validator...
findstr /C:"field_validator" backend\config.py >nul
if %errorlevel%==0 (
    echo   [OK] CORS validator found
) else (
    echo   [FAIL] CORS validator not found
)
echo.

echo [Test 3] Checking frontend vite.config for code splitting...
findstr /C:"manualChunks" frontend\vite.config.ts >nul
if %errorlevel%==0 (
    echo   [OK] Code splitting configured
) else (
    echo   [FAIL] Code splitting not configured
)
echo.

echo [Test 4] Testing backend config loading...
cd backend
python test_config.py
cd ..
echo.

echo ========================================
echo Verification Complete!
echo ========================================
echo.
echo Next Steps:
echo 1. Start backend: cd backend ^& python main.py
echo 2. Start frontend: cd frontend ^& npm run dev
echo 3. Start CLI: cd cli ^& python main.py
echo.
pause