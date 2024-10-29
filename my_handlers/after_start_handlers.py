import keyboards
import messages
from globals import bot


from telebot import types



def start_message(message: types.Message):
    bot.set_state(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        state=0,
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.START_MESSAGE,
        parse_mode="HTML",
        reply_markup=keyboards.start_kb,
    )


def help_message(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.HELP_MESSAGE,
        parse_mode="HTML",
        reply_markup=keyboards.help_kb,
    )