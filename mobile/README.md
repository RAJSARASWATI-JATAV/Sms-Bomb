# SMS-POWERBOMB Mobile App

React Native mobile application for SMS-POWERBOMB v10.0

## Setup

### Prerequisites
- Node.js >= 18
- React Native CLI
- Android Studio (for Android)
- Xcode (for iOS, macOS only)

### Installation

```bash
# Install dependencies
npm install

# For iOS (macOS only)
cd ios && pod install && cd ..

# Start Metro bundler
npm start

# Run on Android
npm run android

# Run on iOS
npm run ios
```

## Build APK

```bash
# Build release APK
npm run build:apk

# APK location: android/app/build/outputs/apk/release/app-release.apk
```

## Features

- 🎯 SMS Bombing with multiple modes
- 📊 Real-time campaign monitoring
- 📈 Statistics and analytics
- 🔐 User authentication
- 🌐 Backend API integration
- 📱 Native mobile experience

## Configuration

Create `.env` file:

```
API_URL=http://your-backend-url:8000
```

## Screens

1. **Home** - Dashboard and quick actions
2. **Bomb** - Start SMS bombing campaign
3. **History** - View past campaigns
4. **Stats** - Analytics and statistics
5. **Settings** - App configuration
6. **Profile** - User profile

## Created by

**RAJSARASWATI JATAV**
- GitHub: https://github.com/RAJSARASWATI-JATAV
- Telegram: https://t.me/rajsaraswatijatav