from telebot.types import BotCommand

default_commands = [
    BotCommand("start", "начало работы с ботом"),
    BotCommand("help", "помощь"),
    BotCommand("choose_rate", "выбрать тариф"),
    BotCommand("free_trial", "бесплатный пробный период"),
    BotCommand("call_us", "связаться с нами")
]