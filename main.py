from emotion_controller import load_state, save_state, update_emotion

state = load_state()

state = update_emotion(state)

save_state(state)
