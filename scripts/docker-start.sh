#!/bin/bash
# SMS-POWERBOMB Docker Quick Start Script

echo "========================================="
echo "SMS-POWERBOMB Docker Deployment"
echo "========================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed!"
    echo "Please install Docker from: https://docs.docker.com/get-docker/"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed!"
    echo "Please install Docker Compose from: https://docs.docker.com/compose/install/"
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"
echo ""

# Check if .env file exists
if [ ! -f "docker/.env.production" ]; then
    echo "⚠️  Production .env file not found!"
    echo "Creating from template..."
    cp docker/.env.production .env
    echo "✅ Created .env file"
    echo "⚠️  Please update SECRET_KEY and other settings in .env file!"
    echo ""
fi

# Build and start containers
echo "🔨 Building Docker images..."
docker-compose build

if [ $? -ne 0 ]; then
    echo "❌ Docker build failed!"
    exit 1
fi

echo ""
echo "🚀 Starting containers..."
docker-compose up -d

if [ $? -ne 0 ]; then
    echo "❌ Failed to start containers!"
    exit 1
fi

echo ""
echo "========================================="
echo "✅ SMS-POWERBOMB is now running!"
echo "========================================="
echo ""
echo "Services:"
echo "  Frontend: http://localhost"
echo "  Backend:  http://localhost:8000"
echo "  API Docs: http://localhost:8000/docs"
echo ""
echo "Useful commands:"
echo "  View logs:    docker-compose logs -f"
echo "  Stop:         docker-compose stop"
echo "  Restart:      docker-compose restart"
echo "  Remove:       docker-compose down"
echo ""
echo "Check status:"
docker-compose ps
echo ""