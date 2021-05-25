import pygame as pg
from entité import Player
from grille import astar
import random
from transfoimage import pixelisation,creation_image
from PIL import Image
import random
import numpy as np
import math

import sqlite3


"""
#réinitialise la base de données SQL

remisea0()
"""
#########variables pouvant être modifié à votre guise########
# nombre d'individus simulés
nbrpoint = 50
# la distance à laquelle deux individus risque une infection
distancesecu = 30

nbrrect = input("Veuillez indiquer le nombre de zones de départs à créer")
nbrfleche = input("Veuillez indiquer le nombre de fléches à créer")

# import de la "carte"
fichierimage = "assets/hallcarrésanspoteau.png"



# transformation de l'image au format de PIL
imageSource = Image.open(fichierimage)
# renvoi un tableau representant la carte avec 1 si la case est libre et 0 si la case est un obstacle
labi = pixelisation(imageSource)
creation_image(720,6,labi)
# transformation de l'image au format de pygame
image = pg.image.load(fichierimage)
imagep = pg.image.load("assets/imagepixel_avec_poteau.png")


pg.init()  # lancement pygame
# la taille du carré qui représente un individu
taillecarre = 6
# on choisira une image en 720*720
ecranx = 720

# donne le nom de la fenétre
pg.display.set_caption("Simulation épidémiologique")

# renvoi la dimension de l'écran
ecran = pg.display.set_mode((ecranx + taillecarre, ecranx + taillecarre))

#initialisation dans pygame de l'image de la flèche.
imagefleche = pg.image.load("assets/fleche.png")
imagefleche.convert_alpha()
imagefleche=pg.transform.scale(imagefleche, (32,64))




Pointactif = []
listeposcontact = []
coorddepart = []
# initialise le compteur , qui sera l'indicateur du "temps" dans notre simulation
compteur = 0
# création de la liste des point et de leurs coordonnées d'arrivées respectives.
Point = []
CoordDepArr = []
# créer la matrice qui representera les intéractions entre les points . 1 si il y a eux intéraction et 0 sinon.
matricecontact = np.zeros((nbrpoint, nbrpoint))
matricestockage=np.zeros((nbrpoint,nbrpoint))

# fonction qui créer des rectangles pygame à partir des cliques de la souris
def creerrect():
    tempo = []
    while len(tempo) != 2:

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                tempo.append(pg.mouse.get_pos())
    rect = pg.Rect(tempo[0][0], tempo[0][1], tempo[1][0] - tempo[0][0], tempo[1][1] - tempo[0][1])
    pg.draw.rect(ecran, (255, 255, 0), rect)
    pg.display.update(rect)
    return rect


# (possible que c'est rect soit fait automatiquement à l'aide d'un code couleur pour l'image )
def prendposition():
    tempo = []
    while len(tempo) != 1:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                tempo.append(pg.mouse.get_pos())
    return (tempo)


# fonction qui créer les n zones de départs duquel les individus proviennent.
def creation_porte(n):
    zonedep = []
    for i in range(int(n)):
        zonedep.append(creerrect())
        print("la zone de départ", i + 1, "a été créer")
    pg.display.flip()
    return zonedep


