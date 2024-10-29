import keyboards
import messages
from globals import bot
from state_filter import MyStates


from telebot import types


def free_trial_message(message: types.Message):
    bot.set_state(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        state=MyStates.free_trial,
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.FREE_TRIAL_MESSAGE,
        parse_mode="HTML",
        reply_markup=keyboards.free_trial_kb,
    )


def free_trial_activation(message: types.Message):
    bot.set_state(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        state=MyStates.free_trial_activation,
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.FREE_TRIAL_ACTIVATION_MESSAGE,
        parse_mode="HTML",
        reply_markup=keyboards.free_trial_activation_kb,
    )


def android_instruction(message: types.Message):
    bot.set_state(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        state=MyStates.android_instruction,
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.ANDROID_INSTRUCTION,
        parse_mode="HTML",
        reply_markup=keyboards.after_insruction_kb,
    )


def instruction_completion(message: types.Message):
    bot.set_state(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        state=0,
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.COMPLETION_MESSAGE,
        parse_mode="HTML",
        reply_markup=types.ReplyKeyboardRemove(),
    )


def call_us(message: types.Message):
    bot.set_state(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        state=0,
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.CALL_US_MESSAGE,
        parse_mode="HTML",
        reply_markup=types.ReplyKeyboardRemove(),
    )