import openai 
from dotenv import load_dotenv
import telebot
import os
from openai import OpenAI
from loguru import logger



load_dotenv()

# Initialize the OpenAI API with your API key
openai.api_key = os.getenv('OPENAI_API_KEY')
# Initialize the Telegram bot with your token
bot = telebot.TeleBot(os.getenv("TOKEN"), parse_mode=None)
BOT_USERNAME = bot.get_me().username
