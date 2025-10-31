# 🚀 SMS-POWERBOMB v10.0 - QUICK START GUIDE

## ⚡ Get Started in Minutes

Choose your platform and get started quickly!

---

## 📋 Prerequisites

### For CLI
- **Python 3.7+**

### For Web Dashboard
- **Python 3.7+** (Backend)
- **Node.js 18+** (Frontend)

### For Telegram Bot
- **Python 3.7+**
- **Telegram Bot Token**

### For Mobile App
- **Node.js 18+**
- **React Native CLI**
- **Android Studio** (for Android)

### For Desktop App
- **Node.js 18+**
- **Electron**

---

## 🎯 Quick Start Options

### Option 1: CLI Only (Fastest - 2 minutes)

```bash
# Clone repository
git clone https://github.com/RAJSARASWATI-JATAV/Sms-Bomb
cd Sms-Bomb

# Install CLI dependencies
cd cli
pip install -r requirements.txt

# Run CLI
python main.py
```

**Access:** Command-line interface

---

### Option 2: Web Dashboard (Full Stack - 5 minutes)

```bash
# Clone repository
git clone https://github.com/RAJSARASWATI-JATAV/Sms-Bomb
cd Sms-Bomb

# Run setup script
./scripts/setup.sh  # Linux/macOS
# OR
bash scripts/setup.sh  # Windows Git Bash

# Start all services
./scripts/run-dev.sh  # Linux/macOS
# OR
scripts\run-dev.bat  # Windows
```

**Access:**
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

### Option 3: Docker (Production - 3 minutes)

```bash
# Clone repository
git clone https://github.com/RAJSARASWATI-JATAV/Sms-Bomb
cd Sms-Bomb

# Start with Docker
docker-compose -f docker/docker-compose.yml up -d
```

**Access:**
- Frontend: http://localhost
- Backend: http://localhost:8000

---

### Option 4: Telegram Bot (3 minutes)

```bash
# Clone repository
git clone https://github.com/RAJSARASWATI-JATAV/Sms-Bomb
cd Sms-Bomb/telegram-bot

# Install dependencies
pip install -r requirements.txt

# Configure bot token
cp .env.example .env
# Edit .env and add TELEGRAM_BOT_TOKEN

# Run bot
python bot.py
```

**Access:** Your Telegram bot

---

### Option 5: Mobile App (10 minutes)

```bash
# Clone repository
git clone https://github.com/RAJSARASWATI-JATAV/Sms-Bomb
cd Sms-Bomb/mobile

# Install dependencies
npm install

# Build APK
npm run build:apk

# Install APK from:
# mobile/android/app/build/outputs/apk/release/app-release.apk
```

---

### Option 6: Desktop App (8 minutes)

```bash
# Clone repository
git clone https://github.com/RAJSARASWATI-JATAV/Sms-Bomb
cd Sms-Bomb/desktop

# Install dependencies
npm install

# Build for your platform
npm run build

# Run executable from desktop/dist/
```

---

## 🎨 Web Dashboard Quick Guide

### 1️⃣ Navigate to Frontend

```bash
cd frontend
```

### 2️⃣ Install Dependencies (First Time Only)

```bash
npm install
```

This will install:
- React 19 + TypeScript
- Tailwind CSS v4
- shadcn/ui components
- React Router v7
- Recharts
- Lucide React
- And all other dependencies

### 3️⃣ Start Development Server

```bash
npm run dev
```

### 4️⃣ Open in Browser

```
http://localhost:5173/
```

**That's it! 🎉**

---

## 🎨 What You'll See

### Login Page
- Beautiful cyberpunk-themed login
- Username/password fields
- Remember me option
- Security badges

**Default Credentials** (for demo):
- Username: `hacker_elite`
- Password: `anything` (no backend yet)

### Dashboard
- Real-time campaign statistics
- Success rate metrics
- Recent campaigns
- Quick actions
- System status

### Campaign Builder
- Create new SMS campaigns
- Choose bombing mode
- Configure settings
- Launch campaigns

### Analytics
- Interactive charts
- Success rate trends
- Campaign volume
- Mode distribution

### API Status
- Real-time API health
- Success/failure stats
- Search and filter
- Performance metrics

### Settings
- General preferences
- Security configuration
- Notifications
- Profile management

---

