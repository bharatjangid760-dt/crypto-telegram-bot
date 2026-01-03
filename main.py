from telegram.ext import ApplicationBuilder, CommandHandler
from config import token
from handlers.start import start
from handlers.price import price

def main():
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))

    print("Crypto bot is running...")
    app.run_polling(close_loop=False)

if __name__=="__main__":
    main()


