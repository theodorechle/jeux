from kandinsky import fill_rect
from time import monotonic
from ion import keydown, KEY_OK, KEY_LEFT, KEY_RIGHT
from random import random, randint

# consts
WHITE = "#ffffff"
GREEN = "#32ff32"

def dessiner(image, coord):
    for i in range(len(image)):
        for j in image[i]:
            if coord[1]+i*taille_case >= 180:
                couleur = (50, 255, 50)
            else:
                couleur = (255, 255, 255)
            fill_rect(coord[0]+j*taille_case, coord[1]+i*taille_case, taille_case, taille_case, couleur)

def dessiner_test(image, coord):
    x, y = 0, 0
    for nb in image:
        if nb == 0:
            y += 1
            x = 0
        elif nb < 0:
            x -= nb
        else:
            if coord[1]+y*taille_case >= 180:
                couleur = (50, 255, 50)
            else:
                couleur = (255, 255, 255)
            fill_rect(coord[0]+x*taille_case, coord[1]+y*taille_case, taille_case * nb, taille_case, couleur)
            x += nb


def collision(h2, h1):
    if (h1[0] <= h2[0] <= h1[0]+h1[2] and h1[1] <= h2[1] <= h1[1]+h1[3]) or (h1[0] <= h2[0]+h2[2] <= h1[0]+h1[2] and h1[1] <= h2[1]+h2[3] <= h1[1]+h1[3]):
        return True


taille_case = 2


mystery_ship = [-5, 6, 0, -3, 10, 0, -2, 12, 0, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, 0, 16, 0, -2, 3, -2, 2, -2, 3, 0, -3, 1, -8, 1]

perso = [
    [-5, 1, 0, -4, 3, 0, -4, 3, 0, -4, 3, 0, -1, 9, 0, 11, 0, 11, 0, 11, 0, 11],
    [-4, 1, 0, 0, -4, 1, -1, 1, -1, 1, 0, -4, 1, 0, -2, 1, -2, 2, -1, 2, 0, 1, -2, 1, -1, 2, -1, 1, 0, -2, 7, -1, 1, 0, 1, 9, -1, 1, -1, 1]
]

bullets = [
    [-2, 1, 0, -1, 1, 0, 1, 0, -1, 1, 0, -2, 1, 0, -1, 1, 0, 1],
    [1, 0, 1, 0, 1]
]

explosion = [-4, 1, -3, 1, 0, -1, 1, -3, 1, -1, 1, -3, 1, 0, -2, 1, -7, 1, 0, -3, 1, -5, 1, 0, 2, -9, 2, 0, -3, 1, -5, 1, 0, -2, 1, -2, 1, -1, 1, -2, 1, 0, -1, 1, -2, 1, -3, 1, -2, 1]

shield = [-4, 12, 0, -3, 14, 0, -2, 16, 0, -1, 18, 0, 20, 0, 20, 0, 20, 0, 20, 0, 20, 0, 20, 0, 8, -4, 8, 0, 7, -6, 7, 0, 6, -8, 6, 0, 5, -10, 5, 0, 5, -10, 5]

grille_monstres = [
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"]
]

aliens = [
    [
        [-4, 4, 0, -1, 10, 0, 12, 0, 3, -2, 2, -2, 3, 0, 12, 0, -3, 2, -2, 2, 0, -2, 1, -2, 2, -2, 1, 0, -3, 1, -4, 1],
        [-2, 1, -5, 1, 0, -3, 1, -3, 1, 0, -2, 7, 0, -1, 2, -1, 3, -1, 2, 0, 11, 0, 1, -1, 7, -1, 1, 0, 1, -1, 1, -5, 1, -1, 1, 0, -3, 2, -1, 2],
        [-3, 3, 0, -2, 5, 0, -1, 7, 0, 2, -2, 1, -2, 2, 0, 9, 0, -2, 1, -3, 1, 0, -1, 1, -1, 3, -1, 1, 0, 1, -1, 1, -3, 1, -1, 1]
    ],
    [
        [-4, 4, 0, -1, 10, 0, 12, 0, 3, -2, 2, -2, 3, 0, 12, 0, -3, 2, -2, 2, 0, -2, 2, -1, 2, -1, 2, 0, 2, -8, 2],
        [-2, 1, -5, 1, 0, 1, -2, 1, -3, 1, -2, 1, 0, 1, -1, 7, -1, 1, 0, 3, -1, 3, -1, 3, 0, 11, 0, -1, 9, 0, -2, 1, -5, 1, 0, -1, 1, -7, 1],
        [-3, 3, 0, -2, 5, 0, -1, 7, 0, 2, -2, 1, -2, 2, 0, 9, 0, -2, 1, -3, 1, 0, -1, 1, -5, 1, 0, -2, 1, -3, 1]
    ]
]

tailles = {
    "mystery_ship": (16, 7),
    "perso0": (11, 9),
    "perso1": (14, 8),
    "missiles0": (3, 7),
    "missiles1": (1, 3),
    "explosion": (13, 8),
    "bouclier": (20, 15),
    "monstre1": (12, 8),
    "monstre2": (11, 8),
    "monstre3": (9, 8)
}


print("""
Attention !
Il faut gérer les boucliers de manière à ce que les missiles puissent passer après les avoir détruits.
Peut-être faudra-t-il également réécrire le code en anglais.
""")

fill_rect(0, 0, 320, 222, (0, 0, 0))

while 1:
    dessiner_test(mystery_ship, (5, 50))
    dessiner_test(perso[0], (50, 50))
    dessiner_test(perso[1], (100, 50))
    dessiner_test(bullets[0], (150, 50))
    dessiner_test(bullets[1], (200, 50))
    dessiner_test(explosion, (250, 50))
    dessiner_test(aliens[0][0], (5, 150))
    dessiner_test(aliens[1][0], (50, 150))
    dessiner_test(aliens[0][1], (100, 150))
    dessiner_test(aliens[1][1], (150, 150))
    dessiner_test(aliens[0][2], (200, 150))
    dessiner_test(aliens[1][2], (250, 150))
    dessiner_test(shield, (50, 180))
