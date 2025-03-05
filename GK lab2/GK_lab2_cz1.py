import math
import pygame
#wniosek: pygame wykorzystuje kąty w stopniach zamiast radianach, co wymaga konwersji, i nie ma funkcji skew
def skew(surface, scale, rotation): 
    rRadians = math.radians(rotation)
    surface = pygame.transform.rotate(surface, rotation)
    surface = pygame.transform.scale(surface, (surface.get_width()*scale[0], surface.get_height()*scale[1]))

    newCos = scale[0]*math.cos(rRadians)
    newSin = scale[1]*math.sin(rRadians)
    newAngle = math.degrees(math.atan2(newSin, newCos))
    return pygame.transform.rotate(surface, -newAngle)


def createPolygonSurf(surf, points):

    surf.fill((255, 255, 0))
    polygon = pygame.draw.polygon(surf, (255, 0, 0), points)
    pygame.draw.line(surf, (0, 0, 0), (polygon.centerx, polygon.centery), (polygon.right, polygon.centery), 2) #oś x
    pygame.draw.line(surf, (255, 255, 255), (polygon.centerx, polygon.centery), (polygon.centerx, polygon.top), 2) #oś y
    return surf


def createPolygon(sides, radius):
    polygonPoints = []
    i = 0
    while i<sides:
        x = radius+math.cos(2*math.pi*i/sides)*radius
        y = radius+math.sin(2*math.pi*i/sides)*radius
        polygonPoints.append(pygame.math.Vector2(x, y))
        i += 1
    return polygonPoints

def findPolygonBounds(points):
    rightX = points[0].x
    leftX = rightX
    topY = points[0].y
    bottomY = topY
    for point in points:
        if(point.x < leftX):
            leftX = point.x
        if(point.y < topY):
            topY = point.y
        if(point.y > bottomY):
            bottomY = point.y
        print(point)
    return (leftX, rightX, topY, bottomY)

def scrollPolygon(points, leftX, topY):
    for point in points:
        point.x -= leftX
        point.y -= topY
    return points

#stworzenie okna
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zad1")
run = True

#przygotowania, oraz rysunek początkowy
allowedModes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
mode = '0'
radius = 150
sides = 6
origin = pygame.math.Vector2(300, 300)
win.fill((255, 255, 0))
polygonPoints = createPolygon(sides, radius)
polygonBounds = findPolygonBounds(polygonPoints)
surf = pygame.Surface((polygonBounds[1]-polygonBounds[0], polygonBounds[3]-polygonBounds[2]))
surf = createPolygonSurf(surf, scrollPolygon(polygonPoints, polygonBounds[0], polygonBounds[2]))
win.blit(surf, (origin.x-surf.get_width()/2, origin.y-surf.get_height()/2))
pygame.display.update()

#wniosek: python sprawdza wszystkie predykaty w bloku if jednocześnie, zamiast kończyć na jednym

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode in allowedModes: 
                mode = event.unicode
                origin = pygame.math.Vector2(300, 300)
                win.fill((255, 255, 0))
                surf = pygame.Surface((300, 300))
                surf = createPolygonSurf(surf, polygonPoints)

                if(mode == '1'):
                    surf = pygame.transform.scale_by(surf, 0.5)
                elif(mode == '2'):
                    surf = pygame.transform.rotate(surf, -45)
                elif(mode == '3'):
                    surf = pygame.transform.flip(surf, 1, 1)
                    surf = pygame.transform.scale(surf, (0.5*surf.get_width(), surf.get_height()))
                elif(mode == '4'):
                    surf = skew(surf, (2, 1), 45)
                elif(mode == '5'):
                    surf = pygame.transform.scale(surf, (1*surf.get_width(), 0.5*surf.get_height()))
                    origin.y = surf.get_height()/2
                elif(mode == '6'):
                    surf = skew(surf, (2, 1), 45)
                    surf = pygame.transform.rotate(surf, -90)
                elif(mode == '7'):
                    surf = pygame.transform.flip(surf, 0, 1)
                    surf = pygame.transform.scale(surf, (0.5*surf.get_width(), surf.get_height()))
                elif(mode == '8'):
                    origin.x -= 50
                    origin.y += 100
                    surf = pygame.transform.scale(surf, (surf.get_width()*1.5, surf.get_height()*0.5))
                    surf = pygame.transform.rotate(surf, -30)
                elif(mode == '9'):
                    surf = skew(surf, (1, 2), 45) 
                    surf = pygame.transform.flip(surf, 0, 1)
                    origin.x += 61
        
                win.blit(surf, (origin.x-surf.get_width()/2, origin.y-surf.get_height()/2))
                pygame.display.update()

#Wniosek: nie chcę już pracować z tą biblioteką, chcę wrócić do godota albo nawet canvasa, jest przestarzala
