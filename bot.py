import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🎉 Welcome to VIP Rewards!

Unlock member benefits, exclusive content, and community perks.

Commands:
/help - View commands
/rewards - View benefits
/profile - Your account
"""
    await update.message.reply_text(text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Use /rewards to see available benefits."
    )

async def rewards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⭐ Exclusive Content\n🎁 Special Offers\n🏆 Loyalty Rewards"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("rewards", rewards))

    app.run_polling()

if __name__ == "__main__":
    main()
