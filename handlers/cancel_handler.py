import messages
from globals import bot


from telebot import types


def cancel_process(message:types.Message):
    bot.set_state(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        state=0,
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.CANCEL_MESSAGE,
        reply_markup=types.ReplyKeyboardRemove(),
        parse_mode="HTML"
    )