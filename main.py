import random as rd
import sys
from fonctions import *

pygame.init()
size = 500, 500
taille = int(input("Grid size : "))

print("--------------------")
print("Click on a square to change its color")
print("Press i to validate the grid")
print("Press r to generate a random grid")
print("--------------------")
screen = pygame.display.set_mode(size)

grille = Grille(taille)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                convert(grille)
            if event.key == pygame.K_r:
                for i in range(taille):
                    for j in range(taille):
                        grille.tab[i][j] = 1 if rd.random() >= 0.5 else 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x //= 500//taille
            y //= 500//taille
            grille.tab[y][x] = 0 if grille.tab[y][x] == 1 else 1

    for i in range(taille):
        for j in range(taille):
            if grille.tab[j][i] == 1:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(i*500/taille, j*500/taille, 500/taille, 500/taille))
            else:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i*500/taille, j*500/taille, 500/taille, 500/taille))

    for i in range(taille):
        pygame.draw.line(screen, (0, 0, 0), (500/taille*i, 0), (500/taille*i, 500))
        pygame.draw.line(screen, (0, 0, 0), (0, 500 / taille * i), (500, 500 / taille * i))


    pygame.display.flip()


