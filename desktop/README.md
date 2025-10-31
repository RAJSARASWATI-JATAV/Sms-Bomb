# SMS-POWERBOMB Desktop App

Electron-based desktop application for SMS-POWERBOMB v10.0

## Features

- 🖥️ Native desktop experience
- 🌐 Wraps the web frontend
- 💾 Local configuration storage
- 🔄 Auto-updates support
- 🎨 Custom window controls

## Development

```bash
# Install dependencies
npm install

# Start in development mode
npm start
```

## Building

```bash
# Build for current platform
npm run build

# Build for Windows
npm run build:win

# Build for Linux
npm run build:linux

# Build for macOS
npm run build:mac
```

## Output

Built applications will be in the `dist/` directory:
- Windows: `.exe` installer
- Linux: `.AppImage`
- macOS: `.dmg`

## Configuration

The app stores configuration in:
- Windows: `%APPDATA%/sms-powerbomb-desktop`
- Linux: `~/.config/sms-powerbomb-desktop`
- macOS: `~/Library/Application Support/sms-powerbomb-desktop`

## Created by

**RAJSARASWATI JATAV**
- GitHub: https://github.com/RAJSARASWATI-JATAV