from telegram import Update
from telegram.ext import ContextTypes
from Crypto_bot import get_price

async def price(update:Update, context:ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Error: Command should a contain a argument \n Example: /price bitcoin")

    else : return None

    coin = context.args[0].lower()
    result = get_price(coin)

    final_result_reply = coin.upper() + " : Price: \n\n USD: " + usd + " \n INR: " + inr + "Thanks"

    if result:
        usd , inr = result
        await update.message.reply_text(
            final_result_reply, parse_mode="Markdown"
        )
    else: update.message.reply_text("Error: Coin not found")
