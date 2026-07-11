import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHAT_ID = os.getenv("CHAT_ID")

SCAN_INTERVAL = int(os.getenv("SCAN_INTERVAL", "30"))

MIN_LIQUIDITY = int(os.getenv("MIN_LIQUIDITY", "50000"))

MIN_VOLUME = int(os.getenv("MIN_VOLUME", "100000"))

DEXSCREENER_API = "https://api.dexscreener.com/latest/dex"

GECKO_API = "https://api.geckoterminal.com/api/v2"
