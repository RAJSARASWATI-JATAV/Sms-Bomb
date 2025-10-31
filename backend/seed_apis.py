"""
Seed script to populate API gateways
Run this to add sample SMS API gateways to the database
"""

import asyncio
from sqlalchemy import select
from database import AsyncSessionLocal, init_db
from models import APIGateway, APIStatus


# Sample API gateways (mock endpoints for testing)
SAMPLE_APIS = [
    {
        "name": "Twilio SMS API",
        "url": "https://api.twilio.com/2010-04-01/Accounts/ACCOUNT_SID/Messages.json",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_TOKEN"
        },
        "payload_template": {
            "To": "{phone}",
            "From": "+1234567890",
            "Body": "Test message"
        },
        "provider": "Twilio",
        "country": "USA",
        "priority": 9,
        "rate_limit_per_minute": 100,
        "rate_limit_per_hour": 5000
    },
    {
        "name": "Nexmo SMS API",
        "url": "https://rest.nexmo.com/sms/json",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "payload_template": {
            "from": "NEXMO",
            "to": "{phone}",
            "text": "Test message",
            "api_key": "YOUR_API_KEY",
            "api_secret": "YOUR_API_SECRET"
        },
        "provider": "Vonage/Nexmo",
        "country": "Global",
        "priority": 8,
        "rate_limit_per_minute": 80,
        "rate_limit_per_hour": 4000
    },
    {
        "name": "MessageBird API",
        "url": "https://rest.messagebird.com/messages",
        "method": "POST",
        "headers": {
            "Authorization": "AccessKey YOUR_ACCESS_KEY",
            "Content-Type": "application/json"
        },
        "payload_template": {
            "recipients": ["{phone}"],
            "originator": "MessageBird",
            "body": "Test message"
        },
        "provider": "MessageBird",
        "country": "Netherlands",
        "priority": 7,
        "rate_limit_per_minute": 60,
        "rate_limit_per_hour": 3000
    },
    {
        "name": "Plivo SMS API",
        "url": "https://api.plivo.com/v1/Account/AUTH_ID/Message/",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Basic YOUR_AUTH"
        },
        "payload_template": {
            "src": "+1234567890",
            "dst": "{phone}",
            "text": "Test message"
        },
        "provider": "Plivo",
        "country": "USA",
        "priority": 7,
        "rate_limit_per_minute": 70,
        "rate_limit_per_hour": 3500
    },
    {
        "name": "Sinch SMS API",
        "url": "https://us.sms.api.sinch.com/xms/v1/SERVICE_PLAN_ID/batches",
        "method": "POST",
        "headers": {
            "Authorization": "Bearer YOUR_TOKEN",
            "Content-Type": "application/json"
        },
        "payload_template": {
            "from": "SINCH",
            "to": ["{phone}"],
            "body": "Test message"
        },
        "provider": "Sinch",
        "country": "Sweden",
        "priority": 6,
        "rate_limit_per_minute": 50,
        "rate_limit_per_hour": 2500
    },
    {
        "name": "Clickatell API",
        "url": "https://platform.clickatell.com/messages",
        "method": "POST",
        "headers": {
            "Authorization": "YOUR_API_KEY",
            "Content-Type": "application/json"
        },
        "payload_template": {
            "to": ["{phone}"],
            "content": "Test message"
        },
        "provider": "Clickatell",
        "country": "South Africa",
        "priority": 6,
        "rate_limit_per_minute": 60,
        "rate_limit_per_hour": 3000
    },
    {
        "name": "Infobip SMS API",
        "url": "https://api.infobip.com/sms/2/text/advanced",
        "method": "POST",
        "headers": {
            "Authorization": "App YOUR_API_KEY",
            "Content-Type": "application/json"
        },
        "payload_template": {
            "messages": [
                {
                    "from": "InfoSMS",
                    "destinations": [{"to": "{phone}"}],
                    "text": "Test message"
                }
            ]
        },
        "provider": "Infobip",
        "country": "Croatia",
        "priority": 8,
        "rate_limit_per_minute": 100,
        "rate_limit_per_hour": 5000
    },
    {
        "name": "Telnyx SMS API",
        "url": "https://api.telnyx.com/v2/messages",
        "method": "POST",
        "headers": {
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json"
        },
        "payload_template": {
            "from": "+1234567890",
            "to": "{phone}",
            "text": "Test message"
        },
        "provider": "Telnyx",
        "country": "USA",
        "priority": 7,
        "rate_limit_per_minute": 90,
        "rate_limit_per_hour": 4500
    },
    {
        "name": "Bandwidth SMS API",
        "url": "https://messaging.bandwidth.com/api/v2/users/ACCOUNT_ID/messages",
        "method": "POST",
        "headers": {
            "Authorization": "Basic YOUR_AUTH",
            "Content-Type": "application/json"
        },
        "payload_template": {
            "from": "+1234567890",
            "to": ["{phone}"],
            "text": "Test message",
            "applicationId": "APP_ID"
        },
        "provider": "Bandwidth",
        "country": "USA",
        "priority": 6,
        "rate_limit_per_minute": 60,
        "rate_limit_per_hour": 3000
    },
    {
        "name": "46elks SMS API",
        "url": "https://api.46elks.com/a1/sms",
        "method": "POST",
        "headers": {
            "Authorization": "Basic YOUR_AUTH",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "payload_template": {
            "from": "46elks",
            "to": "{phone}",
            "message": "Test message"
        },
        "provider": "46elks",
        "country": "Sweden",
        "priority": 5,
        "rate_limit_per_minute": 40,
        "rate_limit_per_hour": 2000
    }
]


async def seed_apis():
    """Seed API gateways into database"""
    
    print("🌱 Seeding API gateways...")
    
    # Initialize database
    await init_db()
    
    async with AsyncSessionLocal() as db:
        try:
            # Check existing APIs
            result = await db.execute(select(APIGateway))
            existing_apis = {api.name for api in result.scalars().all()}
            
            added_count = 0
            skipped_count = 0
            
            for api_data in SAMPLE_APIS:
                if api_data["name"] in existing_apis:
                    print(f"⏭️  Skipping {api_data['name']} (already exists)")
                    skipped_count += 1
                    continue
                
                # Create API gateway
                api = APIGateway(
                    name=api_data["name"],
                    url=api_data["url"],
                    method=api_data["method"],
                    headers=api_data["headers"],
                    payload_template=api_data["payload_template"],
                    provider=api_data["provider"],
                    country=api_data["country"],
                    priority=api_data["priority"],
                    rate_limit_per_minute=api_data["rate_limit_per_minute"],
                    rate_limit_per_hour=api_data["rate_limit_per_hour"],
                    status=APIStatus.ACTIVE,
                    is_enabled=True
                )
                
                db.add(api)
                print(f"✅ Added {api_data['name']}")
                added_count += 1
            
            await db.commit()
            
            print(f"\n📊 Summary:")
            print(f"   ✅ Added: {added_count}")
            print(f"   ⏭️  Skipped: {skipped_count}")
            print(f"   📦 Total: {added_count + skipped_count}")
            print(f"\n🎉 Seeding completed!")
        
        except Exception as e:
            print(f"❌ Error seeding APIs: {e}")
            await db.rollback()
            raise


if __name__ == "__main__":
    asyncio.run(seed_apis())