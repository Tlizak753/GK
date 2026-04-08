import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie 1")

wielokat_surf = pygame.Surface((300, 300), pygame.SRCALPHA)
punkty = []
for i in range(14):
    kat = i * (2 * math.pi / 14)
    x = 150 + 150 * math.cos(kat)
    y = 150 + 150 * math.sin(kat)
    punkty.append((x, y))

pygame.draw.polygon(wielokat_surf, (255, 255, 0), punkty)
pygame.draw.polygon(wielokat_surf, (0, 0, 0), punkty, 3)

run = True
tryb = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if pygame.K_0 <= event.key <= pygame.K_9:
                tryb = event.key - pygame.K_0

    win.fill((255, 255, 255))
    surf = wielokat_surf
    x, y = 150, 150

    if tryb == 1:
        surf = pygame.transform.scale(wielokat_surf, (150, 150))
        x, y = 225, 225
    elif tryb == 2:
        surf = pygame.transform.rotozoom(wielokat_surf, 45, 1)
    elif tryb == 3:
        surf = pygame.transform.scale(pygame.transform.flip(wielokat_surf, False, True), (200, 200))
        x, y = 200, 200
    elif tryb == 4:
        surf = pygame.transform.scale(wielokat_surf, (300, 100))
        x, y = 150, 250
    elif tryb == 5:
        surf = pygame.transform.scale(wielokat_surf, (300, 50))
        x, y = 150, 0
    elif tryb == 6:
        surf = pygame.transform.scale(wielokat_surf, (100, 300))
        x, y = 250, 150
    elif tryb == 7:
        surf = pygame.transform.scale(pygame.transform.flip(wielokat_surf, True, True), (150, 150))
        x, y = 225, 225
    elif tryb == 8:
        surf = pygame.transform.rotozoom(wielokat_surf, -45, 0.5)
        x, y = 100, 400
    elif tryb == 9:
        surf = pygame.transform.flip(wielokat_surf, True, False)

    win.blit(surf, (x, y))
    pygame.display.update()

pygame.quit()