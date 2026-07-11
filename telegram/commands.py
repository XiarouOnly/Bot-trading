from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update,
                context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🚀 Xiarou Scanner AI Online"
    )


async def help_command(update: Update,
                       context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

"""
/scan

/token

/watch

/help
"""
    )
