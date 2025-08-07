import json
import keyboard
import datetime
import pygame
from pygame import Rect


def on_key_event(event):
    if event.name in key_stats:
        key_stats[event.name] += 1
    else:
        key_stats[event.name] = 1
    with open("keylog.txt", "a") as f:
        timestamp = datetime.datetime.now()
        f.write(f"<{timestamp}> {event.name}\n")
        print(f"<{timestamp}> {event.name}")


def save_key_stats(stats, filename="keystats.json"):
    with open(filename, "w") as f:
        json.dump(stats, f)


def load_key_stats(filename="keystats.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


all_keys = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "q",
    "w",
    "e",
    "r",
    "t",
    "y",
    "u",
    "i",
    "o",
    "p",
    "a",
    "s",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    ";",
    "z",
    "x",
    "c",
    "v",
    "b",
    "n",
    "m",
    ",",
    ".",
    "/",
]
padding = 5
box_size = 45

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
my_font = pygame.font.SysFont("Arial", 30)

key_stats = load_key_stats()
keyboard.on_press(on_key_event)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_key_stats(key_stats)
            running = False

    screen.fill((0, 0, 0))

    total_presses = sum(key_stats.values()) or 1
    for index, key in enumerate(all_keys):
        row = index // 10
        col = index % 10

        x = 150 + col * (box_size+padding)
        y = 50 + row * (box_size+padding)
        box_rect = Rect(x, y, box_size, box_size)

        count = key_stats.get(key, 0)
        intensity = int((count / total_presses) * 255)
        rect_color = (255 - intensity, 0, 0) if count > 0 else (255, 255, 255)

        pygame.draw.rect(screen, rect_color, box_rect)
        text_surface = my_font.render(key, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=box_rect.center)
        screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()
