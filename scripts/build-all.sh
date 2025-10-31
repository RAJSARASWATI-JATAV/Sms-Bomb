#!/bin/bash
# SMS-POWERBOMB v10.0 - Build All Script
# Created by: RAJSARASWATI JATAV

set -e

echo "🔨 SMS-POWERBOMB v10.0 - Build All Components"
echo "=============================================="
echo ""

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

BUILD_DIR="builds"
mkdir -p $BUILD_DIR

# Build Frontend
echo -e "${BLUE}[1/5] Building Frontend...${NC}"
cd frontend
npm run build
cp -r dist ../$BUILD_DIR/frontend
cd ..
echo -e "${GREEN}✓ Frontend built${NC}"

# Build Mobile APK
if [ -d "mobile/android" ]; then
    echo -e "${BLUE}[2/5] Building Mobile APK...${NC}"
    cd mobile
    npm run build:apk 2>/dev/null || echo -e "${YELLOW}⚠ Mobile build skipped${NC}"
    if [ -f "android/app/build/outputs/apk/release/app-release.apk" ]; then
        cp android/app/build/outputs/apk/release/app-release.apk ../$BUILD_DIR/SMS-POWERBOMB-v10.0.apk
        echo -e "${GREEN}✓ Mobile APK built${NC}"
    fi
    cd ..
else
    echo -e "${YELLOW}[2/5] Mobile build skipped (not configured)${NC}"
fi

# Build Desktop Apps
if [ -d "desktop" ] && command -v npm >/dev/null 2>&1; then
    echo -e "${BLUE}[3/5] Building Desktop Apps...${NC}"
    cd desktop
    
    # Build for current platform
    npm run build 2>/dev/null || echo -e "${YELLOW}⚠ Desktop build skipped${NC}"
    
    # Copy builds
    if [ -d "dist" ]; then
        cp -r dist/* ../$BUILD_DIR/
        echo -e "${GREEN}✓ Desktop apps built${NC}"
    fi
    cd ..
else
    echo -e "${YELLOW}[3/5] Desktop build skipped (not configured)${NC}"
fi

# Package CLI
echo -e "${BLUE}[4/5] Packaging CLI...${NC}"
mkdir -p $BUILD_DIR/cli
cp -r cli/* $BUILD_DIR/cli/
cp requirements.txt $BUILD_DIR/cli/
echo -e "${GREEN}✓ CLI packaged${NC}"

# Package Backend
echo -e "${BLUE}[5/5] Packaging Backend...${NC}"
mkdir -p $BUILD_DIR/backend
cp -r backend/* $BUILD_DIR/backend/
echo -e "${GREEN}✓ Backend packaged${NC}"

# Create README
cat > $BUILD_DIR/README.txt << EOF
SMS-POWERBOMB v10.0 - ULTIMATE FINAL EDITION
============================================

Created by: RAJSARASWATI JATAV
Team: RAJSARASWATI JATAV CYBER CREW

Build Date: $(date)

Contents:
---------
- frontend/     - Web UI (production build)
- cli/          - Command-line interface
- backend/      - FastAPI backend
- *.apk         - Android mobile app (if built)
- *.exe/.dmg    - Desktop apps (if built)

Quick Start:
-----------
1. CLI: cd cli && python main.py
2. Web: Serve frontend/ folder or use Docker
3. Backend: cd backend && python main.py
4. Mobile: Install the APK on Android device
5. Desktop: Run the executable for your platform

Docker Deployment:
-----------------
cd .. && docker-compose -f docker/docker-compose.yml up -d

For detailed instructions, see: README.md

⚠️ DISCLAIMER: For educational purposes only. Use responsibly!
EOF

echo ""
echo -e "${GREEN}✅ Build completed successfully!${NC}"
echo ""
echo "Build artifacts in: $BUILD_DIR/"
echo ""
ls -lh $BUILD_DIR/
echo ""
echo "Created by: RAJSARASWATI JATAV"