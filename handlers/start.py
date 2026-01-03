from telegram import Update
from telegram.ext import ContextTypes

async def start(update:Update, contect:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(" Crypto Price Bot\n\n"
        "Commands:\n"
        "/price bitcoin\n"
        "/price ethereum\n"
        "/price dogecoin")