## 🎮 Available Commands

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linter
npm run lint
```

---

## 🎨 Features to Explore

### 1. Dashboard
- View campaign statistics
- Check recent campaigns
- Monitor system status
- Quick action buttons

### 2. Campaign Builder
- **Single Target**: Enter one phone number
- **Bulk Upload**: Upload CSV/Excel (UI ready)
- **Modes**: Normal, Stealth, Turbo, Smart
- **Settings**: Waves, delay, proxies, AI

### 3. Analytics
- **Success Rate**: Weekly trend chart
- **Campaigns**: Monthly volume chart
- **Distribution**: Mode usage pie chart
- **Export**: Download reports (UI ready)

### 4. API Status
- **Search**: Find specific APIs
- **Filter**: By status
- **Monitor**: Real-time health
- **Stats**: Success/failure rates

### 5. Settings
- **General**: Theme, language, auto-save
- **Security**: 2FA, proxy, VPN, Tor
- **Notifications**: Campaign, API, email
- **Profile**: Username, email, password

---

## 🎯 Navigation

### Sidebar Menu
- 🏠 **Dashboard** - Overview
- 🎯 **Campaign Builder** - Create campaigns
- 📊 **Analytics** - View statistics
- 📡 **API Status** - Monitor APIs
- ⚙️ **Settings** - Configure app

### Header
- 🔔 **Notifications** - Alerts
- 👤 **Profile** - User menu
- 🚪 **Logout** - Sign out

---

## 🎨 Theme & Design

### Colors
- **Neon Green** - Success, active
- **Neon Pink** - Highlights, CTAs
- **Neon Blue** - Links, info
- **Neon Purple** - Special features
- **Neon Orange** - Warnings

### Effects
- **Glassmorphism** - Frosted glass cards
- **Neon Glow** - Glowing elements
- **Smooth Animations** - Fluid transitions
- **Custom Scrollbar** - Styled scrolling

---

## 🔧 Troubleshooting

### Port Already in Use
```bash
# Kill process on port 5173
npx kill-port 5173

# Or use different port
npm run dev -- --port 3000
```

### Dependencies Error
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Build Error
```bash
# Check TypeScript errors
npm run build

# Fix and rebuild
npm run dev
```

---

## 📱 Responsive Design

The dashboard works perfectly on:
- 📱 **Mobile** (320px+)
- 📱 **Tablet** (768px+)
- 💻 **Desktop** (1024px+)
- 🖥️ **Large Desktop** (1440px+)

---

## 🎯 Next Steps

### Current Status
✅ **CLI Application** - Complete and working
✅ **Web Dashboard** - Complete frontend + backend
✅ **Telegram Bot** - Full implementation
✅ **Mobile App** - React Native with APK build
✅ **Desktop App** - Electron cross-platform
✅ **Docker Deployment** - Production ready
✅ **Documentation** - Comprehensive guides

### All Platforms Available
- ✅ CLI for command-line usage
- ✅ Web for browser access
- ✅ Telegram for remote control
- ✅ Mobile for Android devices
- ✅ Desktop for native experience
- ✅ Docker for easy deployment

---

## 💡 Tips

1. **Explore All Pages** - Check every section
2. **Try Different Modes** - Normal, Stealth, Turbo, Smart
3. **Check Analytics** - View charts and stats
4. **Monitor APIs** - See real-time health
5. **Configure Settings** - Customize your experience

---

## 🎨 Customization

### Change Theme Colors
Edit `frontend/src/index.css`:
```css
--color-neon-green: #00ff41;
--color-neon-pink: #ff006e;
--color-neon-blue: #00d9ff;
```

### Add New Pages
1. Create component in `src/pages/`
2. Add route in `src/App.tsx`
3. Add navigation in `src/components/layout/Sidebar.tsx`

---

## 📚 Documentation

- **Frontend README**: `frontend/README.md`
- **Project Summary**: `PROJECT_SUMMARY.md`
- **This Guide**: `QUICKSTART.md`

---

## 🆘 Need Help?

### Resources
- Check console for errors (F12)
- Read error messages carefully
- Check `frontend/README.md`
- Review component code

### Contact
- **Creator**: RAJSARASWATI JATAV
- **Team**: RAJSARASWATI JATAV CYBER CREW
- **GitHub**: [@RAJSARASWATI-JATAV](https://github.com/RAJSARASWATI-JATAV)

---

## ⚠️ Important Notes

### What's Included
- ✅ Complete CLI application
- ✅ Full-stack web dashboard
- ✅ Working Telegram bot
- ✅ Mobile app with APK
- ✅ Desktop app builds
- ✅ Docker deployment
- ✅ All documentation

### Configuration Required
- 🔧 Backend `.env` for secrets
- 🔧 Frontend `.env` for API URL
- 🔧 Telegram bot token
- 🔧 Mobile app backend URL
- 🔧 Desktop app settings

### What Works
- ✅ All platforms functional
- ✅ Complete UI/UX
- ✅ Real-time updates
- ✅ API integration ready
- ✅ Authentication system
- ✅ Analytics and monitoring

---

## 🎉 Enjoy!

You're now ready to use SMS-POWERBOMB v10.0 on any platform!

**Complete Package**: All platforms (CLI, Web, Telegram, Mobile, Desktop) are fully implemented and ready to use.

---

## 🟢 Quick Commands Reference

```bash
# CLI
cd cli && python main.py

# Web Frontend
cd frontend && npm run dev

# Web Backend
cd backend && python main.py

# Telegram Bot
cd telegram-bot && python bot.py

# Mobile APK
cd mobile && npm run build:apk

# Desktop Build
cd desktop && npm run build

# Docker Deploy
docker-compose -f docker/docker-compose.yml up -d

# Run All (Development)
./scripts/run-dev.sh  # Linux/macOS
scripts\run-dev.bat   # Windows
```

---

<div align="center">
  <b>🔥 SMS-POWERBOMB v10.0 ULTIMATE EDITION 🔥</b>
  <br>
  <i>Stay dark, stay ethical, stay powerful!</i>
  <br><br>
  <b>Created by RAJSARASWATI JATAV</b>
</div>