from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from dotenv import load_dotenv
from .handlers import start#, help, like, dislike


load_dotenv()

token = os.getenv("TOKEN")

def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
   