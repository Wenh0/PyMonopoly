from random import *
import tkinter as tk
from tkinter import Label

# initialisation de la fenêtre
root = tk.Tk()
root.geometry("500x600")
root.title("Monopoly vla super")
canvas = tk.Canvas(root, height=500, width=500, bg="white")
canvas.pack()

# variables importantes
counter = 0

# fonctions importantes
def drawMap():
    pass

def start():
    pass

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

#aligner les boutons en colonnes et lignes
buttonFrame = tk.Frame(root, bg="lightgray")

start = tk.Button(buttonFrame, text="Jouer")
start.grid(row=0, column=0)

next = tk.Button(buttonFrame, text="Prochain tour", fg="gray")
next.grid(row=0, column=2)

#ajouter et enlever des joueurs
addPlayer = tk.Button(buttonFrame, text="+", command = lambda: playerCount("+"))
addPlayer.grid(row=1, column=2)
playerCounter = tk.Label(root, text='nombres de joueurs : 0')
playerCounter.pack()
removePlayer = tk.Button(buttonFrame, text="-", command = lambda: playerCount("-"))
removePlayer.grid(row=1, column=0)

buttonFrame.pack()
# textes informatifs

# fin
root.mainloop()