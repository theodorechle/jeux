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


vieux_mystery = [[5, 6, 7, 8, 9, 10],
                [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                [2, 3, 4, 7, 8, 11, 12, 13],
                [3, 12]
                ]

mystery_ship = [-5, 6, 0, -3, 10, 0, -2, 12, 0, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, 0, 16, 0, -2, 3, -2, 2, -2, 3, 0, -3, 1, -8, 1]

perso = [
    [-5, 1, 0, -4, 3, 0, -4, 3, 0, -4, 3, 0, -1, 9, 0, 11, 0, 11, 0, 11, 0, 11],
    [-4, 1, 0, 0, -4, 1, -1, 1, -1, 1, 0, -4, 1, 0, -2, 1, -2, 2, -1, 2, 0, 1, -2, 1, -1, 2, -1, 1, 0, -2, 7, -1, 1, 0, 1, 9, -1, 1, -1, 1]
]

vieux_perso = [[[5],
          [4, 5, 6],
          [4, 5, 6],
          [4, 5, 6],
          [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
          ],
         [[4],
          [],
          [4, 6, 8],
          [4],
          [2, 5, 6, 8, 9],
          [0, 3, 5, 6, 8],
          [2, 3, 4, 5, 6, 7, 8, 10],
          [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13]
          ]
         ]

missiles = [
    [-2, 1, 0, -1, 1, 0, 1, 0, -1, 1, 0, -2, 1, 0, -1, 1, 0, 1],
    [1, 0, 1, 0, 1]
]

vieux_missiles = [[[2],
             [1],
             [0],
             [1],
             [2],
             [1],
             [0]
             ],
            [[0],
             [0],
             [0]
             ]
            ]

explosion = [-4, 1, -3, 1, 0, -1, 1, -3, 1, -1, 1, -3, 1, 0, -2, 1, -7, 1, 0, -3, 1, -5, 1, 0, 2, -9, 2, 0, -3, 1, -5, 1, 0, -2, 1, -2, 1, -1, 1, -2, 1, 0, -1, 1, -2, 1, -3, 1, -2, 1]

vieille_explosion = [[4, 8],
             [1, 5, 7, 11],
             [2, 10],
             [3, 9],
             [0, 1, 11, 12],
             [3, 9],
             [2, 5, 7, 10],
             [1, 4, 8, 11]
             ]

bouclier = [-4, 12, 0, -3, 14, 0, -2, 16, 0, -1, 18, 0, 20, 0, 20, 0, 20, 0, 20, 0, 20, 0, 20, 0, 8, -4, 8, 0, 7, -6, 7, 0, 6, -8, 6, 0, 5, -10, 5, 0, 5, -10, 5]

vieux_bouclier = [[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            [0, 1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19],
            [0, 1, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17, 18, 19],
            [0, 1, 2, 3, 4, 5, 14, 15, 16, 17, 18, 19],
            [0, 1, 2, 3, 4, 15, 16, 17, 18, 19],
            [0, 1, 2, 3, 4, 15, 16, 17, 18, 19]
            ]


grille_monstres = [
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"]
]

aliens = [
    [-4, 4, 0, -1, 10, 0, 12, 0, 3, -2, 2, -2, 3, 0, 12, 0, -3, 2, -2, 2, 0, -2, 1, -2, 2, -2, 1, 0, -3, 1, -4, 1],
    [-2, 1, -5, 1, 0, -3, 1, -3, 1, 0, -2, 7, 0, -1, 2, -1, 3, -1, 2, 0, 11, 0, 1, -1, 7, -1, 1, 0, 1, -1, 1, -5, 1, -1, 1, 0, -3, 2, -1, 2],
    []
]

aliens2 = [
    [-4, 4, 0, -1, 10, 0, 12, 0, 3, -2, 2, -2, 3, 0, 12, 0, -3, 2, -2, 2, 0, -2, 2, -1, 2, -1, 2, 0, 2, -8, 2],
    [-2, 1, -5, 1, 0, 1, -2, 1, -3, 1, -2, 1, 0, 1, -1, 7, -1, 1, 0, 3, -1, 3, -1, 3, 0, 11, 0, -1, 9, 0, -2, 1, -5, 1, 0, -1, 1, -7, 1],
    []
]

vieilles_correspondances_monstres = {
    "monstre1": [[[4, 5, 6, 7],
                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                  [0, 1, 2, 5, 6, 9, 10, 11],
                  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                  [3, 4, 7, 8],
                  [2, 5, 6, 9],
                  [3, 8]
                  ],
                 [[4, 5, 6, 7],
                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                  [0, 1, 2, 5, 6, 9, 10, 11],
                  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                  [3, 4, 7, 8],
                  [2, 3, 5, 6, 8, 9],
                  [0, 1, 10, 11]
                  ]
                 ],
    "monstre2": [[[2, 8],
                  [3, 7],
                  [2, 3, 4, 5, 6, 7, 8],
                  [1, 2, 4, 5, 6, 8, 9],
                  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                  [0, 2, 3, 4, 5, 6, 7, 8, 10],
                  [0, 2, 8, 10],
                  [3, 4, 6, 7]
                  ],
                 [[2, 8],
                  [0, 3, 7, 10],
                  [0, 2, 3, 4, 5, 6, 7, 8, 10],
                  [0, 1, 2, 4, 5, 6, 8, 9, 10],
                  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
                  [2, 8],
                  [1, 9]
                  ]
                 ],
    "monstre3": [[[3, 4, 5],
                  [2, 3, 4, 5, 6],
                  [1, 2, 3, 4, 5, 6, 7],
                  [0, 1, 4, 7, 8],
                  [0, 1, 2, 3, 4, 5, 6, 7, 8],
                  [2, 6],
                  [1, 3, 4, 5, 7],
                  [0, 2, 6, 8]
                  ],
                 [[3, 4, 5],
                  [2, 3, 4, 5, 6],
                  [1, 2, 3, 4, 5, 6, 7],
                  [0, 1, 4, 7, 8],
                  [0, 1, 2, 3, 4, 5, 6, 7, 8],
                  [2, 6],
                  [1, 7],
                  [2, 6]
                  ]
                 ]
}

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
    dessiner(vieux_mystery, (5, 5))
    dessiner_test(mystery_ship, (5, 50))
    dessiner(vieux_perso[0], (50, 5))
    dessiner_test(perso[0], (50, 50))
    dessiner(vieux_perso[1], (100, 5))
    dessiner_test(perso[1], (100, 50))
    dessiner(vieux_missiles[0], (150, 5))
    dessiner_test(missiles[0], (150, 50))
    dessiner(vieux_missiles[1], (200, 5))
    dessiner_test(missiles[1], (200, 50))
    dessiner(vieille_explosion, (250, 5))
    dessiner_test(explosion, (250, 50))
    dessiner(vieilles_correspondances_monstres["monstre1"][0], (5, 100))
    dessiner_test(aliens[0], (5, 150))
    dessiner(vieilles_correspondances_monstres["monstre1"][1], (50, 100))
    dessiner_test(aliens2[0], (50, 150))
    dessiner(vieilles_correspondances_monstres["monstre2"][0], (100, 100))
    dessiner_test(aliens[1], (100, 150))
    dessiner(vieilles_correspondances_monstres["monstre2"][1], (150, 100))
    dessiner_test(aliens2[1], (150, 150))
    dessiner(vieilles_correspondances_monstres["monstre3"][0], (200, 100))
    dessiner_test(aliens[2], (200, 150))
    dessiner(vieilles_correspondances_monstres["monstre3"][1], (250, 100))
    dessiner_test(aliens2[2], (250, 150))
    dessiner(vieux_bouclier, (5, 180))
    dessiner_test(bouclier, (50, 180))
