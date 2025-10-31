#!/bin/bash
# SMS-POWERBOMB v10.0 - Setup Script
# Created by: RAJSARASWATI JATAV

set -e

echo "🚀 SMS-POWERBOMB v10.0 - Setup Script"
echo "======================================"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Check if running on Windows (Git Bash/WSL)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo -e "${YELLOW}Detected Windows environment${NC}"
    IS_WINDOWS=true
else
    IS_WINDOWS=false
fi

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Python
echo "📦 Checking Python..."
if command_exists python3; then
    PYTHON_CMD=python3
elif command_exists python; then
    PYTHON_CMD=python
else
    echo -e "${RED}❌ Python not found! Please install Python 3.7+${NC}"
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✓ Python $PYTHON_VERSION found${NC}"

# Check Node.js
echo "📦 Checking Node.js..."
if command_exists node; then
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✓ Node.js $NODE_VERSION found${NC}"
else
    echo -e "${YELLOW}⚠ Node.js not found (optional for web/mobile/desktop)${NC}"
fi

# Setup CLI
echo ""
echo "🔧 Setting up CLI..."
cd cli
$PYTHON_CMD -m pip install -r requirements.txt --quiet
echo -e "${GREEN}✓ CLI dependencies installed${NC}"
cd ..

# Setup Backend
echo ""
echo "🔧 Setting up Backend..."
cd backend
$PYTHON_CMD -m pip install -r requirements.txt --quiet
echo -e "${GREEN}✓ Backend dependencies installed${NC}"

# Create .env if not exists
if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "${GREEN}✓ Created backend .env file${NC}"
fi
cd ..

# Setup Frontend
if command_exists node; then
    echo ""
    echo "🔧 Setting up Frontend..."
    cd frontend
    npm install --silent
    echo -e "${GREEN}✓ Frontend dependencies installed${NC}"
    
    # Create .env if not exists
    if [ ! -f .env ]; then
        cp .env.example .env
        echo -e "${GREEN}✓ Created frontend .env file${NC}"
    fi
    cd ..
fi

# Setup Telegram Bot
echo ""
echo "🔧 Setting up Telegram Bot..."
cd telegram-bot
$PYTHON_CMD -m pip install -r requirements.txt --quiet
echo -e "${GREEN}✓ Telegram bot dependencies installed${NC}"

# Create .env if not exists
if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "${GREEN}✓ Created telegram bot .env file${NC}"
fi
cd ..

# Setup Mobile (optional)
if command_exists node && [ -f mobile/package.json ]; then
    echo ""
    echo "🔧 Setting up Mobile App (optional)..."
    cd mobile
    npm install --silent 2>/dev/null || echo -e "${YELLOW}⚠ Mobile setup skipped${NC}"
    cd ..
fi

# Setup Desktop (optional)
if command_exists node && [ -f desktop/package.json ]; then
    echo ""
    echo "🔧 Setting up Desktop App (optional)..."
    cd desktop
    npm install --silent 2>/dev/null || echo -e "${YELLOW}⚠ Desktop setup skipped${NC}"
    cd ..
fi

echo ""
echo -e "${GREEN}✅ Setup completed successfully!${NC}"
echo ""
echo "📚 Next steps:"
echo "  1. Configure .env files in backend/, frontend/, and telegram-bot/"
echo "  2. Run: ./scripts/run-dev.sh (or run-dev.bat on Windows)"
echo "  3. Access web UI at: http://localhost:5173"
echo "  4. Access API at: http://localhost:8000"
echo ""
echo "Created by: RAJSARASWATI JATAV"