# 📁 SMS-POWERBOMB v10.0 - Project Structure

Complete directory structure and file organization.

```
SMS-POWERBOMB-v10/
│
├── 📱 cli/                          # CLI Application
│   ├── main.py                      # Main CLI entry point
│   ├── ai_engine.py                 # AI/ML features
│   ├── analytics.py                 # Analytics engine
│   ├── dashboard.py                 # Live dashboard
│   ├── enhanced_features.py         # Enhanced features
│   ├── quantum_ai.py                # Quantum AI features
│   ├── config.py                    # CLI configuration
│   └── requirements.txt             # CLI dependencies
│
├── 🌐 backend/                      # FastAPI Backend
│   ├── main.py                      # API server entry
│   ├── config.py                    # Backend config
│   ├── database.py                  # Database setup
│   ├── models.py                    # SQLAlchemy models
│   ├── schemas.py                   # Pydantic schemas
│   ├── auth.py                      # Authentication
│   ├── execution_engine.py          # Campaign execution
│   ├── websocket_manager.py         # WebSocket manager
│   ├── task_manager.py              # Background tasks
│   │
│   ├── routers/                     # API Routes
│   │   ├── auth.py                  # Auth endpoints
│   │   ├── campaigns.py             # Campaign endpoints
│   │   ├── apis.py                  # API management
│   │   ├── dashboard.py             # Dashboard data
│   │   ├── monitoring.py            # System monitoring
│   │   └── websocket.py             # WebSocket endpoint
│   │
│   ├── .env.example                 # Environment template
│   ├── .env                         # Environment config
│   └── requirements.txt             # Backend dependencies
│
├── 💻 frontend/                     # React Frontend
│   ├── src/
│   │   ├── components/              # React components
│   │   │   ├── layout/              # Layout components
│   │   │   │   ├── Sidebar.tsx
│   │   │   │   ├── Header.tsx
│   │   │   │   └── Layout.tsx
│   │   │   └── ui/                  # shadcn components
│   │   │
│   │   ├── pages/                   # Page components
│   │   │   ├── Dashboard.tsx
│   │   │   ├── CampaignBuilder.tsx
│   │   │   ├── Analytics.tsx
│   │   │   ├── ApiStatus.tsx
│   │   │   ├── Settings.tsx
│   │   │   └── Login.tsx
│   │   │
│   │   ├── contexts/                # React contexts
│   │   │   └── AuthContext.tsx
│   │   │
│   │   ├── hooks/                   # Custom hooks
│   │   │   └── useWebSocket.ts
│   │   │
│   │   ├── lib/                     # Utilities
│   │   │   ├── api.ts               # API client
│   │   │   ├── websocket.ts         # WebSocket client
│   │   │   └── utils.ts             # Helper functions
│   │   │
│   │   ├── App.tsx                  # Main app component
│   │   ├── main.tsx                 # Entry point
│   │   └── index.css                # Global styles
│   │
│   ├── public/                      # Static assets
│   ├── .env.example                 # Environment template
│   ├── .env                         # Environment config
│   ├── package.json                 # Dependencies
│   ├── tsconfig.json                # TypeScript config
│   ├── vite.config.ts               # Vite config
│   └── components.json              # shadcn config
│
├── 🤖 telegram-bot/                 # Telegram Bot
│   ├── bot.py                       # Main bot file
│   ├── .env.example                 # Environment template
│   ├── .env                         # Environment config
│   └── requirements.txt             # Bot dependencies
│
├── 📱 mobile/                       # React Native App
│   ├── android/                     # Android build
│   │   └── app/
│   │       └── build/
│   │           └── outputs/
│   │               └── apk/
│   │                   └── release/
│   │                       └── app-release.apk
│   │
│   ├── ios/                         # iOS build (optional)
│   ├── src/                         # App source code
│   ├── App.tsx                      # Main app component
│   ├── package.json                 # Dependencies
│   └── README.md                    # Mobile docs
│
├── 🖥️ desktop/                      # Electron Desktop
│   ├── main.js                      # Electron main process
│   ├── preload.js                   # Preload script
│   ├── dist/                        # Built executables
│   │   ├── *.exe                    # Windows
│   │   ├── *.AppImage               # Linux
│   │   └── *.dmg                    # macOS
│   │
│   ├── package.json                 # Dependencies
│   └── README.md                    # Desktop docs
│
├── 🐳 docker/                       # Docker Configuration
│   ├── Dockerfile.backend           # Backend image
│   ├── Dockerfile.frontend          # Frontend image
│   ├── docker-compose.yml           # Compose config
│   └── nginx.conf                   # Nginx config
│
├── 🔧 scripts/                      # Build & Deploy Scripts
│   ├── setup.sh                     # Setup script
│   ├── run-dev.sh                   # Dev run (Linux/macOS)
│   ├── run-dev.bat                  # Dev run (Windows)
│   ├── build-all.sh                 # Build all platforms
│   ├── deploy.sh                    # Deploy script
│   └── stop-dev.sh                  # Stop dev servers
│
├── 📚 docs/                         # Documentation
│   ├── SETUP.md                     # Setup guide
│   ├── API.md                       # API documentation
│   └── USAGE.md                     # Usage guide
│
├── 🗄️ builds/                       # Build Artifacts
│   ├── frontend/                    # Frontend build
│   ├── cli/                         # CLI package
│   ├── backend/                     # Backend package
│   ├── *.apk                        # Android APK
│   ├── *.exe                        # Windows executable
│   ├── *.AppImage                   # Linux executable
│   └── *.dmg                        # macOS executable
│
├── 📄 Root Files
│   ├── README.md                    # Main readme
│   ├── QUICKSTART.md                # Quick start guide
│   ├── PROJECT_STRUCTURE.md         # This file
│   ├── LICENSE                      # Apache 2.0 license
│   ├── .gitignore                   # Git ignore rules
│   ├── requirements.txt             # Root Python deps
│   ├── package.json                 # Root Node deps
│   └── sms_bomb_analytics.db        # SQLite database
│
└── 🖼️ Assets
    └── smsbombv5.png                # Logo/banner
```

