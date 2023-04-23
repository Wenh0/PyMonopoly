from random import *
import tkinter as tk
import customtkinter
import pygame
import time

# initialisation de la fenêtre
root = customtkinter.CTk()
root.geometry("600x750")
root.title("Python Monopoly")
canvas = tk.Canvas(root, height=600, width=600, bg="white")
customtkinter.set_appearance_mode("light")
root.resizable(False, False)

# initialisation du Canvas
image = tk.PhotoImage(file="monopoly3.png")
canvas.create_image(0, 0, image = image, anchor=tk.NW)

# musique ambiance
pygame.init()
pygame.mixer.music.load('musique.mp3')
pygame.mixer.music.play(-1)

pygame.mixer.music.set_volume(0.1)

# variables importantes
counter = 0
colors = ['red', 'blue', 'yellow', 'green', 'purple', 'white', 'black', 'gray']
started = False
pions = []
banque = []
joueur = 0
clique = True
cases = {"1":["marron","sansMaison",True],
        "3":["marron","sansMaison",True],
        "6":["bleu clair","sans maison",True],"8":["bleu clair","sans maison",True],"9":["bleu clair","sans maison",True],
        "11":["rose","sansMaison",True],"13":["rose","sansMaison",True],"14":["rose","sansMaison",True],
        "16":["orange","sansMaison",True],"18":["orange","sansMaison",True],"19":["orange","sansMaison",True],
        "21":["rouge","sansMaison",True],"23":["rouge","sansMaison",True],"24":["rouge","sansMaison",True],
        "26":["jaune","sansMaison",True],"27":["jaune","sansMaison",True],"29":["jaune","sansMaison",True],
        "31":["vert","sansMaison",True],"32":["vert","sansMaison",True],"34":["vert","sansMaison",True],
        "37":["bleu fonce","sansMaison",True],"39":["bleu fonce","sansMaison",True],
        "5":["gare",True],"15":["gare",True],"25":["gare",True],"35":["gare",True],
        "12":["publique",True],"28":["publique",True],
        "0":["special",200,False],"4":["special",-200,False],"10":["special","bloque",False],"20":["special","parc",False],
        "30":["special","prison",False],"38":["special",-100,False],
        "2":["caisse de communaute",False],"17":["caisse de communaute",False],"33":["caisse de communaute",False],
        "7":["chance",False],"22":["chance",False],"36":["chance",False]
        }

cartes_chance = {

    1: "Avancez jusqu'à la case départ",
    2: "Allez en prison. Ne passez pas par la case départ",
    3: "Amende pour excès de vitesse : 50M ",
    4: "Erreur de la banque en votre faveur recever 200M",
    5: "Vous êtes libéré de prison",
    6: "Payez pour frais de scolarité : 150M",
    7: "La vente de votre stocke vous rapporte 50M",
    8: "Payez une amende de 100M  ou tirez une carte 'Caisse de communauté'",
    9: "Faites des réparations dans toutes vos maisons : 25M par maison, 100M par hôtel",
    10: "Payez une amende de 50M ou tirez une carte 'Caisse de communauté'",
}

cartes_caisse = {

    1: "Avancez jusqu'à la case départ",
    2: "Allez en prison. Ne passez pas par la case départ",
    3: "Payez une cotisation de 20M ou tirez une carte 'Chance'",
    4: "Vous êtes libéré de prison. Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée",
    5: "Payez une amende de 50M ou tirez une carte 'Chance'",
    6: "Vous avez gagné le premier prix de mot croisé recevez 30M",
    7: "C'est votre anniversaire chaque joueur vous donne 15M",
    8: "Recevez votre intérêt sur l'emprunt à 7% : 25M",
    9: "Payez une cotisation d'assurance de 500M",
    10: "Ammende pour ivresse payer 50M"
}

casesPos = [[520, 520], [475, 520], [430, 520], [385, 520], [340, 520], [295, 520], [250, 520], [205, 520], [160, 520], [115, 520], [70, 520], [70, 475], [70, 430], [70, 385], [70, 340], [70, 295], [70, 250], [70, 205], [70, 160], [70, 115], [70, 70], [115, 70], [160, 70], [205, 70], [250, 70], [295, 70], [340, 70], [385, 70], [430, 70], [475, 70], [520, 70], [520, 115], [520, 160], [520, 205], [520, 250], [520, 295], [520, 340], [520, 385], [520, 430], [520, 475]]
prix = {'marron':50, 'bleu clair':100, 'rose':150, 'orange':180, 'rouge':220, 'jaune':270, 'vert':320, 'bleu fonce':370, 'gare':200, 'compagnie':150}

