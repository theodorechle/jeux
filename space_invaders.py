# -*- coding: utf-8 -*-
from kandinsky import fill_rect
from time import monotonic
from ion import keydown, KEY_OK, KEY_LEFT, KEY_RIGHT
from random import choice, random


def dessiner(image, coord):
    for i in range(len(image)):
        for j in image[i]:
            if coord[1]+i*taille_case >= 180:
                couleur = (50, 255, 50)
            else:
                couleur = (255, 255, 255)
            fill_rect(coord[0]+j*taille_case, coord[1]+i*taille_case, taille_case, taille_case, couleur)


def collision(h2, h1):
    if (h1[0] <= h2[0] <= h1[0]+h1[2] and h1[1] <= h2[1] <= h1[1]+h1[3]) or (h1[0] <= h2[0]+h2[2] <= h1[0]+h1[2] and h1[1] <= h2[1]+h2[3] <= h1[1]+h1[3]):
        return True


taille_case = 2


mystery_ship = [[5, 6, 7, 8, 9, 10, 11],
                [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                [2, 3, 4, 7, 8, 11, 12, 13],
                [3, 12]
                ]


perso = [[[5],
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

missiles = [[[2],
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

explosion = [[4, 8],
             [1, 5, 7, 11],
             [2, 10],
             [3, 9],
             [0, 1, 11, 12],
             [3, 9],
             [2, 5, 7, 10],
             [1, 4, 8, 11]
             ]


bouclier = [[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
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


monstres = [
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"],
    ["monstre1", "monstre1", "monstre2", "monstre2", "monstre3", "monstre3"]
]


correspondance_monstres = {
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

coords_base = [30, 30]
coords = coords_base
coords_missile = coords_missile_ennemis = []
coords_mystery_ship = [0, 10, tailles["mystery_ship"][0], tailles["mystery_ship"][1]]
coords_perso = [159, 200]
dist = (40, 22)
score = 0
nouv_coords_perso = 160
nouv_coords = coords
fill_rect(0, 0, 320, 222, (0, 0, 0))

combo = 0
ajout = (5, 5)
coord_explos = {}
perso_explos = 0
nb = False
sens = 1

t_ennemis = monotonic()-0.7
t_missile = monotonic()-0.1
t_perso = monotonic()-0.1
t_tirer = monotonic()-0.7
t_mystery_ship = monotonic()+int(random()*100)

continuer = True

while continuer:
    if t_ennemis+0.7 <= monotonic():
        if 5 < coords[0]+sens*ajout[0] < coords_base[1]+55:
            nouv_coords = coords[0]+ajout[0]*sens, coords[1]
        else:
            sens = -sens
            nouv_coords = coords[0], coords[1]+ajout[1]
        for i in range(len(monstres)):
            for j in range(len(monstres[i])-1, -1, -1):

                if monstres[i][j] != "":
                    if monstres[i][j] == "explosion":
                        x, y = coord_explos[str(i)+str(j)]
                        fill_rect(x+dist[0]*i, y+dist[1]*j, 25, 25, (0, 0, 0))
                        dessiner(explosion, (x+dist[0]*i, y+dist[1]*j))
                        monstres[i][j] = "explosion2"
                    elif monstres[i][j] == "explosion2":
                        monstres[i][j] = ""
                        x, y = coord_explos[str(i)+str(j)]
                        fill_rect(x+dist[0]*i, y+dist[1]*j, 27, 17, (0, 0, 0))
                    else:
                        image = str(monstres[i][j])
                        fill_rect(coords[0]+dist[0]*i, coords[1]+dist[1]*j, tailles[image][0]*taille_case, tailles[image][1]*taille_case, (0, 0, 0))
                        dessiner(correspondance_monstres[image][nb], (nouv_coords[0]+dist[0]*i, nouv_coords[1]+dist[1]*j))
                        if j < len(monstres[i])-1 and monstres[i][j+1] in "explosion2" and random() < 0.1:
                            coords_missile_ennemis.append([nouv_coords[0]+dist[0]*i+(tailles[image][0]//2-tailles["missiles0"][0]//2)*taille_case, nouv_coords[1]+dist[1]*j+tailles[image][1]*taille_case+3, tailles["missiles0"][0]*taille_case, tailles["missiles0"][1]*taille_case])
                            dessiner(missiles[0], coords_missile_ennemis[-1])

        nb = not nb
        coords = nouv_coords
        t_ennemis = monotonic()

    if t_missile+0.1 <= monotonic():
        coords_suppr = []
        for indice, i in enumerate(coords_missile):
            fill_rect(i[0], i[1]+5, i[2], i[3], (0, 0, 0))
            dessiner(missiles[1], i)
            coords_missile[indice][1] -= 5
            if collision(i, coords_mystery_ship):
                combo += 1
                score += 300 if (combo-23) % 15 == 0 else choice([50, 100, 150, 200])
                coords_suppr.append(i)
                fill_rect(i[0], i[1]+5, i[2], i[3], (0, 0, 0))
            elif i[1] <= 0:
                combo = 0
                coords_suppr.append(i)
                fill_rect(i[0], i[1]+5, i[2], i[3], (0, 0, 0))

            test = False
            for k in range(len(monstres)):
                for j in range(len(monstres[k])-1, -1, -1):
                    if not test and monstres[k][j] != "":
                        if "explosion" not in monstres[k][j]:
                            if collision(i, [coords[0]+dist[0]*k, coords[1]+dist[1]*j, tailles[str(monstres[k][j])][0]*taille_case, tailles[str(monstres[k][j])][1]*taille_case]):
                                combo += 1
                                score += (k//2+1)*10
                                fill_rect(i[0], i[1]+5, i[2], i[3], (0, 0, 0))
                                coords_suppr.append(i)
                                test = True
                                monstres[k][j] = "explosion"
                                coord_explos[str(k)+str(j)] = (coords[0], coords[1])
                            else:
                                coords_suppr_alien = []
                                for tir_alien in coords_missile_ennemis:
                                    if collision(i, tir_alien):
                                        coords_suppr.append(i)
                                        fill_rect(i[0], i[1]+5, i[2], i[3], (0, 0, 0))
                                        coords_suppr_alien.append(tir_alien)
                                        fill_rect(tir_alien[0], tir_alien[1], tir_alien[2], tir_alien[3], (0, 0, 0))

                                coords_missile_ennemis = [i for i in coords_missile_ennemis if i not in coords_suppr_alien]

        coords_missile = [i for i in coords_missile if i not in coords_suppr]

        for indice, i in enumerate(coords_missile_ennemis):
            fill_rect(i[0], i[1], i[2], i[3], (0, 0, 0))
            coords_missile_ennemis[indice][1] += 5
            if collision(i, [coords_perso[0], coords_perso[1], tailles["perso0"][0]*taille_case, tailles["perso0"][1]*taille_case]):
                perso_explos = 1
            else:
                dessiner(missiles[0], i)
        t_missile = monotonic()

    if t_perso+0.1 <= monotonic():
        if perso_explos == 0:
            if keydown(KEY_LEFT) and coords_perso[0] >= 10:
                nouv_coords_perso = coords_perso[0]-5
            if keydown(KEY_RIGHT) and coords_perso[0] <= 290:
                nouv_coords_perso = coords_perso[0]+5
            if nouv_coords_perso != coords_perso[0]:
                fill_rect(coords_perso[0], coords_perso[1], tailles["perso0"][0]*taille_case, tailles["perso0"][1]*taille_case, (0, 0, 0))
                coords_perso[0] = nouv_coords_perso
                dessiner(perso[0], coords_perso)
                t_perso = monotonic()
        elif perso_explos == 1:
            fill_rect(coords_perso[0], coords_perso[1], tailles["perso0"][0]*taille_case, tailles["perso0"][1]*taille_case, (0, 0, 0))
            dessiner(perso[1], coords_perso)
            perso_explos = 2
        elif perso_explos == 2:
            fill_rect(coords_perso[0], coords_perso[1], tailles["perso1"][0]*taille_case, tailles["perso1"][1]*taille_case, (0, 0, 0))
            continuer = False

    if t_tirer+0.7 <= monotonic():
        if keydown(KEY_OK):
            coords_missile.append([coords_perso[0]+5*taille_case, coords_perso[1]-6*taille_case, tailles["missiles1"][0]*taille_case, tailles["missiles1"][1]*taille_case])
            t_tirer = monotonic()

    # if t_mystery_ship <= monotonic():
    #     if coords_mystery_ship[0] is None:
    #         sens_mystery_ship = choice([-1, 1])
    #         coords_mystery_ship[0] = 0 if sens_mystery_ship == 1 else 320-tailles["mystery_ship"][0]
    #         dessiner(mystery_ship, coords_mystery_ship)
    #     else:
    #         fill_rect(coords_mystery_ship[0], coords_mystery_ship[1],tailles["mystery_ship"][0]*taille_case, tailles["mystery_ship"][1]*taille_case)
    #         coords_mystery_ship[0] += 5*sens_mystery_ship
    #         if 0 < coords_mystery_ship[0] < 320-tailles["mystery_ship"][0]:
    #             dessiner(mystery_ship, coords_mystery_ship)
    #         else:
    #             coords_mystery_ship[0] = None
    #             t_mystery_ship += int(random()*100)
