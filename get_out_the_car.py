from ion import *
from kandinsky import *
from time import *

class Voiture:
  def __init__(self,pos,taille,mouv,couleur):
    self.pos=pos
    tab[pos[1]][pos[0]]=self
    self.taille=taille
    self.mouv=mouv
    for i in range(1,taille):
      if self.mouv==1:
        tab[pos[1]+i][pos[0]]=(0,-i)
      else:
        tab[pos[1]][pos[0]+i]=(-i,0)

    self.couleur=couleur
    self.dessiner(self.couleur)
  
  def dessiner(self,couleur):
    for i in range(self.taille):
      x,y=0,0
      if self.mouv:
        y=i
      else:
        x=i
      fill_rect(int(self.pos[0]*taille_carreau+taille_carreau*x+1),int(self.pos[1]*taille_carreau+taille_carreau*y+1),taille_carreau-1,taille_carreau-1,couleur)
  
  def posx(self,x):
    if x==1 and self.pos[0]+self.taille+x-1<len(tab[0]) and tab[self.pos[1]][self.pos[0]+self.taille-1+x]==0 or x==-1 and self.pos[0]+x>=0 and tab[self.pos[1]][self.pos[0]+x]==0:
      if self.pos[0]+x>=0 and self.pos[0]+self.taille+x<=taille_ecran[0]:
        self.dessiner((255,255,255))
        self.pos[0]+=x
        self.dessiner(self.couleur)
        if x==1:
          r=range(self.taille-1,-1,-1)
        else:
          r=range(self.taille)
        for i in r:
          tab[self.pos[1]][self.pos[0]+i]=tab[self.pos[1]][self.pos[0]+i-x]
          tab[self.pos[1]][self.pos[0]+i-x]=0
          
        return True
    return False
  
  def posy(self,y):
    if y==1 and self.pos[1]+self.taille+y-1<len(tab) and tab[self.pos[1]+self.taille+y-1][self.pos[0]]==0 or y==-1 and self.pos[1]+y>=0 and tab[self.pos[1]+y][self.pos[0]]==0:
      if self.pos[1]+y>=0 and self.pos[1]+self.taille+y<=taille_ecran[1]:
        self.dessiner((255,255,255))
        self.pos[1]+=y
        self.dessiner(self.couleur)
        if y==1:
          r=range(self.taille-1,-1,-1)
        else:
          r=range(self.taille)
        for i in r:
          tab[self.pos[1]+i][self.pos[0]]=tab[self.pos[1]+i-y][self.pos[0]]
          tab[self.pos[1]+i-y][self.pos[0]]=0
        return True
    return False

