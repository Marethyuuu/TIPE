import pygame as pg
from entité import Player
from grille import astar
from transfoimage import transfoimage
import random



pg.init() #lancement pygame
taillecarre = 1
ecranx =720
ecrany = 720
couleurcase = (100, 100, 100)


pg.display.set_caption("Test")

ecran = pg.display.set_mode((ecranx + taillecarre, ecrany + taillecarre))
imagefond = pg.image.load("assets/blanc.jpg") # choix image fond d'ecran





#création labi, obstacle
labi =[]
#labi =[[0 for j in range (ecranx // taillecarre)] for i in range (ecrany // taillecarre)]
labi = transfoimage()






obstacle =[]
coorddepart = []


for i in range (len(labi)):
    for j in range (len(labi)):
        if labi[i][j] ==1:
            obstacle.append((i,j))
        if labi[i][j] ==2:
            coorddepart.append((i,j))














#création liste point
Point = []
CoordDepArr=[]
<<<<<<< HEAD
nbrpoint=5
=======
nbrpoint=100
>>>>>>> parent of 41b29d3... amélioration
for i in range (nbrpoint):
    x1 = random.choice(coorddepart)
    x2 = x1
    while x2 == x1:
        x2 = random.choice(coorddepart)

    CoordDepArr.append((x1[0],x1[1],x2[0],x2[1]))

for  i in range (nbrpoint):
    Point.append(Player(CoordDepArr[i][0] , CoordDepArr[i][1], CoordDepArr[i][2], CoordDepArr[i][3], taillecarre))

def actualisation():
    for i in range(len(Point)):
        Point[i].centre[0] = Point[i].rect.x + Point[i].taille / 2
        Point[i].centre[1] = Point[i].rect.y + Point[i].taille / 2




'''
#calcul chemin pour chaque point
path =[]

<<<<<<< HEAD



for i in range(nbrpoint):
    path += [[(120,400),(600,200),(320,100),(40,600)]]
print(path)

=======
    path =  path + [astar(labi, (Point[i].rect.x // taillecarre, Point[i].rect.y // taillecarre), Point[i].arrivé)]
    path[i].insert(0,(0,0))
    print("path",path)

'''
>>>>>>> parent of 41b29d3... amélioration


#lancement fenêtre
running = True

def mouvementauto (M,point):


    if ((M[point.compteur+1][0]*taillecarre + taillecarre/2) - point.taille /2)- point.rect.x < 0:
        point.rect.x += -1
    elif ((M[point.compteur+1][0]*taillecarre + taillecarre/2) - point.taille /2)- point.rect.x > 0:
        point.rect.x += 1
    if ((M[point.compteur+1][1]*taillecarre + taillecarre/2) - point.taille /2)- point.rect.y < 0:
        point.rect.y += -1
    elif ((M[point.compteur+1][1]*taillecarre + taillecarre/2) - point.taille /2)- point.rect.y > 0:
        point.rect.y += 1
    actualisation()








#boucle principal
while running:

    ecran.blit(imagefond, (0, 0))     #affichage du fond blanc

    for i in range (len(Point)):
        carréx = Point[i].centre[0] // taillecarre
        carréy = Point[i].centre[1] // taillecarre
        Point[i].carré = (carréx, carréy)

    for j in range(len(labi)):
        for i in range(len(labi[j])):
            if labi[i][j] == 2:
                pg.draw.rect(ecran, (55, 55, 55), (i * taillecarre, j * taillecarre, taillecarre, taillecarre))
            if labi[i][j] == 0:
                pg.draw.rect(ecran, (55, 0, 55), (i * taillecarre, j * taillecarre, taillecarre, taillecarre))

    #affichage points
    for i in range(len(Point)):
         ecran.blit(Point[i].image, Point[i].rect)


    '''for i in range(len(Point)):
        if Point[i].centre != [path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2, path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2]:
            mouvementauto(path[i], Point[i])


        elif Point[i].centre == list((path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2, path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2)):
            if  Point[i].compteur+2 < len(path[i]):
                Point[i].compteur +=1'''


'''

    #actualisation visuelle écran
    pg.display.flip()




    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
'''




