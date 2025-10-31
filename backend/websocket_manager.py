"""
WebSocket Manager - Phase 5
Handles real-time updates for campaigns, monitoring, and notifications
"""

import asyncio
import json
from typing import Dict, Set, Optional, Any
from datetime import datetime
from fastapi import WebSocket, WebSocketDisconnect
import logging

logger = logging.getLogger(__name__)


class ConnectionManager:
    """Manages WebSocket connections for real-time updates"""
    
    def __init__(self):
        # Store active connections by user_id
        self.active_connections: Dict[int, Set[WebSocket]] = {}
        
        # Store connections by campaign_id for campaign-specific updates
        self.campaign_connections: Dict[int, Set[WebSocket]] = {}
        
        # Store all connections for broadcast
        self.all_connections: Set[WebSocket] = set()
        
        # Lock for thread-safe operations
        self.lock = asyncio.Lock()
    
    async def connect(self, websocket: WebSocket, user_id: int):
        """Accept and register a new WebSocket connection"""
        await websocket.accept()
        
        async with self.lock:
            # Add to user-specific connections
            if user_id not in self.active_connections:
                self.active_connections[user_id] = set()
            self.active_connections[user_id].add(websocket)
            
            # Add to all connections
            self.all_connections.add(websocket)
        
        logger.info(f"WebSocket connected for user {user_id}")
        
        # Send welcome message
        await self.send_personal_message({
            "type": "connection",
            "status": "connected",
            "message": "WebSocket connection established",
            "timestamp": datetime.utcnow().isoformat()
        }, websocket)
    
    async def disconnect(self, websocket: WebSocket, user_id: int):
        """Remove a WebSocket connection"""
        async with self.lock:
            # Remove from user-specific connections
            if user_id in self.active_connections:
                self.active_connections[user_id].discard(websocket)
                if not self.active_connections[user_id]:
                    del self.active_connections[user_id]
            
            # Remove from campaign connections
            for campaign_id in list(self.campaign_connections.keys()):
                self.campaign_connections[campaign_id].discard(websocket)
                if not self.campaign_connections[campaign_id]:
                    del self.campaign_connections[campaign_id]
            
            # Remove from all connections
            self.all_connections.discard(websocket)
        
        logger.info(f"WebSocket disconnected for user {user_id}")
    
    async def subscribe_to_campaign(self, websocket: WebSocket, campaign_id: int):
        """Subscribe a connection to campaign-specific updates"""
        async with self.lock:
            if campaign_id not in self.campaign_connections:
                self.campaign_connections[campaign_id] = set()
            self.campaign_connections[campaign_id].add(websocket)
        
        logger.info(f"WebSocket subscribed to campaign {campaign_id}")
    
    async def unsubscribe_from_campaign(self, websocket: WebSocket, campaign_id: int):
        """Unsubscribe a connection from campaign updates"""
        async with self.lock:
            if campaign_id in self.campaign_connections:
                self.campaign_connections[campaign_id].discard(websocket)
                if not self.campaign_connections[campaign_id]:
                    del self.campaign_connections[campaign_id]
        
        logger.info(f"WebSocket unsubscribed from campaign {campaign_id}")
    
    async def send_personal_message(self, message: Dict[str, Any], websocket: WebSocket):
        """Send a message to a specific connection"""
        try:
            await websocket.send_json(message)
        except Exception as e:
            logger.error(f"Error sending personal message: {e}")
    
    async def send_to_user(self, message: Dict[str, Any], user_id: int):
        """Send a message to all connections of a specific user"""
        if user_id not in self.active_connections:
            return
        
        disconnected = set()
        for connection in self.active_connections[user_id]:
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Error sending to user {user_id}: {e}")
                disconnected.add(connection)
        
        # Clean up disconnected connections
        if disconnected:
            async with self.lock:
                self.active_connections[user_id] -= disconnected
    
    async def send_to_campaign(self, message: Dict[str, Any], campaign_id: int):
        """Send a message to all connections subscribed to a campaign"""
        if campaign_id not in self.campaign_connections:
            return
        
        disconnected = set()
        for connection in self.campaign_connections[campaign_id]:
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Error sending to campaign {campaign_id}: {e}")
                disconnected.add(connection)
        
        # Clean up disconnected connections
        if disconnected:
            async with self.lock:
                self.campaign_connections[campaign_id] -= disconnected
    
    async def broadcast(self, message: Dict[str, Any]):
        """Broadcast a message to all connected clients"""
        disconnected = set()
        for connection in self.all_connections:
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Error broadcasting: {e}")
                disconnected.add(connection)
        
        # Clean up disconnected connections
        if disconnected:
            async with self.lock:
                self.all_connections -= disconnected
    
    def get_connection_count(self) -> int:
        """Get total number of active connections"""
        return len(self.all_connections)
    
    def get_user_connection_count(self, user_id: int) -> int:
        """Get number of connections for a specific user"""
        return len(self.active_connections.get(user_id, set()))
    
    def get_campaign_subscriber_count(self, campaign_id: int) -> int:
        """Get number of connections subscribed to a campaign"""
        return len(self.campaign_connections.get(campaign_id, set()))


