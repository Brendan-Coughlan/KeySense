import pygame
from pygame import Color, Rect

all_keys = [
    '`', '1', '2', '3', '4', '5', '6', '7', '8', '9',        # Row 1
    '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u',        # Row 2
    'i', 'o', 'p', '[', ']', '\\', 'a', 's', 'd', 'f',       # Row 3
    'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c'
]
x = {1: 2, 3: 5, 9: 8}

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
my_font = pygame.font.SysFont('Arial', 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    index = 0
    for j in range(4):
        for i in range(10):
            box_rect = Rect((150 + i * 50)+(j*50), j*50+50, 45, 45)
            if i in x:
                rect_color = (255 - (int((x[i]/sum(x.values()))* 255)), 0, 0)
            else:
                rect_color = (255, 255, 255)
            pygame.draw.rect(screen, rect_color, box_rect)

            text_surface = my_font.render(all_keys[index], True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=box_rect.center)

            screen.blit(text_surface, text_rect)
            index += 1

    pygame.display.flip()    

pygame.quit()