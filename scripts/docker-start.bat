@echo off
REM SMS-POWERBOMB Docker Quick Start Script (Windows)

echo =========================================
echo SMS-POWERBOMB Docker Deployment
echo =========================================
echo.

REM Check if Docker is installed
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Docker is not installed!
    echo Please install Docker Desktop from: https://docs.docker.com/desktop/install/windows-install/
    pause
    exit /b 1
)

REM Check if Docker Compose is installed
docker-compose --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Docker Compose is not installed!
    echo Please install Docker Compose
    pause
    exit /b 1
)

echo [OK] Docker and Docker Compose are installed
echo.

REM Check if .env file exists
if not exist "docker\.env.production" (
    echo [WARNING] Production .env file not found!
    echo Creating from template...
    copy docker\.env.production .env
    echo [OK] Created .env file
    echo [WARNING] Please update SECRET_KEY and other settings in .env file!
    echo.
)

REM Build and start containers
echo [BUILD] Building Docker images...
docker-compose build

if %errorlevel% neq 0 (
    echo [ERROR] Docker build failed!
    pause
    exit /b 1
)

echo.
echo [START] Starting containers...
docker-compose up -d

if %errorlevel% neq 0 (
    echo [ERROR] Failed to start containers!
    pause
    exit /b 1
)

echo.
echo =========================================
echo [SUCCESS] SMS-POWERBOMB is now running!
echo =========================================
echo.
echo Services:
echo   Frontend: http://localhost
echo   Backend:  http://localhost:8000
echo   API Docs: http://localhost:8000/docs
echo.
echo Useful commands:
echo   View logs:    docker-compose logs -f
echo   Stop:         docker-compose stop
echo   Restart:      docker-compose restart
echo   Remove:       docker-compose down
echo.
echo Check status:
docker-compose ps
echo.
pause