from telegram import Update,ReplyKeyboardMarkup,Keyboardbutton
from telegram.ext import CallbackContext
from .db import DB

db=DB('db.json')

def start(update:Update,context:CallbackContext):
    user=update.effective_user
    db.add(user.id,user.first_name)
    update.message.reply_text(
        text=f"hello{user.first_name} welcome to our bot",
        reply_markup=ReplyKeyboardMarkup(
        [[Keyboardbutton('👍'),Keyboardbutton('👎')]],
        resize_keyboard=True
        )
    )