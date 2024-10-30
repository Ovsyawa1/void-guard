class ChattingStates():
    free_trial = "free_trial"
    choose_rate = "choose_rate"
    free_trial_activation = "free_trial_activation"
    android_instruction = "android_instruction"


any_entry_state = [
    ChattingStates.choose_rate, 
    ChattingStates.free_trial, 
    ChattingStates.free_trial_activation, 
    ChattingStates.android_instruction,
]