# fonctions importantes
def toursuivant():
    global started, colors, counter, pions, banque, joueur
    if started == False:
        print('oui')
        if counter < 2 or counter > 8:
            info.configure(text='ta gueule')
        else:
            started = True
            start["state"] = 'disabled'
            next['state'] = 'active'
            addPlayer['state'] = 'disabled'
            removePlayer['state'] = 'disabled'
            # banque initialisee
            for i in range(counter):
                banque.append(950)
            print(banque)
            # pions affiches
            solde.configure(text=f'le joueur {colors[joueur]} a {str(banque[joueur])} millions €')
            for i in range(counter):
                pions.append([520, 520, 0, []])
            pions = tour(joueur, pions)
            print(pions)
            print(f'apres le tour, pions (2) :{pions}')
            print(f'le pion qui sort {joueur}')
            solde.configure(text=f'le joueur {colors[joueur]} a {str(banque[joueur])} millions €')
            update(pions)
            canvas.pack()
    else:
        print(f'longueur de la liste {len(pions)-1}')
        print(f'pendant le tour suivant, voici la liste pions : {pions}')
        if joueur == len(pions)-1:
            joueur = 0
            print(f'on a remis le joueur a zero {colors[joueur]}')
            pions = tour(joueur, pions)
            update(pions)
        else:
            joueur += 1
            print(f'on a change le joueur {colors[joueur]}')
            pions = tour(joueur, pions)
            update(pions)
        print(joueur)
        print(banque)
        if banque[joueur] < 0:
            banque[joueur] = 'perdu'
        solde.configure(text=f'le joueur {colors[joueur]} a {str(banque[joueur])} millions €')
        print(f'le pion qui sort {joueur}')

def tour(joueur, pions):
    de = randint(2,12)
    print(de)
    pionActuel = pions[joueur]
    pionActuel[2] = pionActuel[2] + de
    if pionActuel[2] > 40:
        pionActuel[2] -= 40
    caseDeplacement = casesPos[pionActuel[2]]
    pionActuel[0] = caseDeplacement[0] # position X
    pionActuel[1] = caseDeplacement[1] # position Y
    pions[joueur] = [pionActuel[0], pionActuel[1], pionActuel[2], []]
    canvas.delete("all")
    actionCase(joueur, pions)
    return pions

def actionCase(joueur, pions):
    parc_gratuit = 0
    pionActuel = pions[joueur]
    positionpion = pionActuel[2]
    if positionpion > 40:
        positionpion -= 40
    info = cases[str(positionpion)]
    if info[0] == "marron":
        if info[2] == True:
           achat(pions, prix['marron'], joueur)
           if achat(pions, prix['marron'], joueur)[1] == True:
               info[2] = False
        else:
            loyer(pions, prix['marron'], joueur)
    elif info[0] == "bleu clair":
        if info[2] == True:
            achat(pions, prix['bleu clair'], joueur)
            if achat(pions, prix['bleu clair'], joueur)[1] == True:
                info[2] = False
        else:
            loyer(pions, prix['bleu clair'], joueur)
    elif info[0] == "orange":
        if info[2] == True:
            achat(pions, prix['orange'], joueur)
            if achat(pions, prix['orange'], joueur)[1] == True:
                info[2] = False
        else:
            loyer(pions, prix['orange'], joueur)
    elif info[0] == "rose":
        if info[2] == True:
            achat(pions, prix['rose'], joueur)
            if achat(pions, prix['rose'], joueur)[1] == True:
                info[2] = False
        else:
            loyer(pions, prix['rose'], joueur)
    elif info[0] == "rouge":
        if info[2] == True:
            achat(pions, prix['rouge'], joueur)
            if achat(pions, prix['rouge'], joueur)[1] == True:
                info[2] = False
        else:
            loyer(pions, prix["rouge"], joueur)
    elif info[0] == "jaune":
        if info[2] == True:
            achat(pions, prix["jaune"], joueur)
            if achat(pions, prix['jaune'], joueur)[1] == True:
                info[2] = False
        else:
            loyer(pions, prix["jaune"], joueur)
    elif info[0] == "vert":
        if info[2] == True:
            achat(pions, prix["vert"], joueur)
            if achat(pions, prix['vert'], joueur)[1] == True:
                info[2] = False
        else:
            loyer(pions, prix["vert"], joueur)
    elif info[0] == "bleu fonce":
        if info[2] == True:
            if achat(pions, prix['bleu fonce'], joueur)[1] == True:
                info[2] = False
        else:
            loyer(pions, prix["bleu fonce"], joueur)
    elif info[0] == "gare":
        if info[1] == True:
            achat(pions, prix["gare"], joueur)
            if achat(pions, prix['gare'], joueur)[1] == True:
                info[1] = False
        else:
            loyer(pions, prix["gare"], joueur)
    elif info[0] == "chance":
        carte_chance()
    elif info[0] == "caisse de communaute":
        caisse_de_com()
    elif info[0] == "special":
       if type(info[1]) == int:
           banque[joueur] += info[1]
       else:
            if info[1] == "prison":
                prison = casesPos[10]
                pionActuel[0] = prison[0]
                pionActuel[1] = prison[1]
            elif info[1] == "parc":
                pass
    elif info[0] == "publique":
        if info[1] == True:
            achat(pions, prix["compagnie"], joueur)
            if achat(pions, prix['compagnie'], joueur)[1] == True:
                info[1] = False
        else:
            loyer(pions, prix["compagnie"], joueur)
    return pions

