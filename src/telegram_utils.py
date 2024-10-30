from bot import bot
from loguru import logger
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup


def send_telegram_message(
    bot,
    chat_id,
    text,
    edit_message_id=None,
    reply_to_message_id=None,
    reply_markup=None,
):
    """Unified function to send, edit, or reply to messages in a Telegram bot.

    :param bot: The Telegram bot instance
    :param chat_id: The chat ID to send the message to
    :param text: The text of the message
    :param message_id: The message ID to edit (if editing an existing message)
    :param reply_to_message_id: The message ID to reply to (if replying to a message)
    :param reply_markup: Optional reply markup (e.g., inline keyboard)
    :return: The sent message object
    """
    if edit_message_id:
        # Edit existing message
        return bot.edit_message_text(
            chat_id=chat_id,
            message_id=edit_message_id,
            text=text,
            reply_markup=reply_markup,
        )
    if reply_to_message_id:
        # Reply to a message
        return bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )
    # Send a new message
    return bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=reply_markup,
    )
    
    
def get_message_content(chat_id: int, message_id: int) -> str:
    """Get the content of a message by forwarding it to the same chat.
    Telegram bot cannot access the content of a message having just the message_id
    but we can forward the message to the same chat and get the content of the forwarded message.
    """
    try:
        # Forward the message to the same chat
        forwarded_message = bot.forward_message(chat_id, chat_id, message_id)

        # Get the content of the forwarded message
        if forwarded_message.content_type == "text":
            content = forwarded_message.text
        elif forwarded_message.content_type == "photo":
            content = forwarded_message.photo[-1].file_id
        elif forwarded_message.content_type == "document":
            content = forwarded_message.document.file_id
        # Add more content types as needed
        else:
            content = "Unsupported content type"

        # Delete the forwarded message
        bot.delete_message(chat_id, forwarded_message.message_id)

    except Exception as e:
        logger.error(f"Error forwarding message: {e}")
        return None
    else:
        return content