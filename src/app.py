from bot import bot
from loguru import logger
import telebot
import os
from handlers import handle_welcome, handle_message, handle_reaction
from filters import IsAdmin

# from telegram_utils import get_message_content
bot.add_custom_filter(IsAdmin())
bot.message_handler(commands=['start', 'help'])(handle_welcome)
bot.message_handler(func=lambda message: True, is_chat_admin=True)(handle_message)
bot.edited_message_handler(func=lambda message: True, is_chat_admin=True)(handle_message)
bot.message_reaction_handler(func=lambda message: message.new_reaction, is_chat_admin=True)(handle_reaction)

bot.infinity_polling(
        allowed_updates=[
            "message",
            "message_reaction",
            "edited_message",
        ],
    )