def achat(pions, prix, joueur):
    moneysound = pygame.mixer.Sound("argent.mp3")
    pygame.mixer.Sound.play(moneysound)
    print('salut')
    global banque, clique
    achete = False
    if clique == True:
        print('oui')
        pionActuel = pions[joueur]
        print(pionActuel)
        pionActuel[3].append(pionActuel[2])
        pions[joueur] = pionActuel
        banque[joueur] -= prix
        achete = True
    return pions, achete

def loyer(pions, prix, joueur):
    moneysound = pygame.mixer.Sound("argent.mp3")
    pygame.mixer.Sound.play(moneysound)
    global banque
    pionJoueur = pions[joueur]
    compteur = 0
    for i in pions:
        pionActuel = i
        if pionJoueur[2] in pionActuel[3]:
            banque[compteur] += prix/2
            banque[joueur] -= prix/2
        compteur += 1
    return pions

def caisse_de_com():
    carte_aleatoire = randint(1,10)
    sonCarte = pygame.mixer.Sound("carte.mp3")
    pygame.mixer.Sound.play(sonCarte)
    canvas.create_rectangle(240, 190, 360, 410, fill='white')
    canvas.create_rectangle(245, 195, 355, 405, fill='orange')
    canvas.create_text(300, 240, text="CAISSE \n DE \n COMMUNAUTE", justify=tk.CENTER, font=('Helvetica 10 bold'))
    canvas.create_text(300, 300, text="Vous avancez de \n 40", justify=tk.CENTER, font=('Helvetica 9 italic'))

def carte_chance():
    carte_aleatoire = randint(1, 10)
    sonCarte = pygame.mixer.Sound("carte.mp3")
    pygame.mixer.Sound.play(sonCarte)
    canvas.create_rectangle(240, 190, 360, 410, fill='white')
    canvas.create_rectangle(245, 195, 355, 405, fill='orange')
    canvas.create_text(300, 240, text="CAISSE \n DE \n COMMUNAUTE", justify=tk.CENTER, font=('Helvetica 10 bold'))
    canvas.create_text(300, 300, text="Vous avancez de \n 40", justify=tk.CENTER, font=('Helvetica 9 italic'))

def update(pionsPos):
    global image
    canvas.create_image(0, 0, image=image, anchor=tk.NW)
    pionActuel = []
    compteCouleurs = 0
    #print(pionsPos)
    for i in pionsPos:
        pionActuel = i
        canvas.create_rectangle(pionActuel[0], pionActuel[1], pionActuel[0] + 20, pionActuel[1] + 20, fill=colors[compteCouleurs])
        compteCouleurs += 1

def playerCount(operation:str):
    global counter, playerCounter, addPlayer, removePlayer
    if operation == "+":
        counter += 1
        playerCounter.configure(text=f'nombre de joueurs : {str(counter)}')
        removePlayer.configure(text_color='black')
    if operation == "-":
        counter -= 1
        playerCounter.configure(text=f'nombre de joueurs : {str(counter)}')
    if counter <= 0:
        counter = 0
        playerCounter.configure(text=f'nombre de joueurs : {str(counter)}')
        removePlayer.configure(text_color='gray')
    if counter < 2:
        info.configure(text='pas assez de joueurs !', text_color='red')
    elif counter > 8:
        info.configure(text='vous avez atteint la limite de joueurs !', text_color='red')
    else:
        info.configure(text='vous pouvez jouer !', text_color='green')

#aligner les boutons en colonnes et lignes
start = customtkinter.CTkButton(root, text="Jouer", command=toursuivant)
start['state'] = 'active'
start.place(x=5,y=5)

next = customtkinter.CTkButton(root, text="Prochain tour", command=toursuivant)
next['state'] = 'disabled'
next.place(x=450,y=5)

# ajouter et enlever des joueurs boutons
addOrRemove = customtkinter.CTkFrame(root)
addPlayer = customtkinter.CTkButton(addOrRemove, text="+", command=lambda: playerCount("+"), width=20)
addPlayer.grid(row=0, column=2, sticky='ne', pady=5)
playerCounter = customtkinter.CTkLabel(addOrRemove, text='nombres de joueurs : 0')
playerCounter.grid(row=0, column=1, sticky='nsew', padx=10, pady=5)
removePlayer = customtkinter.CTkButton(addOrRemove, text="-", command=lambda: playerCount("-"), width=20)
removePlayer.grid(row=0, column=0, sticky="nw", pady=5)

addOrRemove.pack()

# bouton vla avance pour acheter les cases
#achatBouton = customtkinter.CTkButton(root, text="acheter", command=achete, width=20)
#achatBouton.place(x=5,y=30)

# textes informatifs
info = customtkinter.CTkLabel(root, text='pas assez de joueurs', text_color='red')
info.pack()

solde = customtkinter.CTkLabel(root, text='950 millions €', text_color='blue')
solde.pack()

# fin
canvas.pack()
root.mainloop()