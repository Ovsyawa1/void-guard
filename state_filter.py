class MyStates():
    free_trial = "free_trial"
    choose_rate = "choose_rate"
    free_trial_activation = "free_trial_activation"
    android_instruction = "android_instruction"


any_entry_state = [
    MyStates.choose_rate, 
    MyStates.free_trial, 
    MyStates.free_trial_activation, 
    MyStates.android_instruction,
]