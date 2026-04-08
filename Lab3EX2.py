import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie 2")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))

    pygame.draw.rect(win, (0, 255, 0), (200, 150, 200, 200))
    pygame.draw.polygon(win, (255, 255, 255), [(200, 350), (400, 350), (300, 250)])

    pygame.display.update()

pygame.quit()