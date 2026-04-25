def update_emotion(state):
    current = state["emotional_state"]["state"]
    target = state["emotional_state"]["target_state"]
    speed = state["emotional_state"]["transition_speed"]

    if current == target:
        return state

    # simple step transition
    emotions = ["calm", "cheerful", "excited", "curious", "comforting", "reflective"]

    i = emotions.index(current)
    j = emotions.index(target)

    if i < j:
        i += 1 if speed > 0 else 0
    elif i > j:
        i -= 1 if speed > 0 else 0

    state["emotional_state"]["state"] = emotions[i]

    return state