def creation_fleche(nbrefleche):
    zonefleches = []
    listefleches=[]
    for k in range(int(nbrefleche)):
        print("veuillez cliquer sur le sommet haut-gauche puis bas droit de la flèche voulant être créé")
        #récolte la position du clic au format de la fenêtre
        clic1=prendposition()[0]
        #transforme la position du clic au format de l'image "pixellisé"
        point1=[clic1[0]//6,clic1[1]//6]
        clic2=prendposition()[0]
        point2=[clic2[0]//6,clic2[1]//6]


        pg.display.update()
        fleche=[]
        for x in range(int(point1[0]),int(point2[0])):
            for y in range(int(point1[1]),int(point2[1])):
                fleche.append((x,y))
        print("la fleche", k + 1, "a été créer")
        #à changer pour un pg.key 12346789 pour définir les direction au lieu d'avoir à l'écrire.
        print("Veuillez indiquer la direction de la zone fléchées(nord(8),nord-est(9),est(6),sud-est(3),sud(2),sud-ouest(1),ouest(4),nord-ouest(7)")
        direction=True
        while direction==True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key==pg.K_8:
                        direction="nord"
                        angle=0
                    elif event.key==pg.K_9:
                        direction="nord-est"
                        angle=45
                    elif event.key==pg.K_6:
                        direction="est"
                        angle=90
                    elif event.key==pg.K_3:
                        direction="sud-est"
                        angle=135
                    elif event.key==pg.K_2:
                        direction="sud"
                        angle=180
                    elif event.key==pg.K_1:
                        direction="sud-ouest"
                        angle=225
                    elif event.key==pg.K_4:
                        direction="ouest"
                        angle=270
                    elif event.key==pg.K_7:
                        direction="nord-ouest"
                        angle=315
        rectangle = pg.Rect(clic1[0], clic1[1], clic2[0] - clic1[0], clic2[1] - clic1[1])
        pg.draw.rect(ecran, (0, 100, 255), rectangle, width=1)
        center = (clic1[0] + clic2[0]) // 2, (clic1[1] + clic2[1]) // 2
        """
        # on cree un Rect qui a la taille de l'image a la position voulue
        rectangle = pg.Rect(center + imagefleche.get_size())
        """
        rectfleche = imagefleche.get_rect()
        rectfleche.center = center
        print(point1,point2,direction)
        imagefleche1=pg.transform.rotozoom(imagefleche,-angle,1)
        pos=(center[0]-imagefleche1.get_width()//2,center[1]-imagefleche1.get_height()//2)
        #création du rectangle permettant l'affichage de la fleche sur la carte
        listefleches.append([imagefleche1, pos])
        ecran.blit(imagefleche1, pos)
        pg.display.flip()

        zonefleches.append([fleche, direction])

    return (zonefleches,listefleches)

def regroupement(i, j):
    p = 0.0005
    result = random.random()
    if result < p:
        tempspause1 = random.randint(10, 200)
        tempspause2 = random.randint(10, 30)
        Point[i].pause = [True, compteur + tempspause1, compteur + tempspause1 + 20]
        Point[j].pause = [True, compteur + tempspause1, compteur + tempspause1 + 20]


def testpause():
    for i in range(len(Point)):
        if compteur >= Point[i].pause[1]:
            Point[i].pause[0] = False

# alerte covid est la fonction qui renvoi si deux individus sont trop proche signifiant un contact dangereux.
def alertecovid(x1, y1, x2, y2):
    global distancesecu, taillecarre
    contact = False
    if np.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)) < ((taillecarre) + distancesecu):
        contact = True
    return (contact)
# fonction qui actualise la position des individus sur la representation pygame.
def actualisation():
    for i in range(len(Point)):
        Point[i].centre[0] = Point[i].rect.x + Point[i].taille / 2
        Point[i].centre[1] = Point[i].rect.y + Point[i].taille / 2
    for i in range(len(actif)):
        # cette notation permet d'obtenir la matrice de contact telle que l'on ne calcule pas deux fois la même distance et test entre pts différents
        for j in range(i + 1, len(actif)):
            x1 = Point[actif[i]].rect.x
            y1 = Point[actif[i]].rect.y
            x2 = Point[actif[j]].rect.x
            y2 = Point[actif[j]].rect.y
            if alertecovid(x1, y1, x2, y2):
                matricestockage[i,j]+=1
                matricestockage[j,i]+=1
                if matricecontact[i, j] == 0:

                    """
                        enregistrement_contact(compteur,i,j,(x1+x2)/2,(y1+y2)/2)
                        """
                    matricecontact[i, j] = 1
                    matricecontact[j, i] = 1

                if Point[actif[i]].etat == "infecte" or Point[actif[j]].etat == "infecte":
                    Point[actif[i]].etat = "infecte"
                    Point[actif[j]].etat = "infecte"
                if Point[actif[i]].pause[2] < compteur and Point[actif[j]].pause[2] < compteur:
                    regroupement(actif[i], actif[j])
            else:
                #obligé de prendre int à cause des approximations

                poidscontact = math.floor(matricestockage[i, j])
                if poidscontact !=0:
                    #poidscontact est le nombre de frame durant laquel le contact a eu lieu

                    matricestockage[i,j]=0.
                    listeposcontact.append([(x1 + x2) / 2, (y1 + y2) / 2,poidscontact])
# fonction permettant le mouvement de chaque point
def mouvementauto(M, point):
    pas = 1

    if ((M[point.compteur + 1][0] * taillecarre + taillecarre / 2) - point.taille / 2) - point.rect.x < 0:
        point.rect.x += -pas
    elif ((M[point.compteur + 1][0] * taillecarre + taillecarre / 2) - point.taille / 2) - point.rect.x > 0:
        point.rect.x += pas
    if ((M[point.compteur + 1][1] * taillecarre + taillecarre / 2) - point.taille / 2) - point.rect.y < 0:
        point.rect.y += -pas
    elif ((M[point.compteur + 1][1] * taillecarre + taillecarre / 2) - point.taille / 2) - point.rect.y > 0:
        point.rect.y += pas
    actualisation()

# lancement fenêtre
running = True
# boucle principal
defrect = False
defleche = False
defchemin=False
while running:

    if defrect == False:
        # partie calcul
        ecran.blit(imagep, (0, 0))  # affichage image blanche fond
        """
        for i in range(len(obstacle)):
            pg.draw.rect(ecran, (0, 0, 0),(obstacle[i][0] * taillecarre, obstacle[i][1] * taillecarre, taillecarre, taillecarre)) # affichage obstacle
        """
        pg.display.flip()  # actualisation écran
        Point = []
        zonedep = creation_porte(nbrrect)  # création des rect

        defrect = True
        # créer les zones fléchées sous formes de blocs rectangulaires auquels leurs sont associées une direction.
        if defleche == False:
            if nbrfleche == 0:
                defleche = True
            else:
                zonefleches,listefleche = creation_fleche(nbrfleche)
                pg.display.flip()  # actualisation écran
                print("flecheslycee=", zonefleches)
                defleche = True
        if defchemin == False:
            # choix des coordonnées de depart et d'arrivées de chaque points parmi les rects
            for i in range(nbrpoint):
                rectdep = random.choice(zonedep)
                x1 = random.randint(rectdep[0], rectdep[0] + rectdep[2])
                y1 = random.randint(rectdep[1], rectdep[1] + rectdep[3])
                rectar = random.choice(zonedep)
                while rectar == rectdep:
                    rectar = random.choice(zonedep)
                x2 = random.randint(rectar[0], rectar[0] + rectar[2])
                y2 = random.randint(rectar[1], rectar[1] + rectar[3])
                Point.append(Player(x1, y1, x2, y2, taillecarre))

        pointfait = 0
        pointtot = len(Point)
        path = []
        # définition du centre des points et on leur associe à tous un path grâce au A*
        for i in range(len(Point)):
            carréx = Point[i].centre[0] // taillecarre
            carréy = Point[i].centre[1] // taillecarre
            Point[i].carré = (carréx, carréy)
            print("les coordonnées de départ du point", i + 1, "sont",
                  (Point[i].rect.x // taillecarre, Point[i].rect.y // taillecarre),
                  "et les coordonnées du point d'arrivée sont",
                  (Point[i].arrivé[0] // taillecarre, Point[i].arrivé[1] // taillecarre))
            path = path + [astar(labi, (Point[i].rect.x // taillecarre, Point[i].rect.y // taillecarre),
                                 (Point[i].arrivé[0] // taillecarre, Point[i].arrivé[1] // taillecarre), pointfait,
                                 pointtot, zonefleches)]
            pointfait += 1

        defchemin=True
        for i in range(len(Point)):
            tempsapparition = random.randint(10, 500)
            Point[i].apparition = tempsapparition

        actif = []
        actif.append(0)
        Point[0].etat = "infecte"
        defrect = True

        # créer les zones fléchées sous formes de blocs rectangulaires auquels leurs sont associées une direction.



    else:
        # partie affichage

        ecran.blit(imagep, (0, 0))
        for j in range (len(zonedep)):
            pg.draw.rect(ecran, (255, 255,0),zonedep[j])
        for k in range(len(listefleche)):

            ecran.blit(listefleche[k][0],listefleche[k][1])



        """
        for i in range(len(obstacle)):                                                       #affichage obstacle
            pg.draw.rect(ecran, (0, 0, 0),
                         (obstacle[i][0] * taillecarre, obstacle[i][1] * taillecarre, taillecarre, taillecarre))
        """
        for i in range(len(path)):  # affichage du chemin
            for j in range(len(path[i])):
                pg.draw.circle(ecran, (255, 0, 255), (path[i][j][0] * taillecarre, path[i][j][1] * taillecarre), 2)

        pointaretirer = []
        for i in actif:  # mouvement des points
            if Point[i].centre != [path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2,
                                   path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2] and \
                    Point[i].pause[0] == False:
                mouvementauto(path[i], Point[i])

            elif Point[i].centre == list((path[i][Point[i].compteur + 1][0] * taillecarre + taillecarre / 2,
                                          path[i][Point[i].compteur + 1][1] * taillecarre + taillecarre / 2)):
                if Point[i].compteur + 2 < len(path[i]):
                    Point[i].compteur += 1
            if Point[i].centre == [path[i][-1][0] * taillecarre + taillecarre / 2,
                                   path[i][-1][1] * taillecarre + taillecarre / 2]:
                pointaretirer.append(i)
            if Point[i].etat == "infecte":
                ecran.blit(Point[i].imageinf, Point[i].rect)
            else:
                ecran.blit(Point[i].image, Point[i].rect)
        pg.display.flip()

        compteur = compteur + 1
        testpause()
        """print(compteur)"""
        for i in range(len(Point)):
            if compteur == Point[i].apparition:
                actif.append(i)

        for i in pointaretirer:
            actif.remove(i)

            """
            enregistrement_durée(i,Point[i].tempsactivite)
            """

        for event in pg.event.get():  # détection touche
            if event.type == pg.QUIT:
                running = False
                print(matricecontact)
                print("les coordonnées des points où il y a eu des contacts sont", listeposcontact)
                """
                analyse_essai()
                """
                pg.quit()