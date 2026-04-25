import json

def load_state():
    with open("character_state.json", "r") as f:
        return json.load(f)

def save_state(state):
    with open("character_state.json", "w") as f:
        json.dump(state, f, indent=2)

def update_emotion(state):
    current = state["emotional_state"]["state"]
    target = state["emotional_state"]["target_state"]

    if current == target:
        return state

    emotions = ["calm", "cheerful", "excited", "curious", "comforting", "reflective"]

    i = emotions.index(current)
    j = emotions.index(target)

    if i < j:
        i += 1
    elif i > j:
        i -= 1

    state["emotional_state"]["state"] = emotions[i]
    return state
