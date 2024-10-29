from telebot import types

import text_for_buttons

### клавиатура после старта
start_kb = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)
start_kb.add(text_for_buttons.free_trial_button_text)
start_kb.add(text_for_buttons.choose_rate_button_text)
start_kb.add(text_for_buttons.help_button_text)
start_kb.add(text_for_buttons.call_us_button_text)

### клавиатура после помощи
help_kb = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)
help_kb.add(text_for_buttons.free_trial_button_text)
help_kb.add(text_for_buttons.choose_rate_button_text)
help_kb.add(text_for_buttons.call_us_button_text)

### клавиатура после выбора бесплатного тарифа
free_trial_kb = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)
free_trial_kb.add(text_for_buttons.activate_free_trial_button_text)
free_trial_kb.add(text_for_buttons.choose_paying_rate_button_text)
free_trial_kb.add(text_for_buttons.go_back_button_text)

### клавиатура активации бесплатного тарифа
free_trial_activation_kb = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)
free_trial_activation_kb.add(
    text_for_buttons.android_button_text, 
    text_for_buttons.ios_button_text
)
free_trial_activation_kb.add(
    text_for_buttons.windows_button_text,
    text_for_buttons.macos_button_text
)
free_trial_activation_kb.add(text_for_buttons.go_back_button_text)

### клавиаутра после инструкций
after_insruction_kb = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)
after_insruction_kb.add(text_for_buttons.complete_installation_button_text)
after_insruction_kb.add(text_for_buttons.problems_button_text)

### клавиатура для отмены действия
cancel_kb = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)
cancel_kb.add("Отмена")
