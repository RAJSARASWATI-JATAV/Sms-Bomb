"""
WebSocket Router - Phase 5
Handles WebSocket connections and real-time communication
"""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, Query, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
import json
import logging

from database import get_db
from auth import get_current_user_ws
from websocket_manager import get_connection_manager, get_event_emitter
from models import User

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/ws", tags=["WebSocket"])


@router.websocket("/connect")
async def websocket_endpoint(
    websocket: WebSocket,
    token: str = Query(...),
    db: AsyncSession = Depends(get_db)
):
    """
    Main WebSocket endpoint for real-time updates
    
    Query Parameters:
    - token: JWT authentication token
    
    Message Types (Client -> Server):
    - subscribe_campaign: Subscribe to campaign updates
    - unsubscribe_campaign: Unsubscribe from campaign updates
    - ping: Heartbeat message
    
    Message Types (Server -> Client):
    - connection: Connection established
    - campaign_started: Campaign execution started
    - campaign_progress: Campaign progress update
    - campaign_completed: Campaign completed
    - campaign_failed: Campaign failed
    - campaign_paused: Campaign paused
    - campaign_resumed: Campaign resumed
    - request_completed: Individual request completed
    - api_health_update: API health status changed
    - system_metrics: System metrics update
    - notification: User notification
    - pong: Heartbeat response
    """
    
    manager = get_connection_manager()
    user = None
    
    try:
        # Authenticate user
        user = await get_current_user_ws(token, db)
        
        if not user:
            await websocket.close(code=1008, reason="Authentication failed")
            return
        
        # Connect user
        await manager.connect(websocket, user.id)
        
        # Handle incoming messages
        while True:
            try:
                # Receive message
                data = await websocket.receive_text()
                message = json.loads(data)
                
                message_type = message.get("type")
                
                # Handle different message types
                if message_type == "subscribe_campaign":
                    campaign_id = message.get("campaign_id")
                    if campaign_id:
                        await manager.subscribe_to_campaign(websocket, campaign_id)
                        await manager.send_personal_message({
                            "type": "subscribed",
                            "campaign_id": campaign_id,
                            "message": f"Subscribed to campaign {campaign_id}"
                        }, websocket)
                
                elif message_type == "unsubscribe_campaign":
                    campaign_id = message.get("campaign_id")
                    if campaign_id:
                        await manager.unsubscribe_from_campaign(websocket, campaign_id)
                        await manager.send_personal_message({
                            "type": "unsubscribed",
                            "campaign_id": campaign_id,
                            "message": f"Unsubscribed from campaign {campaign_id}"
                        }, websocket)
                
                elif message_type == "ping":
                    # Heartbeat response
                    await manager.send_personal_message({
                        "type": "pong",
                        "timestamp": message.get("timestamp")
                    }, websocket)
                
                else:
                    logger.warning(f"Unknown message type: {message_type}")
            
            except json.JSONDecodeError:
                logger.error("Invalid JSON received")
                await manager.send_personal_message({
                    "type": "error",
                    "message": "Invalid JSON format"
                }, websocket)
            
            except Exception as e:
                logger.error(f"Error processing message: {e}")
    
    except WebSocketDisconnect:
        logger.info(f"WebSocket disconnected for user {user.id if user else 'unknown'}")
    
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
    
    finally:
        # Disconnect user
        if user:
            await manager.disconnect(websocket, user.id)


@router.get("/stats")
async def get_websocket_stats(
    token: str = Query(...),
    db: AsyncSession = Depends(get_db)
):
    """Get WebSocket connection statistics"""
    # Authenticate user
    current_user = await get_current_user_ws(token, db)
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    
    manager = get_connection_manager()
    
    return {
        "total_connections": manager.get_connection_count(),
        "user_connections": manager.get_user_connection_count(current_user.id),
        "active_users": len(manager.active_connections),
        "active_campaign_subscriptions": len(manager.campaign_connections)
    }