import os

import telebot
from celery import shared_task

bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))


@shared_task
def send_notification(habit, telegram_user_id):
    notification_message = (f"Напоминаю"
                            f"\"<b><u>{habit}</u></b>\"")

    bot.send_message(
        telegram_user_id,
        notification_message,
        parse_mode='html'
    )


bot.polling()
