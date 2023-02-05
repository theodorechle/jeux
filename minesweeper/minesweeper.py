import random
import time
from kandinsky import *
from ion import *


def test_nb_bombes(x,y,tab):
  nb=0
  for i in range(-1,2,2):
    if 0<=y+i<len(tab) and tab[y+i][x][0]==9:nb+=1
    if 0<=x+i<len(tab[y]) and tab[y][x+i][0]==9:nb+=1
    if 0<=y+i<len(tab) and 0<=x+i<len(tab[y]) and tab[y+i][x+i][0]==9:nb+=1
    if 0<=y-i<len(tab) and 0<=x+i<len(tab[y]) and tab[y-i][x+i][0]==9:nb+=1
  return nb

def couleur(case,j,i):
  texte=""
  if case[1]==1 and 0<case[0]<9:texte=str(case[0])
  dessiner_cases(couleurs[9 if case==(9,1) else case[1]],j,i)
  draw_string(texte,(j)*(taille_case+1),i*(taille_case+1)+22,(0,0,0),couleurs[case[1]])

def compare(tab):
  for i in range(len(tab)):
    for j in range(len(tab[i])):
      case=tab[i][j]
      couleur(case,j,i)

def dessiner_cases(coul,x,y):
  fill_rect(x*(taille_case+1),y*(taille_case+1)+22,taille_case,taille_case,coul)

def dessiner_pointeur(x,y,c):
  #h,b,g,d
  for i in range(taille_case):
    set_pixel(x*(taille_case+1)+i,y*(taille_case+1)+22,c)
  for i in range(taille_case):
    set_pixel(x*(taille_case+1)+i,y*(taille_case+1)+21+taille_case,c)
  for i in range(taille_case):
    set_pixel(x*(taille_case+1),y*(taille_case+1)+i+22,c)
  for i in range(taille_case):
    set_pixel(x*(taille_case+1)-1+taille_case,y*(taille_case+1)+22+i,c)

def genere(tab):
  coor=[]
  for i in range(hauteur):
    for j in range(longueur):
      coor.append((j,i))
  
  for i in range(-1,2):
    for j in range(-1,2):
      if (x_pointeur+j,y_pointeur+i) in coor:
        coor.remove((x_pointeur+j,y_pointeur+i))

  for i in range(nb_bombes):
    v=random.choice(coor)
    x,y=v
    coor.remove((x,y))
    tab[y][x]=(9,0)

  coor=None
  for i in range(len(tab)):
    for j in range(len(tab[i])):
      if tab[i][j][0]!=9:
        tab[i][j]=(test_nb_bombes(j,i,tab),0)
  return tab

def affiche_sup(tab,x,y):
  if tab[y][x][0]==0:
    for i in range(-1,2):
      for j in range(-1,2):
        if 0<=y+i<len(tab) and 0<=x+j<len(tab[0]) and tab[y+i][x+j][1]==0:
          tab[y+i][x+j]=(tab[y+i][x+j][0],1)
          couleur(tab[y+i][x+j],x+j,y+i)
          tab=affiche_sup(tab,x+j,y+i)
  return tab

taille_case=19

couleurs={0:(200,200,200),1:(230,230,230),2:(255,150,150),9:(220,0,0)}

nb_bombes=30
bombes_reste=nb_bombes
longueur=16
hauteur=10

tab=[0]*hauteur
for i in range(len(tab)):
  tab[i]=[(0,0)]*longueur

compteur1=time.monotonic()
compteur2=time.monotonic()

x_pointeur=5
y_pointeur=5
premier_coup=True
#0,1,2,3,4,5,6,7,8,9=bombe
#0=vide,1=touche,2=drapeau
continuer=True
compare(tab)
dessiner_pointeur(x_pointeur,y_pointeur,(0,0,0))
while continuer:
  if keydown(KEY_LEFT) and x_pointeur-1>=0 and compteur1<time.monotonic():
    couleur(tab[y_pointeur][x_pointeur],x_pointeur,y_pointeur)
    x_pointeur-=1
    dessiner_pointeur(x_pointeur,y_pointeur,(0,0,0))
    compteur1=time.monotonic()+0.2
  elif keydown(KEY_UP) and y_pointeur-1>=0 and compteur1<time.monotonic():
    couleur(tab[y_pointeur][x_pointeur],x_pointeur,y_pointeur)
    y_pointeur-=1
    dessiner_pointeur(x_pointeur,y_pointeur,(0,0,0))
    compteur1=time.monotonic()+0.2
  elif keydown(KEY_DOWN) and y_pointeur+1<hauteur and compteur1<time.monotonic():
    couleur(tab[y_pointeur][x_pointeur],x_pointeur,y_pointeur)
    y_pointeur+=1
    dessiner_pointeur(x_pointeur,y_pointeur,(0,0,0))
    compteur1=time.monotonic()+0.2
  elif keydown(KEY_RIGHT) and x_pointeur+1<longueur and compteur1<time.monotonic():
    couleur(tab[y_pointeur][x_pointeur],x_pointeur,y_pointeur)
    x_pointeur+=1
    dessiner_pointeur(x_pointeur,y_pointeur,(0,0,0))
    compteur1=time.monotonic()+0.2
  elif keydown(KEY_TOOLBOX):
    if premier_coup:
      tab=genere(tab)
      premier_coup=False
    tab[y_pointeur][x_pointeur]=(tab[y_pointeur][x_pointeur][0],1)
    tab=affiche_sup(tab,x_pointeur,y_pointeur)
    couleur(tab[y_pointeur][x_pointeur],x_pointeur,y_pointeur)
    dessiner_pointeur(x_pointeur,y_pointeur,(0,0,0))
    if tab[y_pointeur][x_pointeur][0]==9:
      continuer=False
      draw_string("PERDU",125,0)
  elif keydown(KEY_BACKSPACE) and compteur2<time.monotonic():
    if tab[y_pointeur][x_pointeur][1]==0:
      tab[y_pointeur][x_pointeur]=(tab[y_pointeur][x_pointeur][0],2)
      if tab[y_pointeur][x_pointeur][0]==9:bombes_reste-=1
      couleur(tab[y_pointeur][x_pointeur],x_pointeur,y_pointeur)
      dessiner_pointeur(x_pointeur,y_pointeur,(0,0,0))
    elif tab[y_pointeur][x_pointeur][1]==2:
      tab[y_pointeur][x_pointeur]=(tab[y_pointeur][x_pointeur][0],0)
      if tab[y_pointeur][x_pointeur][0]==9:bombes_reste+=1
      couleur(tab[y_pointeur][x_pointeur],x_pointeur,y_pointeur)
      dessiner_pointeur(x_pointeur,y_pointeur,(0,0,0))
    compteur2=time.monotonic()+0.2
  if bombes_reste==0:
    continuer=False
    draw_string("GAGNE",125,0)

for i in range(len(tab)):
  for j in range(len(tab[i])):
     if tab[i][j][0]==9: tab[i][j]=(tab[i][j][0],1)
compare(tab)
