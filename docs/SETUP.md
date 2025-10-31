# SMS-POWERBOMB v10.0 - Setup Guide

Complete setup instructions for all platforms.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start](#quick-start)
3. [CLI Setup](#cli-setup)
4. [Web Application Setup](#web-application-setup)
5. [Telegram Bot Setup](#telegram-bot-setup)
6. [Mobile App Setup](#mobile-app-setup)
7. [Desktop App Setup](#desktop-app-setup)
8. [Docker Deployment](#docker-deployment)

---

## Prerequisites

### Required
- **Python 3.7+** - For CLI and backend
- **Git** - For cloning repository

### Optional (for web/mobile/desktop)
- **Node.js 18+** - For frontend, mobile, and desktop apps
- **Docker & Docker Compose** - For containerized deployment
- **Android Studio** - For mobile app development
- **React Native CLI** - For mobile app

---

## Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/RAJSARASWATI-JATAV/Sms-Bomb
cd Sms-Bomb
```

### 2. Run Setup Script

**Linux/macOS:**
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

**Windows:**
```bash
# Using Git Bash
bash scripts/setup.sh

# Or using PowerShell
python scripts/setup.py
```

### 3. Configure Environment

Edit `.env` files in:
- `backend/.env` - Backend configuration
- `frontend/.env` - Frontend configuration
- `telegram-bot/.env` - Telegram bot token

### 4. Start Development Environment

**Linux/macOS:**
```bash
./scripts/run-dev.sh
```

**Windows:**
```bash
scripts\run-dev.bat
```

---

## CLI Setup

The CLI is the standalone command-line interface.

### Installation

```bash
cd cli
pip install -r requirements.txt
```

### Usage

```bash
python main.py
```

### Features
- 🎯 SMS bombing with 20+ APIs
- 🤖 AI-powered optimization
- 📊 Real-time analytics
- 💾 Campaign history
- 🎨 Cyberpunk UI

---

## Web Application Setup

Full-stack web application with React frontend and FastAPI backend.

### Backend Setup

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Run migrations (if any)
# alembic upgrade head

# Start server
python main.py
# Or: uvicorn main:app --reload
```

Backend will be available at: `http://localhost:8000`

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Configure environment
cp .env.example .env
# Edit .env with backend URL

# Start development server
npm run dev
```

Frontend will be available at: `http://localhost:5173`

### Production Build

```bash
cd frontend
npm run build
# Built files in dist/
```

---

## Telegram Bot Setup

Remote control via Telegram bot.

### 1. Create Bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow instructions to create bot
4. Copy the bot token

### 2. Configure

```bash
cd telegram-bot

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your bot token
```

### 3. Run Bot

```bash
python bot.py
```

### Bot Commands

- `/start` - Start the bot
- `/bomb <phone> <count> [mode]` - Start bombing
- `/status` - Check campaign status
- `/stop` - Stop active campaign
- `/stats` - View statistics
- `/apis` - Check API health
- `/help` - Show help

---

## Mobile App Setup

React Native mobile application for Android/iOS.

### Prerequisites

- Node.js 18+
- React Native CLI
- Android Studio (for Android)
- Xcode (for iOS, macOS only)

### Setup

```bash
cd mobile

# Install dependencies
npm install

# For iOS (macOS only)
cd ios && pod install && cd ..
```

### Run on Android

```bash
# Start Metro bundler
npm start

# In another terminal, run on Android
npm run android
```

### Build APK

```bash
npm run build:apk
# APK: android/app/build/outputs/apk/release/app-release.apk
```

### Run on iOS (macOS only)

```bash
npm run ios
```

---

## Desktop App Setup

Electron-based desktop application.

### Setup

```bash
cd desktop

# Install dependencies
npm install
```

### Development

```bash
npm start
```

### Build Executables

```bash
# Build for current platform
npm run build

# Build for specific platform
npm run build:win    # Windows
npm run build:linux  # Linux
npm run build:mac    # macOS
```

Built apps will be in `desktop/dist/`

---

## Docker Deployment

Containerized deployment with Docker.

### Prerequisites

- Docker
- Docker Compose

### Quick Deploy

```bash
# Start all services
docker-compose -f docker/docker-compose.yml up -d

# View logs
docker-compose -f docker/docker-compose.yml logs -f

# Stop services
docker-compose -f docker/docker-compose.yml down
```

### Services

- **Frontend**: http://localhost
- **Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Redis**: localhost:6379

### Custom Configuration

Edit `docker/docker-compose.yml` for custom ports and settings.

---

## Troubleshooting

### Common Issues

**1. Import errors**
```bash
pip install -r requirements.txt --upgrade
```

**2. Permission denied (Linux/macOS)**
```bash
chmod +x scripts/*.sh
```

**3. Port already in use**
- Change ports in `.env` files
- Or stop conflicting services

**4. Database errors**
- Delete `sms_bomb_analytics.db`
- Restart application

**5. Frontend can't connect to backend**
- Check `VITE_API_URL` in `frontend/.env`
- Ensure backend is running
- Check CORS settings in `backend/.env`

---

## Support

- **GitHub**: https://github.com/RAJSARASWATI-JATAV/Sms-Bomb
- **Telegram**: https://t.me/rajsaraswatijatav
- **Issues**: https://github.com/RAJSARASWATI-JATAV/Sms-Bomb/issues

---

**Created by: RAJSARASWATI JATAV**  
**Team: RAJSARASWATI JATAV CYBER CREW**