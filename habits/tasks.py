import os

import telebot
from celery import shared_task

bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))


@shared_task
def send_notification(habit, telegram_user_id):
    """
    Отправляет уведомление пользователю в Telegram о выполнении привычки.
    habit: Название привычки, которую нужно отметить в уведомлении.
    Telegram_user_id: Идентификатор пользователя Telegram, который получит уведомление.
    """
    notification_message = (f"Напоминаю"
                            f"\"<b><u>{habit}</u></b>\"")

    bot.send_message(
        telegram_user_id,
        notification_message,
        parse_mode='html'
    )


bot.polling()
