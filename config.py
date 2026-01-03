import os
from dotenv import load_dotenv

load_dotenv()

token=os.getenv("8265179925:AAFw6PxMbk_HiVeeATYiQU_1O9jZ72tZ7m4")
url = os.getenv("https://api.coingecko.com/api/v3/simple/price")
currencies = os.getenv("usd, inr")