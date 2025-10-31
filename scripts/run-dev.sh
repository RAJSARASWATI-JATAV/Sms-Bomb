#!/bin/bash
# SMS-POWERBOMB v10.0 - Development Run Script
# Created by: RAJSARASWATI JATAV

set -e

echo "🚀 Starting SMS-POWERBOMB v10.0 Development Environment"
echo "======================================================="
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Check if tmux is available
if command -v tmux >/dev/null 2>&1; then
    USE_TMUX=true
    echo -e "${GREEN}Using tmux for session management${NC}"
else
    USE_TMUX=false
    echo -e "${YELLOW}tmux not found, running in background${NC}"
fi

# Function to start backend
start_backend() {
    echo -e "${BLUE}Starting Backend...${NC}"
    cd backend
    python main.py &
    BACKEND_PID=$!
    echo $BACKEND_PID > ../backend.pid
    cd ..
    echo -e "${GREEN}✓ Backend started (PID: $BACKEND_PID)${NC}"
}

# Function to start frontend
start_frontend() {
    echo -e "${BLUE}Starting Frontend...${NC}"
    cd frontend
    npm run dev &
    FRONTEND_PID=$!
    echo $FRONTEND_PID > ../frontend.pid
    cd ..
    echo -e "${GREEN}✓ Frontend started (PID: $FRONTEND_PID)${NC}"
}

# Start services
if [ "$USE_TMUX" = true ]; then
    # Create tmux session
    tmux new-session -d -s smsbomb
    
    # Backend window
    tmux rename-window -t smsbomb:0 'backend'
    tmux send-keys -t smsbomb:0 'cd backend && python main.py' C-m
    
    # Frontend window
    tmux new-window -t smsbomb:1 -n 'frontend'
    tmux send-keys -t smsbomb:1 'cd frontend && npm run dev' C-m
    
    echo ""
    echo -e "${GREEN}✅ Services started in tmux session 'smsbomb'${NC}"
    echo ""
    echo "Commands:"
    echo "  tmux attach -t smsbomb  - Attach to session"
    echo "  tmux kill-session -t smsbomb  - Stop all services"
    echo ""
    
    # Attach to session
    tmux attach -t smsbomb
else
    # Start in background
    start_backend
    sleep 2
    start_frontend
    
    echo ""
    echo -e "${GREEN}✅ Services started in background${NC}"
    echo ""
    echo "Access points:"
    echo "  Frontend: http://localhost:5173"
    echo "  Backend:  http://localhost:8000"
    echo "  API Docs: http://localhost:8000/docs"
    echo ""
    echo "To stop services:"
    echo "  ./scripts/stop-dev.sh"
    echo ""
    
    # Wait for user interrupt
    echo "Press Ctrl+C to stop all services..."
    trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; rm -f backend.pid frontend.pid; exit" INT
    wait
fi