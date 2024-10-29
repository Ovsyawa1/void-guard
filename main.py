from globals import bot


from my_handlers.after_start_handlers import start_message, help_message
from my_handlers.free_trial_handlers import free_trial_message, free_trial_activation
from my_handlers.cancel_handler import cancel_process

from my_handlers.free_trial_handlers import android_instruction
from my_handlers.free_trial_handlers import instruction_completion
from my_handlers.free_trial_handlers import call_us
from state_filter import any_entry_state
import config, text_for_buttons
from commands import default_commands

from telebot import types, util, formatting, custom_filters

# добавляем стандартные фильтры
bot.add_custom_filter(custom_filters.TextMatchFilter()) # проверка на полное совпадение
bot.add_custom_filter(custom_filters.StateFilter(bot))

# начало блока обработчиков запросов

# обработчик команды отмены
@bot.message_handler(
    text=custom_filters.TextFilter(
        equals=text_for_buttons.go_back_button_text,
        ignore_case=True
    ),
    state=any_entry_state,
)
@bot.message_handler(
    commands=["cancel"],
    state=any_entry_state,
)
def handle_cancel_process(message: types.Message):
    cancel_process(message)
 

# обработчик команды старт   
@bot.message_handler(commands=['start'])
def handle_start_message(message: types.Message):
    start_message(message)

#обработчик команды помощь    
@bot.message_handler(
        text=custom_filters.TextFilter(
            equals=text_for_buttons.help_button_text,
            ignore_case=True,
        )
)
@bot.message_handler(commands=['help'])
def handle_help_message(message: types.Message):
    help_message(message)

#####
# блок обработок запросов бесплатного тарифа
#####

# обработчик команды на бесплатный тариф
@bot.message_handler(
        text=custom_filters.TextFilter(
            equals=text_for_buttons.free_trial_button_text,
            ignore_case=True,
        )
)
@bot.message_handler(commands=['free_trial'])
def handle_free_trial_message(message: types.Message):
    free_trial_message(message)
    
# обработать активацию бесплатного тарифа
@bot.message_handler(
    text=custom_filters.TextFilter(
        equals=text_for_buttons.activate_free_trial_button_text,
        ignore_case=True,
    )
)
def handle_free_trial_activation(message: types.Message):
    free_trial_activation(message)

# обработчик инструкции для дроида   
@bot.message_handler(
    text=custom_filters.TextFilter(
        equals=text_for_buttons.android_button_text,
        ignore_case=True,
    )
)
def handler_android_instruction(message: types.Message):
    android_instruction(message)

# обработчик выполнения инструкции
@bot.message_handler(
    text=custom_filters.TextFilter(
        equals=text_for_buttons.complete_installation_button_text,
        ignore_case=True,
    )
)
def handle_intruction_completion(message: types.Message):
    instruction_completion(message)

# обработчик, когда пользователь не справился
@bot.message_handler(
    text=custom_filters.TextFilter(
        equals=text_for_buttons.problems_button_text,
        ignore_case=True,
    )
)
def handle_call_us(message: types.Message):
    call_us(message)

if __name__ == "__main__":
    bot.enable_saving_states() # сохранять стейты пользователей
    bot.set_my_commands(default_commands) # установка стандартных комманд, которые видит пользователь
    bot.infinity_polling(skip_pending = True, allowed_updates = [])