import pygame
import sys


class Grille:
    def __init__(self, taille):
        self.tab = [[0 for _ in range(taille)] for _ in range(taille)]

    def __str__(self):
        s = ""
        for i in self.tab:
            s += str(i)
        return s

    def row(self, i):
        return self.tab[i]

    def column(self, i):
        return [self.tab[j][i] for j in range(len(self.tab))]
    

def count(row):
    r = []
    c = 0
    for i in row:
        c += i
        if i == 0 and c != 0:
            r.append(c)
            c = 0
    if c != 0:
        r.append(c)
    return r
    
def convert(grille):
    taille = len(grille.tab)
    sysfont = pygame.font.get_default_font()
    font = pygame.font.SysFont(None, int(500//taille*1.7))

    rows = [count(grille.row(i)) for i in range(taille)]
    columns = [count(grille.column(i)) for i in range(taille)]


    width_plus = max([len(i) for i in rows])
    width = 500 + width_plus * (500//taille)
    height_plus = max([len(i) for i in columns])
    height = 500 + height_plus * (500//taille)
    size = (width, height)
    screen = pygame.display.set_mode(size)
    show = 0
    
    font = pygame.font.Font(None, int(1.3*500//taille))

    print("--------------------")
    print("Press u to show/hide the black squares")
    print("Press y to save the grid (the black squares will appear on the saved image if they are currently visible on the screen.)")
    print("--------------------")

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    show = 0 if show == 1 else 1
                if event.key == pygame.K_y:
                    pygame.image.save(screen, "grid.png")

        screen.fill((255, 255, 255))

        for r in range(len(rows)):
            for i in range(len(rows[r])):
                text = font.render(str(rows[r][i]), True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (i*500/taille + 250/taille + (width_plus - len(rows[r]))*500/taille, (r*500/taille) + (height_plus*500/taille) + 250/taille)
                screen.blit(text, text_rect)
        
        for c in range(len(columns)):
            for i in range(len(columns[c])):
                text = font.render(str(columns[c][i]), True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = ((c*500/taille) + (width_plus*500/taille) + 250/taille, i*500/taille + 250/taille + (height_plus - len(columns[c]))*500/taille)
                screen.blit(text, text_rect)
        
        if show:
            for i in range(taille):
                for j in range(taille):
                    if grille.tab[j][i] == 1:
                        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((i*500/taille) + (width_plus*500/taille) - 1, (j*500/taille) + (height_plus*500/taille) - 1, 500//taille, 500//taille))

        for i in range(taille):
            if ((i-(taille%5)+1) % 5 == 0):
                pygame.draw.line(screen, (0, 0, 0), (width - (500/taille*(i+1)), 0), (width - (500/taille*(i+1)), height), 2)
                pygame.draw.line(screen, (0, 0, 0), (0, height - (500/taille*(i+1))), (width, height - (500/taille*(i+1))), 2)
            else:
                pygame.draw.line(screen, (0, 0, 0), (width - (500/taille*(i+1)), 0), (width - (500/taille*(i+1)), height))
                pygame.draw.line(screen, (0, 0, 0), (0, height - (500/taille*(i+1))), (width, height - (500/taille*(i+1))))

        pygame.display.flip()
