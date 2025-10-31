#!/usr/bin/env python3
"""
SMS-POWERBOMB v10.0 - Telegram Bot
Complete bot implementation for remote control
"""

import os
import sys
import asyncio
import logging
from typing import Optional, Dict, Any
from datetime import datetime

try:
    from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
    from telegram.ext import (
        Application,
        CommandHandler,
        CallbackQueryHandler,
        MessageHandler,
        ContextTypes,
        filters
    )
    import httpx
except ImportError:
    print("❌ Required packages not installed!")
    print("Run: pip install python-telegram-bot httpx")
    sys.exit(1)

# Configuration
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
ALLOWED_USERS = os.getenv("ALLOWED_USERS", "").split(",")

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class SMSBomberBot:
    """SMS Bomber Telegram Bot"""
    
    def __init__(self, token: str, backend_url: str):
        self.token = token
        self.backend_url = backend_url
        self.active_campaigns: Dict[int, str] = {}
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Start command handler"""
        user = update.effective_user
        
        welcome_message = f"""
🔥 *SMS-POWERBOMB v10.0 Bot*

Welcome {user.mention_html()}!

🎯 *Available Commands:*
/bomb - Start SMS bombing
/status - Check campaign status
/stop - Stop active campaign
/stats - View statistics
/apis - Check API health
/help - Show help message

⚠️ *Disclaimer:* Use responsibly and ethically!

Created by: *RAJSARASWATI JATAV*
        """
        
        keyboard = [
            [
                InlineKeyboardButton("🚀 Start Bombing", callback_data="start_bomb"),
                InlineKeyboardButton("📊 Statistics", callback_data="stats")
            ],
            [
                InlineKeyboardButton("🔧 API Status", callback_data="api_status"),
                InlineKeyboardButton("ℹ️ Help", callback_data="help")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_html(welcome_message, reply_markup=reply_markup)
    
    async def bomb_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Bomb command handler"""
        if not context.args or len(context.args) < 2:
            await update.message.reply_text(
                "❌ *Invalid usage!*\n\n"
                "Usage: `/bomb <phone> <count> [mode]`\n\n"
                "Example: `/bomb 9876543210 5 normal`\n\n"
                "Modes: normal, stealth, turbo, smart",
                parse_mode="Markdown"
            )
            return
        
        phone = context.args[0]
        try:
            count = int(context.args[1])
        except ValueError:
            await update.message.reply_text("❌ Count must be a number!")
            return
        
        mode = context.args[2] if len(context.args) > 2 else "normal"
        
        # Validate phone
        if not self._validate_phone(phone):
            await update.message.reply_text("❌ Invalid phone number! Must be 10 digits.")
            return
        
        # Start bombing
        await update.message.reply_text(
            f"🚀 *Starting SMS Bombing*\n\n"
            f"📱 Target: `{phone}`\n"
            f"🔢 Waves: {count}\n"
            f"⚙️ Mode: {mode}\n\n"
            f"⏳ Please wait...",
            parse_mode="Markdown"
        )
        
        # Call backend API
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.backend_url}/api/v1/campaigns/start",
                    json={
                        "phone": phone,
                        "count": count,
                        "mode": mode,
                        "source": "telegram"
                    },
                    timeout=30.0
                )
                
                if response.status_code == 200:
                    data = response.json()
                    campaign_id = data.get("campaign_id")
                    self.active_campaigns[update.effective_user.id] = campaign_id
                    
                    await update.message.reply_text(
                        f"✅ *Campaign Started!*\n\n"
                        f"🆔 Campaign ID: `{campaign_id}`\n"
                        f"📊 Use /status to check progress",
                        parse_mode="Markdown"
                    )
                else:
                    await update.message.reply_text(
                        f"❌ Failed to start campaign: {response.text}"
                    )
        except Exception as e:
            logger.error(f"Error starting campaign: {e}")
            await update.message.reply_text(
                f"❌ Error: {str(e)}\n\n"
                f"Make sure backend is running!"
            )
    
    async def status_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Status command handler"""
        user_id = update.effective_user.id
        
        if user_id not in self.active_campaigns:
            await update.message.reply_text("❌ No active campaign found!")
            return
        
        campaign_id = self.active_campaigns[user_id]
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.backend_url}/api/v1/campaigns/{campaign_id}",
                    timeout=10.0
                )
                
                if response.status_code == 200:
                    data = response.json()
                    
                    status_msg = f"""
📊 *Campaign Status*

🆔 ID: `{campaign_id}`
📱 Phone: `{data.get('phone', 'N/A')}`
📈 Status: {data.get('status', 'Unknown')}

✅ Success: {data.get('success_count', 0)}
❌ Failed: {data.get('fail_count', 0)}
📊 Success Rate: {data.get('success_rate', 0):.1f}%
⏱️ Duration: {data.get('duration', 'N/A')}