---

## 📦 Key Components

### CLI Application
- **Purpose**: Standalone command-line interface
- **Tech**: Python 3.7+
- **Features**: AI engine, analytics, live dashboard
- **Entry**: `cli/main.py`

### Backend API
- **Purpose**: RESTful API server
- **Tech**: FastAPI, SQLAlchemy, WebSocket
- **Features**: Authentication, campaigns, real-time updates
- **Entry**: `backend/main.py`
- **Port**: 8000

### Frontend Dashboard
- **Purpose**: Web-based UI
- **Tech**: React 19, TypeScript, Tailwind v4, shadcn
- **Features**: Dashboard, analytics, campaign builder
- **Entry**: `frontend/src/main.tsx`
- **Port**: 5173

### Telegram Bot
- **Purpose**: Remote control via Telegram
- **Tech**: python-telegram-bot
- **Features**: Campaign control, status monitoring
- **Entry**: `telegram-bot/bot.py`

### Mobile App
- **Purpose**: Native Android/iOS app
- **Tech**: React Native
- **Features**: Full mobile experience
- **Entry**: `mobile/App.tsx`
- **Output**: APK/IPA files

### Desktop App
- **Purpose**: Native desktop application
- **Tech**: Electron
- **Features**: Wraps web UI in native window
- **Entry**: `desktop/main.js`
- **Output**: EXE/AppImage/DMG

---

## 🔧 Configuration Files

### Environment Files
- `backend/.env` - Backend configuration
- `frontend/.env` - Frontend configuration
- `telegram-bot/.env` - Bot token and settings

### Build Configs
- `frontend/vite.config.ts` - Vite configuration
- `frontend/tsconfig.json` - TypeScript config
- `frontend/components.json` - shadcn config
- `mobile/package.json` - React Native config
- `desktop/package.json` - Electron config

### Docker Configs
- `docker/docker-compose.yml` - Service orchestration
- `docker/Dockerfile.backend` - Backend image
- `docker/Dockerfile.frontend` - Frontend image
- `docker/nginx.conf` - Nginx configuration

---

## 📊 Data Flow

```
User Input
    ↓
Frontend/CLI/Telegram/Mobile/Desktop
    ↓
Backend API (FastAPI)
    ↓
Database (SQLite)
    ↓
Execution Engine
    ↓
SMS APIs (20+)
    ↓
Real-time Updates (WebSocket)
    ↓
Frontend/Telegram/Mobile
```

---

## 🚀 Deployment Options

### 1. Local Development
```bash
./scripts/run-dev.sh
```

### 2. Docker Deployment
```bash
docker-compose -f docker/docker-compose.yml up -d
```

### 3. Production Build
```bash
./scripts/build-all.sh
```

### 4. Individual Platforms
```bash
# CLI
cd cli && python main.py

# Web
cd frontend && npm run dev
cd backend && python main.py

# Telegram
cd telegram-bot && python bot.py

# Mobile
cd mobile && npm run android

# Desktop
cd desktop && npm start
```

---

## 📝 File Naming Conventions

### Python Files
- `snake_case.py` - Module files
- `PascalCase` - Class names
- `snake_case` - Function names

### TypeScript/React Files
- `PascalCase.tsx` - Component files
- `camelCase.ts` - Utility files
- `kebab-case.css` - Style files

### Configuration Files
- `.env` - Environment variables
- `*.config.ts` - Configuration files
- `*.json` - JSON configs

---

## 🔐 Security Files

### Sensitive Files (Not in Git)
- `.env` files
- `*.db` files
- `node_modules/`
- `__pycache__/`
- `dist/` and `build/` folders
- API keys and tokens

### Public Files
- `.env.example` templates
- Documentation
- Source code
- Configuration templates

---

## 📦 Dependencies

### Python Dependencies
- Core: `requirements.txt` (root)
- CLI: `cli/requirements.txt`
- Backend: `backend/requirements.txt`
- Bot: `telegram-bot/requirements.txt`

### Node Dependencies
- Root: `package.json` (workspace)
- Frontend: `frontend/package.json`
- Mobile: `mobile/package.json`
- Desktop: `desktop/package.json`

---

## 🎯 Entry Points

| Platform | Entry Point | Command |
|----------|-------------|---------|
| CLI | `cli/main.py` | `python main.py` |
| Backend | `backend/main.py` | `python main.py` |
| Frontend | `frontend/src/main.tsx` | `npm run dev` |
| Telegram | `telegram-bot/bot.py` | `python bot.py` |
| Mobile | `mobile/App.tsx` | `npm run android` |
| Desktop | `desktop/main.js` | `npm start` |
| Docker | `docker/docker-compose.yml` | `docker-compose up` |

---

**Created by: RAJSARASWATI JATAV**  
**Team: RAJSARASWATI JATAV CYBER CREW**