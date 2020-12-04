import pygame as pg
from entité import Player
from grille import astar
import random


pg.init() #lancement pygame
taillecarre = 40
ecranx =720
couleurcase = (100, 100, 100)


pg.display.set_caption("Test")

ecran = pg.display.set_mode((ecranx + taillecarre, ecranx + taillecarre))
imagefond = pg.image.load("assets/blanc.jpg") # choix image fond d'ecran





#création labi, obstacle
labi =[]
labi =[[0 for j in range (ecranx // taillecarre)] for i in range (ecranx // taillecarre)]

nbrcasedepart=20
quadri = []
obstacle =[]
coorddepart = []

nbrobstacle = 50
for i in range(nbrcasedepart):
    e = random.randint(0,len(labi)-1)
    f = random.randint(0,len(labi)-1)
    labi[e][f] = 2
    coorddepart.append((e, f))


for i in range (nbrobstacle):
    (murx,mury) = coorddepart[0]
    while (murx,mury) in coorddepart:
        murx = random.randint(0,len(labi)-1)
        mury = random.randint(0,len(labi)-1)
    labi[murx][mury] = 1
    obstacle.append((murx,mury))













#création liste point
Point = []
CoordDepArr=[]
nbrpoint=20
for i in range (nbrpoint):
    x1 = random.choice(coorddepart)
    x2 = x1
    while x2 == x1:
        x2 = random.choice(coorddepart)

    CoordDepArr.append((x1[0],x1[1],x2[0],x2[1]))

for  i in range (nbrpoint):
    Point.append(Player(CoordDepArr[i][0] * taillecarre, CoordDepArr[i][1] * taillecarre, CoordDepArr[i][2], CoordDepArr[i][3], taillecarre))

def actualisation():
    for i in range(len(Point)):
        Point[i].centre[0] = Point[i].rect.x + Point[i].taille / 2
        Point[i].centre[1] = Point[i].rect.y + Point[i].taille / 2





#calcul chemin pour chaque point
path =[]
for i in range(len(Point)):

    path =  path + [astar(labi, (Point[i].rect.x // taillecarre, Point[i].rect.y // taillecarre), Point[i].arrivé)]
    path[i].insert(0,(0,0))





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











    for i in range (ecranx // taillecarre + taillecarre):
        if i%2 ==0:

            for j in range (ecranx // taillecarre + taillecarre):
                if j%2==0:

                    pg.draw.rect(ecran, (255, 255, 255), (i * taillecarre, j * taillecarre, taillecarre, taillecarre))
                else:
                    pg.draw.rect(ecran, couleurcase, (i * taillecarre, j * taillecarre, taillecarre, taillecarre))
        else:
            for j in range (ecranx // taillecarre + taillecarre):
                if j%2==0:
                    pg.draw.rect(ecran, couleurcase, (i * taillecarre, j * taillecarre, taillecarre, taillecarre))

                else:
                    pg.draw.rect(ecran, (255, 255, 255), (i * taillecarre, j * taillecarre, taillecarre, taillecarre))
    for i in range (len(Point)):
        pg.draw.rect(ecran, (0, 255, 0), (Point[i].arrivé[0] * taillecarre, Point[i].arrivé[1] * taillecarre, taillecarre, taillecarre))
    for i in range(len(obstacle)):
        pg.draw.rect(ecran, (0, 0, 0), (obstacle[i][0] * taillecarre, obstacle[i][1] * taillecarre, taillecarre, taillecarre))





    #affichage points
    for i in range(len(Point)):
         ecran.blit(Point[i].image, Point[i].rect)




    for i in range(len(Point)):
        if Point[i].centre != [path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2, path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2]:
            mouvementauto(path[i], Point[i])


        elif Point[i].centre == list((path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2, path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2)):
            if  Point[i].compteur+2 < len(path[i]):
                Point[i].compteur +=1




    #actualisation visuelle écran
    pg.display.flip()




    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()





