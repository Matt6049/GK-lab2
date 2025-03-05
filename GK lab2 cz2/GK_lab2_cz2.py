import pygame
import math

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zad2")
run = True


topleft1 = (0, 0)
topleft2 = (300, 0)
topleft3 = (0, 300)
topleft4 = (300, 300)
win.fill((255, 255, 255))

#figura 1
pygame.draw.circle(win, (0,0,0), (topleft1[0]+150, topleft1[1]+150), 100)
pygame.draw.rect(win, (255, 255, 0), pygame.Rect((topleft1[0]+100, topleft1[1]+100), (100, 100)))

#figura 2
greenSquare = pygame.draw.rect(win, (0, 255, 0), pygame.Rect((topleft2[0]+50, topleft2[1]+50),(200, 200)))
pygame.draw.polygon(win, (255,255,255), (greenSquare.bottomleft, greenSquare.bottomright, greenSquare.center))

#figura 3
triangleWidth = 75
triangleHeight = 75
blueRect = pygame.draw.rect(win, (0,0,255), pygame.Rect((topleft3[0]+80, topleft3[1]+120),(triangleWidth*2, triangleHeight)))

xLeft = blueRect.centerx-triangleWidth/2
xRight = xLeft+triangleWidth
yBottom = blueRect.bottom+triangleHeight
yTop = blueRect.top-triangleHeight

pygame.draw.polygon(win, (0,0,255), (blueRect.midbottom, (xLeft, yBottom), (xRight, yBottom)))
pygame.draw.polygon(win, (0,0,255), (blueRect.midtop, (xLeft, yTop), (xRight, yTop)))

#figura 4
pygame.draw.lines(win, (255, 0, 0), False, ((topleft4[0]+50, topleft4[1]+50), (topleft4[0]+250, topleft4[1]+50), (topleft4[0]+50, topleft4[1]+250), (topleft4[0]+250, topleft4[1]+250)), 10)
pygame.display.update()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
