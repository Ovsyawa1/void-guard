from dotenv import load_dotenv
from os import getenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("Please provide BOT_TOKEN!")