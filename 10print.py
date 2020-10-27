import pygame
import random
pygame.init()

width = 1280
height = 720
gameLoop = True
drawLine = True
xoff = 0
yoff = 0
white = (255, 255, 255)


win = pygame.display.set_mode((width, height))

while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
    if drawLine:
        if (random.randint(0, 1)):
            pygame.draw.line(win, white,
                             (0+xoff, 0+yoff), (10+xoff, 10+yoff))

        else:
            pygame.draw.line(win, white,
                             (0+xoff, 10+yoff), (10+xoff, 0+yoff))

    xoff += 10
    if xoff > width:
        yoff += 10
        xoff = 0
    if yoff > height:
        drawLine = False

    pygame.display.update()
