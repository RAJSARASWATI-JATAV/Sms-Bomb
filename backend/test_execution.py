"""
Test script for Campaign Execution Engine
Demonstrates Phase 4 functionality
"""

import asyncio
import sys
from datetime import datetime

# Add backend to path
sys.path.insert(0, '.')

from database import AsyncSessionLocal, init_db
from models import User, Campaign, CampaignStatus, CampaignMode
from auth import get_password_hash
from task_manager import get_task_manager


async def create_test_user():
    """Create a test user"""
    async with AsyncSessionLocal() as db:
        from sqlalchemy import select
        
        # Check if user exists
        result = await db.execute(
            select(User).where(User.username == "testuser")
        )
        user = result.scalar_one_or_none()
        
        if user:
            print("✅ Test user already exists")
            return user.id
        
        # Create user
        user = User(
            username="testuser",
            email="test@example.com",
            hashed_password=get_password_hash("testpass123"),
            full_name="Test User",
            is_active=True
        )
        
        db.add(user)
        await db.commit()
        await db.refresh(user)
        
        print(f"✅ Created test user: {user.username} (ID: {user.id})")
        return user.id


async def create_test_campaign(user_id: int):
    """Create a test campaign"""
    async with AsyncSessionLocal() as db:
        campaign = Campaign(
            user_id=user_id,
            name="Test Campaign - Phase 4 Demo",
            description="Demonstrating campaign execution engine",
            mode=CampaignMode.NORMAL,
            targets=["+1234567890", "+0987654321", "+1111111111"],
            target_count=3,
            waves=2,
            delay_seconds=3,
            use_proxy=False,
            use_vpn=False,
            randomize_apis=True,
            status=CampaignStatus.PENDING
        )
        
        db.add(campaign)
        await db.commit()
        await db.refresh(campaign)
        
        print(f"✅ Created campaign: {campaign.name} (ID: {campaign.id})")
        print(f"   Targets: {len(campaign.targets)}")
        print(f"   Waves: {campaign.waves}")
        print(f"   Delay: {campaign.delay_seconds}s")
        
        return campaign.id


async def monitor_campaign(campaign_id: int, duration: int = 30):
    """Monitor campaign progress"""
    print(f"\n📊 Monitoring campaign {campaign_id} for {duration} seconds...")
    print("=" * 60)
    
    start_time = datetime.utcnow()
    
    while (datetime.utcnow() - start_time).total_seconds() < duration:
        async with AsyncSessionLocal() as db:
            from sqlalchemy import select
            
            result = await db.execute(
                select(Campaign).where(Campaign.id == campaign_id)
            )
            campaign = result.scalar_one_or_none()
            
            if not campaign:
                print("❌ Campaign not found")
                break
            
            # Calculate progress
            total_expected = campaign.target_count * campaign.waves
            progress = (campaign.total_requests / total_expected * 100) if total_expected > 0 else 0
            
            # Display status
            print(f"\r⏱️  Status: {campaign.status.value.upper()} | "
                  f"Progress: {progress:.1f}% | "
                  f"Requests: {campaign.total_requests}/{total_expected} | "
                  f"Success: {campaign.successful_requests} | "
                  f"Failed: {campaign.failed_requests} | "
                  f"Rate: {campaign.success_rate:.1f}%", end="")
            
            # Check if completed
            if campaign.status in [CampaignStatus.COMPLETED, CampaignStatus.FAILED, CampaignStatus.CANCELLED]:
                print("\n")
                print("=" * 60)
                print(f"✅ Campaign {campaign.status.value}!")
                print(f"   Total Requests: {campaign.total_requests}")
                print(f"   Successful: {campaign.successful_requests}")
                print(f"   Failed: {campaign.failed_requests}")
                print(f"   Success Rate: {campaign.success_rate:.2f}%")
                if campaign.duration_seconds:
                    print(f"   Duration: {campaign.duration_seconds}s")
                break
        
        await asyncio.sleep(1)


async def main():
    """Main test function"""
    print("🚀 Phase 4: Campaign Execution Engine Test")
    print("=" * 60)
    
    # Initialize database
    print("\n📦 Initializing database...")
    await init_db()
    print("✅ Database initialized")
    
    # Create test user
    print("\n👤 Creating test user...")
    user_id = await create_test_user()
    
    # Create test campaign
    print("\n📋 Creating test campaign...")
    campaign_id = await create_test_campaign(user_id)
    
    # Start campaign
    print(f"\n🎯 Starting campaign {campaign_id}...")
    task_manager = get_task_manager()
    success = await task_manager.start_campaign(campaign_id)
    
    if not success:
        print("❌ Failed to start campaign")
        return
    
    print("✅ Campaign started in background")
    
    # Monitor campaign
    await monitor_campaign(campaign_id, duration=30)
    
    # Show final statistics
    print("\n📈 Final Statistics:")
    async with AsyncSessionLocal() as db:
        from sqlalchemy import select, func
        from models import CampaignLog, APIGateway
        
        # Get campaign
        result = await db.execute(
            select(Campaign).where(Campaign.id == campaign_id)
        )
        campaign = result.scalar_one_or_none()
        
        if campaign:
            print(f"   Campaign: {campaign.name}")
            print(f"   Status: {campaign.status.value}")
            print(f"   Total Requests: {campaign.total_requests}")
            print(f"   Successful: {campaign.successful_requests}")
            print(f"   Failed: {campaign.failed_requests}")
            print(f"   Success Rate: {campaign.success_rate:.2f}%")
        
        # Get log count
        log_count = await db.execute(
            select(func.count(CampaignLog.id)).where(
                CampaignLog.campaign_id == campaign_id
            )
        )
        print(f"   Log Entries: {log_count.scalar()}")
        
        # Get API stats
        api_count = await db.execute(select(func.count(APIGateway.id)))
        print(f"   Available APIs: {api_count.scalar()}")
    
    print("\n✨ Test completed successfully!")
    print("=" * 60)
    
    # Cleanup
    await task_manager.cleanup()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()