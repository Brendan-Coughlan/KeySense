import json
import keyboard
import datetime

pressed_keys = {}

def on_key_event(event):
    if event.name in pressed_keys:
        pressed_keys[event.name] += 1
    else:
        pressed_keys[event.name] = 1
    with open('keylog.txt', 'a') as f:
        timestamp = datetime.datetime.now()
        f.write(f'<{timestamp}> {event.name}\n')
        print(f'<{timestamp}> {event.name}')

def save_key_stats(stats, filename='keystats.json'):
    with open(filename, 'w') as f:
        json.dump(stats, f)

def load_key_stats(filename='keystats.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

pressed_keys = load_key_stats()
keyboard.on_press(on_key_event)

keyboard.wait('esc')
save_key_stats(pressed_keys)

print(pressed_keys)
