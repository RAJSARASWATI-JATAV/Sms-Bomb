"""
Background Task Manager
Manages campaign execution as background tasks
"""

import asyncio
from typing import Dict, Optional
from sqlalchemy.ext.asyncio import AsyncSession
import logging

from execution_engine import CampaignExecutor
from database import AsyncSessionLocal

logger = logging.getLogger(__name__)


class TaskManager:
    """Manages background campaign execution tasks"""
    
    def __init__(self):
        self.tasks: Dict[int, asyncio.Task] = {}
        self.executors: Dict[int, CampaignExecutor] = {}
    
    async def start_campaign(self, campaign_id: int) -> bool:
        """
        Start campaign execution in background
        
        Returns:
            True if started successfully, False if already running
        """
        if campaign_id in self.tasks and not self.tasks[campaign_id].done():
            logger.warning(f"Campaign {campaign_id} is already running")
            return False
        
        # Create new database session for this task
        db = AsyncSessionLocal()
        
        try:
            # Create executor
            executor = CampaignExecutor(db)
            self.executors[campaign_id] = executor
            
            # Create and start task
            task = asyncio.create_task(
                self._run_campaign(campaign_id, executor, db)
            )
            self.tasks[campaign_id] = task
            
            logger.info(f"Started background task for campaign {campaign_id}")
            return True
        
        except Exception as e:
            logger.error(f"Error starting campaign {campaign_id}: {e}")
            await db.close()
            return False
    
    async def _run_campaign(
        self,
        campaign_id: int,
        executor: CampaignExecutor,
        db: AsyncSession
    ):
        """Run campaign and cleanup after completion"""
        try:
            await executor.execute_campaign(campaign_id)
        except Exception as e:
            logger.error(f"Error in campaign {campaign_id} execution: {e}")
        finally:
            # Cleanup
            await executor.close()
            await db.close()
            
            # Remove from tracking
            self.tasks.pop(campaign_id, None)
            self.executors.pop(campaign_id, None)
            
            logger.info(f"Cleaned up resources for campaign {campaign_id}")
    
    async def stop_campaign(self, campaign_id: int) -> bool:
        """
        Stop a running campaign
        
        Returns:
            True if stopped successfully, False if not running
        """
        if campaign_id not in self.tasks:
            logger.warning(f"Campaign {campaign_id} is not running")
            return False
        
        task = self.tasks[campaign_id]
        
        if task.done():
            logger.warning(f"Campaign {campaign_id} has already completed")
            return False
        
        # Signal executor to stop
        if campaign_id in self.executors:
            await self.executors[campaign_id].stop_campaign(campaign_id)
        
        # Cancel task
        task.cancel()
        
        try:
            await task
        except asyncio.CancelledError:
            logger.info(f"Campaign {campaign_id} cancelled successfully")
        
        return True
    
    def is_running(self, campaign_id: int) -> bool:
        """Check if campaign is currently running"""
        if campaign_id not in self.tasks:
            return False
        
        task = self.tasks[campaign_id]
        return not task.done()
    
    def get_running_campaigns(self) -> list[int]:
        """Get list of currently running campaign IDs"""
        return [
            campaign_id
            for campaign_id, task in self.tasks.items()
            if not task.done()
        ]
    
    async def stop_all(self):
        """Stop all running campaigns"""
        running = self.get_running_campaigns()
        
        for campaign_id in running:
            await self.stop_campaign(campaign_id)
        
        logger.info(f"Stopped {len(running)} running campaigns")
    
    async def cleanup(self):
        """Cleanup all resources"""
        await self.stop_all()
        
        # Close all executors
        for executor in self.executors.values():
            await executor.close()
        
        self.tasks.clear()
        self.executors.clear()


# Global task manager instance
_task_manager: Optional[TaskManager] = None


def get_task_manager() -> TaskManager:
    """Get or create task manager singleton"""
    global _task_manager
    if _task_manager is None:
        _task_manager = TaskManager()
    return _task_manager


async def cleanup_task_manager():
    """Cleanup task manager on shutdown"""
    global _task_manager
    if _task_manager:
        await _task_manager.cleanup()
        _task_manager = None