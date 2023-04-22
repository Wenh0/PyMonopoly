from random import *
import tkinter as tk
import time
from tkinter import Label
from tkinter import Button

# initialisation de la fenêtre
root = tk.Tk()
root.geometry("600x750")
root.title("Monopoly vla super")
canvas = tk.Canvas(root, height=600, width=600, bg="white")

# initialisation du Canvas
image = tk.PhotoImage(file="monopoly3.png")
canvas.create_image(0, 0, image = image, anchor=tk.NW)

# variables importantes
counter = 0
colors = ['red', 'blue', 'yellow', 'green', 'purple', 'white', 'black', 'gray']
started = False

# fonctions importantes
def start():
    global pions, joueur, started
    print('oui')
    banque = []
    global counter, colors
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
        for i in range(counter):
            pions.append([520,520,0])
        print(pions)
        update(pions)
        toursuivant(joueur, pions)
        joueur = 0
        canvas.pack()
        return pions, joueur

def toursuivant():
    global started, colors
    pions = []
    pionsSuivants = []
    joueur = 0
    if started == False:
        startData = start()
        pions = startData[0]
        joueur = startData[1]
        pionsSuivants = tour(pions, joueur)
        update(pionsSuivants)
        canvas.pack()
    else:
        if started:
            pionsSuivants = tour(joueur, pionsSuivants)
            update(pionsSuivants)
            started = False
            print(f'on a commence avec le joueur {colors[joueur]}')
        else:
            print(f'longueur de la liste {len(pionsSuivants)-1}')
            if joueur == len(pionsSuivants)-1:
                joueur = 0
                print(f'on a remis le joueur a zero {colors[joueur]}')
                pionsSuivants = tour(joueur, pionsSuivants)
                update(pionsSuivants)
            else:
                joueur += 1
                print(f'on a change le joueur {colors[joueur]}')
                pionsSuivants = tour(joueur, pionsSuivants)
                update(pionsSuivants)
        print(f'le pion qui sort {joueur}')

def tour(joueur, pions):
    de = randint(2, 12)
    print(de)
    pionActuel = pions[joueur]
    pionActuel[2] = pionActuel[2] + de
    if pionActuel[2] > 40:
        de = de - 40 * int((de/40))
        pionActuel[2] = de
    for i in range(de):
        # print(pionActuel[0], pionActuel[1])
        if i < 10:
            pionActuel[0] -= 45
        elif 10 < i < 21:
            pionActuel[1] -= 45
        elif 20 < i < 31:
            pionActuel[0] += 45
        elif 30 < i < 41:
            pionActuel[1] += 45
        elif i >= 41:
            de = 0
    canvas.delete("all")
    return pions

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
        playerCounter.configure(text=str(counter))
        removePlayer.configure(fg='black')
    if operation == "-":
        counter -= 1
        playerCounter.configure(text=str(counter))
    if counter <= 0:
        counter = 0
        playerCounter.configure(text=str(counter))
        removePlayer.configure(fg='gray')
    if counter < 2:
        info.configure(text='pas assez de joueurs !', fg='red')
    elif counter > 8:
        info.configure(text='vous avez atteint la limite de joueurs !', fg='red')
    else:
        info.configure(text='vous pouvez jouer !', fg='green')

#aligner les boutons en colonnes et lignes

start = tk.Button(root, text="Jouer", command=lambda: toursuivant)
start['state'] = 'active'
start.pack()

next = tk.Button(root, text="Prochain tour", command=toursuivant)
next['state'] = 'disabled'
next.pack()

# ajouter et enlever des joueurs
addPlayer = tk.Button(root, text="+", command=lambda: playerCount("+"))
addPlayer.pack()
playerCounter = tk.Label(root, text='nombres de joueurs : 0')
playerCounter.pack()
removePlayer = tk.Button(root, text="-", command=lambda: playerCount("-"))
removePlayer.pack()

# textes informatifs
info = tk.Label(root, text='pas assez de joueurs', fg='red')
info.pack()

# fin
canvas.pack()
root.mainloop()