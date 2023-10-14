import pygame


WIDHT = 1300
HEIGHT = 700

SIZE = (WIDHT, HEIGHT)

FPS = 60

window = pygame.display.set_mode(SIZE)
backround_color = (0, 255, 0)
window.fill(backround_color)
clock = pygame.time.Clock()


game = True 
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False 


    pygame.display.update()
    clock.tick(FPS)


