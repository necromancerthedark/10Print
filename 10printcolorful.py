import pygame
import random
pygame.init()

width = 1280
height = 720
gameLoop = True
drawLine = True
xoff = 0
yoff = 0
color = 0


win = pygame.display.set_mode((width, height))

while gameLoop:
    color = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
    if drawLine:
        if (random.randint(0, 1)):
            pygame.draw.line(win, color,
                             (0+xoff, 0+yoff), (10+xoff, 10+yoff))

        else:
            pygame.draw.line(win, color,
                             (0+xoff, 10+yoff), (10+xoff, 0+yoff))

    xoff += 10
    if xoff > width:
        yoff += 10
        xoff = 0
    if yoff > height:
        drawLine = False

    pygame.display.update()