def taille_case():
  return min(320//taille_ecran[0],222//taille_ecran[1])

def cadrillage():
  taille_carreau=taille_case()
  for i in range(taille_ecran[0]+1):
      fill_rect(i*taille_carreau,0,1,(taille_ecran[1])*taille_carreau,(0,0,0))
  for i in range(taille_ecran[1]+1):
      fill_rect(0,i*taille_carreau,(taille_ecran[0])*taille_carreau,1,(0,0,0))
  return taille_carreau

def perso(coords,couleur):
  fill_rect(coords[0]*taille_carreau,coords[1]*taille_carreau,1,taille_carreau,couleur)
  fill_rect((coords[0]+1)*taille_carreau,coords[1]*taille_carreau,1,taille_carreau,couleur)
  fill_rect(coords[0]*taille_carreau,coords[1]*taille_carreau,taille_carreau,1,couleur)
  fill_rect(coords[0]*taille_carreau,(coords[1]+1)*taille_carreau,taille_carreau,1,couleur)

def deplacer_perso(coords,coords_suiv):
  global pause
  pause=True
  if coords==sortie:
    case_sortie(coords)
  else:
    perso(coords,(0,0,0))
  coords[0]+=coords_suiv[0]
  coords[1]+=coords_suiv[1]
  perso(coords,(0,0,255))

def case_sortie(coords):
  couleur=(255,0,0)
  fill_rect(coords[0]*taille_carreau,coords[1]*taille_carreau,1,taille_carreau,couleur)
  fill_rect((coords[0]+1)*taille_carreau,coords[1]*taille_carreau,1,taille_carreau,couleur)
  fill_rect(coords[0]*taille_carreau,coords[1]*taille_carreau,taille_carreau,1,couleur)
  fill_rect(coords[0]*taille_carreau,(coords[1]+1)*taille_carreau,taille_carreau,1,couleur)

  
def deplacer(voiture,d):
  dv=voiture.mouv
  if d==1 and dv==1:
    return voiture.posy(-1)
  if d==3 and dv==1:
   return voiture.posy(1)
  if d==2 and dv==0:
    return voiture.posx(1)
  if d==4 and dv==0:
    return voiture.posx(-1)

#taille_ecran=(5,5)
taille_ecran=(10,10)
taille_carreau=cadrillage()

tab=[[0 for i in range(taille_ecran[0])] for i in range(taille_ecran[1])]

# j=Voiture([2,1],2,0,(255,0,0))
# Voiture([3,0],2,0,(255,127,0))
# Voiture([1,3],2,1,(255,127,0))
# Voiture([2,4],3,0,(255,255,0))
# Voiture([4,1],3,1,(0,255,0))

j=Voiture([3,0],2,0,(0,0,255))
Voiture([5,0],3,1,(255,0,0))
Voiture([4,3],2,0,(0,255,0))
Voiture([6,0],4,1,(100,50,150))
Voiture([6,5],4,1,(100,50,150))
Voiture([5,9],5,0,(250,0,0))
Voiture([2,5],5,1,(255,255,0))
Voiture([3,6],4,1,(255,127,0))
Voiture([4,6],4,1,(0,0,0))
Voiture([3,5],3,0,(253,108,158))
Voiture([4,4],3,0,(120,120,120))
Voiture([2,4],2,0,(0,0,255))
Voiture([7,4],2,1,(0,255,255))
Voiture([7,6],2,0,(255,0,0))
Voiture([9,6],3,1,(120,120,0))
Voiture([8,4],2,0,(120,0,120))
Voiture([7,3],3,0,(0,120,120))

sortie=[4,1]

case_sortie(sortie)

pause=False
attrape=None
coords=[0,0]
fini=False
deplacer_perso(coords,(0,0))
while not fini:
  #fill_rect(0,200,320,222,(255,255,255))
  #draw_string(str(coords[0])+", "+str(coords[1]),150,200)
  if attrape is None:
    if keydown(KEY_DOWN) and coords[1]<taille_ecran[1]-1:
      deplacer_perso(coords,(0,1))
    elif keydown(KEY_UP) and coords[1]>0:
      deplacer_perso(coords,(0,-1))
    elif keydown(KEY_LEFT) and coords[0]>0:
      deplacer_perso(coords,(-1,0))
    elif keydown(KEY_RIGHT) and coords[0]<taille_ecran[0]-1:
      deplacer_perso(coords,(1,0))
    elif keydown(KEY_OK):
      tempo=tab[coords[1]][coords[0]]
      if tempo!=0:
        if type(tempo)==tuple:
          attrape=tab[coords[1]+tempo[1]][coords[0]+tempo[0]]
        else:
          attrape=tempo
  
  else:
    if keydown(KEY_DOWN):
      if deplacer(attrape,3):
        deplacer_perso(coords,(0,1))
    elif keydown(KEY_UP):
      if deplacer(attrape,1):
        deplacer_perso(coords,(0,-1))
    elif keydown(KEY_LEFT):
      if deplacer(attrape,4):
        deplacer_perso(coords,(-1,0))
    elif keydown(KEY_RIGHT):
      if deplacer(attrape,2):
        deplacer_perso(coords,(1,0))
    
    elif keydown(KEY_BACKSPACE):
      attrape=None

  if j.mouv==0:
    if j.pos[0]<=sortie[0]<j.pos[0]+j.taille and j.pos[1]==sortie[1]:
      fini=True
  else:
    if j.pos[0]==sortie[0] and j.pos[1]<=sortie[1]<j.pos[1]+j.taille:
      fini=True
  if not fini and pause:
    sleep(0.2)
    pause=False
j.dessiner(j.couleur)
print("GAGNE")