🕐 Started: {data.get('started_at', 'N/A')}
                    """
                    
                    await update.message.reply_text(status_msg, parse_mode="Markdown")
                else:
                    await update.message.reply_text("❌ Failed to fetch status")
        except Exception as e:
            logger.error(f"Error fetching status: {e}")
            await update.message.reply_text(f"❌ Error: {str(e)}")
    
    async def stop_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Stop command handler"""
        user_id = update.effective_user.id
        
        if user_id not in self.active_campaigns:
            await update.message.reply_text("❌ No active campaign to stop!")
            return
        
        campaign_id = self.active_campaigns[user_id]
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.backend_url}/api/v1/campaigns/{campaign_id}/stop",
                    timeout=10.0
                )
                
                if response.status_code == 200:
                    del self.active_campaigns[user_id]
                    await update.message.reply_text("✅ Campaign stopped successfully!")
                else:
                    await update.message.reply_text("❌ Failed to stop campaign")
        except Exception as e:
            logger.error(f"Error stopping campaign: {e}")
            await update.message.reply_text(f"❌ Error: {str(e)}")
    
    async def stats_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Statistics command handler"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.backend_url}/api/v1/dashboard/stats",
                    timeout=10.0
                )
                
                if response.status_code == 200:
                    data = response.json()
                    
                    stats_msg = f"""
📈 *Overall Statistics*

🎯 Total Campaigns: {data.get('total_campaigns', 0)}
✅ Successful: {data.get('successful_campaigns', 0)}
❌ Failed: {data.get('failed_campaigns', 0)}

📊 Total SMS Sent: {data.get('total_sms', 0)}
📈 Success Rate: {data.get('overall_success_rate', 0):.1f}%

🔧 Active APIs: {data.get('active_apis', 0)}
⚡ Avg Response Time: {data.get('avg_response_time', 0):.2f}s
                    """
                    
                    await update.message.reply_text(stats_msg, parse_mode="Markdown")
                else:
                    await update.message.reply_text("❌ Failed to fetch statistics")
        except Exception as e:
            logger.error(f"Error fetching stats: {e}")
            await update.message.reply_text(f"❌ Error: {str(e)}")
    
    async def apis_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """API status command handler"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.backend_url}/api/v1/apis/status",
                    timeout=10.0
                )
                
                if response.status_code == 200:
                    data = response.json()
                    apis = data.get('apis', [])
                    
                    status_msg = "🔧 *API Status*\n\n"
                    
                    for api in apis[:10]:  # Show first 10
                        name = api.get('name', 'Unknown')
                        active = api.get('active', False)
                        success_rate = api.get('success_rate', 0)
                        
                        status = "✅" if active else "❌"
                        status_msg += f"{status} {name}: {success_rate:.0f}%\n"
                    
                    if len(apis) > 10:
                        status_msg += f"\n... and {len(apis) - 10} more"
                    
                    await update.message.reply_text(status_msg, parse_mode="Markdown")
                else:
                    await update.message.reply_text("❌ Failed to fetch API status")
        except Exception as e:
            logger.error(f"Error fetching API status: {e}")
            await update.message.reply_text(f"❌ Error: {str(e)}")
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Help command handler"""
        help_msg = """
📚 *SMS-POWERBOMB Bot Help*

*Commands:*
/start - Start the bot
/bomb <phone> <count> [mode] - Start bombing
/status - Check campaign status
/stop - Stop active campaign
/stats - View statistics
/apis - Check API health
/help - Show this help

*Bombing Modes:*
• normal - Balanced speed (default)
• stealth - Randomized patterns
• turbo - Maximum speed
• smart - AI-optimized

*Examples:*
`/bomb 9876543210 5` - Normal mode
`/bomb 9876543210 10 turbo` - Turbo mode
`/bomb 9876543210 3 stealth` - Stealth mode

⚠️ *Important:*
• Use responsibly and ethically
• Get consent before use
• For educational purposes only

Created by: *RAJSARASWATI JATAV*
        """
        
        await update.message.reply_text(help_msg, parse_mode="Markdown")
    
    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle button callbacks"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "start_bomb":
            await query.message.reply_text(
                "🚀 To start bombing, use:\n"
                "`/bomb <phone> <count> [mode]`\n\n"
                "Example: `/bomb 9876543210 5 normal`",
                parse_mode="Markdown"
            )
        elif query.data == "stats":
            await self.stats_command(update, context)
        elif query.data == "api_status":
            await self.apis_command(update, context)
        elif query.data == "help":
            await self.help_command(update, context)
    
    def _validate_phone(self, phone: str) -> bool:
        """Validate phone number"""
        phone = phone.replace(" ", "").replace("-", "").replace("+", "")
        
        if len(phone) == 10 and phone.isdigit() and phone[0] in ['6', '7', '8', '9']:
            return True
        
        if len(phone) == 12 and phone.startswith("91") and phone[2] in ['6', '7', '8', '9']:
            return True
        
        return False
    
    def run(self):
        """Run the bot"""
        if not self.token:
            logger.error("❌ TELEGRAM_BOT_TOKEN not set!")
            sys.exit(1)
        
        # Create application
        app = Application.builder().token(self.token).build()
        
        # Add handlers
        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(CommandHandler("bomb", self.bomb_command))
        app.add_handler(CommandHandler("status", self.status_command))
        app.add_handler(CommandHandler("stop", self.stop_command))
        app.add_handler(CommandHandler("stats", self.stats_command))
        app.add_handler(CommandHandler("apis", self.apis_command))
        app.add_handler(CommandHandler("help", self.help_command))
        app.add_handler(CallbackQueryHandler(self.button_callback))
        
        # Start bot
        logger.info("🤖 Starting SMS-POWERBOMB Telegram Bot...")
        logger.info(f"📡 Backend URL: {self.backend_url}")
        app.run_polling(allowed_updates=Update.ALL_TYPES)


def main():
    """Main entry point"""
    print("🤖 SMS-POWERBOMB v10.0 - Telegram Bot")
    print("=" * 50)
    
    if not BOT_TOKEN:
        print("❌ Error: TELEGRAM_BOT_TOKEN environment variable not set!")
        print("\nSet it using:")
        print("  export TELEGRAM_BOT_TOKEN='your_token_here'")
        sys.exit(1)
    
    bot = SMSBomberBot(BOT_TOKEN, BACKEND_URL)
    bot.run()


if __name__ == "__main__":
    main()