#!/bin/bash
# SMS-POWERBOMB v10.0 - Deployment Script
# Created by: RAJSARASWATI JATAV

set -e

echo "🚀 SMS-POWERBOMB v10.0 - Deployment Script"
echo "==========================================="
echo ""

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# Check if Docker is installed
if ! command -v docker >/dev/null 2>&1; then
    echo -e "${RED}❌ Docker not found! Please install Docker first.${NC}"
    exit 1
fi

if ! command -v docker-compose >/dev/null 2>&1; then
    echo -e "${RED}❌ docker-compose not found! Please install docker-compose first.${NC}"
    exit 1
fi

echo -e "${BLUE}Select deployment mode:${NC}"
echo "  1) Development (with hot reload)"
echo "  2) Production (optimized)"
echo "  3) Stop all services"
echo "  4) View logs"
echo ""
read -p "Enter choice [1-4]: " choice

case $choice in
    1)
        echo -e "${BLUE}Starting in Development mode...${NC}"
        docker-compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml up -d
        ;;
    2)
        echo -e "${BLUE}Starting in Production mode...${NC}"
        
        # Build images
        echo "Building Docker images..."
        docker-compose -f docker/docker-compose.yml build
        
        # Start services
        echo "Starting services..."
        docker-compose -f docker/docker-compose.yml up -d
        ;;
    3)
        echo -e "${YELLOW}Stopping all services...${NC}"
        docker-compose -f docker/docker-compose.yml down
        echo -e "${GREEN}✓ Services stopped${NC}"
        exit 0
        ;;
    4)
        echo -e "${BLUE}Viewing logs...${NC}"
        docker-compose -f docker/docker-compose.yml logs -f
        exit 0
        ;;
    *)
        echo -e "${RED}Invalid choice!${NC}"
        exit 1
        ;;
esac

# Wait for services to start
echo ""
echo "Waiting for services to start..."
sleep 5

# Check service health
echo ""
echo -e "${BLUE}Checking service health...${NC}"

# Check backend
if curl -s http://localhost:8000/health > /dev/null; then
    echo -e "${GREEN}✓ Backend is healthy${NC}"
else
    echo -e "${RED}✗ Backend is not responding${NC}"
fi

# Check frontend
if curl -s http://localhost:80 > /dev/null; then
    echo -e "${GREEN}✓ Frontend is healthy${NC}"
else
    echo -e "${RED}✗ Frontend is not responding${NC}"
fi

echo ""
echo -e "${GREEN}✅ Deployment completed!${NC}"
echo ""
echo "Access points:"
echo "  Frontend:  http://localhost"
echo "  Backend:   http://localhost:8000"
echo "  API Docs:  http://localhost:8000/docs"
echo ""
echo "Useful commands:"
echo "  docker-compose -f docker/docker-compose.yml ps       - View running services"
echo "  docker-compose -f docker/docker-compose.yml logs -f  - View logs"
echo "  docker-compose -f docker/docker-compose.yml down     - Stop services"
echo ""
echo "Created by: RAJSARASWATI JATAV"