# Global connection manager instance
_connection_manager: Optional[ConnectionManager] = None


def get_connection_manager() -> ConnectionManager:
    """Get or create connection manager singleton"""
    global _connection_manager
    if _connection_manager is None:
        _connection_manager = ConnectionManager()
    return _connection_manager


class WebSocketEventEmitter:
    """Emits events to WebSocket clients"""
    
    def __init__(self, connection_manager: ConnectionManager):
        self.manager = connection_manager
    
    async def emit_campaign_started(self, campaign_id: int, campaign_data: Dict[str, Any]):
        """Emit campaign started event"""
        message = {
            "type": "campaign_started",
            "campaign_id": campaign_id,
            "data": campaign_data,
            "timestamp": datetime.utcnow().isoformat()
        }
        await self.manager.send_to_campaign(message, campaign_id)
    
    async def emit_campaign_progress(self, campaign_id: int, progress_data: Dict[str, Any]):
        """Emit campaign progress update"""
        message = {
            "type": "campaign_progress",
            "campaign_id": campaign_id,
            "data": progress_data,
            "timestamp": datetime.utcnow().isoformat()
        }
        await self.manager.send_to_campaign(message, campaign_id)
    
    async def emit_campaign_completed(self, campaign_id: int, result_data: Dict[str, Any]):
        """Emit campaign completed event"""
        message = {
            "type": "campaign_completed",
            "campaign_id": campaign_id,
            "data": result_data,
            "timestamp": datetime.utcnow().isoformat()
        }
        await self.manager.send_to_campaign(message, campaign_id)
    
    async def emit_campaign_failed(self, campaign_id: int, error_data: Dict[str, Any]):
        """Emit campaign failed event"""
        message = {
            "type": "campaign_failed",
            "campaign_id": campaign_id,
            "data": error_data,
            "timestamp": datetime.utcnow().isoformat()
        }
        await self.manager.send_to_campaign(message, campaign_id)
    
    async def emit_campaign_paused(self, campaign_id: int):
        """Emit campaign paused event"""
        message = {
            "type": "campaign_paused",
            "campaign_id": campaign_id,
            "timestamp": datetime.utcnow().isoformat()
        }
        await self.manager.send_to_campaign(message, campaign_id)
    
    async def emit_campaign_resumed(self, campaign_id: int):
        """Emit campaign resumed event"""
        message = {
            "type": "campaign_resumed",
            "campaign_id": campaign_id,
            "timestamp": datetime.utcnow().isoformat()
        }
        await self.manager.send_to_campaign(message, campaign_id)
    
    async def emit_request_completed(self, campaign_id: int, request_data: Dict[str, Any]):
        """Emit individual request completed event"""
        message = {
            "type": "request_completed",
            "campaign_id": campaign_id,
            "data": request_data,
            "timestamp": datetime.utcnow().isoformat()
        }
        await self.manager.send_to_campaign(message, campaign_id)
    
    async def emit_api_health_update(self, api_data: Dict[str, Any]):
        """Emit API health status update"""
        message = {
            "type": "api_health_update",
            "data": api_data,
            "timestamp": datetime.utcnow().isoformat()
        }
        await self.manager.broadcast(message)
    
    async def emit_system_metrics(self, metrics_data: Dict[str, Any]):
        """Emit system metrics update"""
        message = {
            "type": "system_metrics",
            "data": metrics_data,
            "timestamp": datetime.utcnow().isoformat()
        }
        await self.manager.broadcast(message)
    
    async def emit_notification(self, user_id: int, notification_data: Dict[str, Any]):
        """Emit notification to specific user"""
        message = {
            "type": "notification",
            "data": notification_data,
            "timestamp": datetime.utcnow().isoformat()
        }
        await self.manager.send_to_user(message, user_id)


def get_event_emitter() -> WebSocketEventEmitter:
    """Get event emitter instance"""
    return WebSocketEventEmitter(get_connection_manager())