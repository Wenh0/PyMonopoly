from tkinter import *
from PIL import Image,ImageTk
from random import *

root = Tk()
root.geometry('600x700')
root.title('Monopoly')

#root.resizable(False, False)

# canevas ou il y aura le plateau + pions
canvas = Canvas(root, width = 600, height = 600)
img= ImageTk.PhotoImage(Image.open("assets\monopoly3.png"))
canvas.create_image(0,0,anchor=NW,image=img)
canvas.pack()

#les pions
img2 = ImageTk.PhotoImage(Image.open('assets\pion1.png'))
pion = Label(root, width=5, height=2, anchor=CENTER, bg='black')
pion.pack()
canvas.create_window(50, 50, window=pion)
pion.place(relx = 0.1,
                   rely = 0.1,
                   anchor = 'center')

# le dé
de = Label(root, width=4, height=2, anchor = CENTER, bg ='black') 
de.pack()
canvas.create_window(50, 50, window=de)
de.place(relx = 0.4,
                   rely = 0.6,
                   anchor = 'center'
                   )
#les contrôles




x=0.1
def rightclick():
    global x
    x = x + 0.1
    pion.place(relx = x, anchor=CENTER)
    print("cc")

root.bind("a", rightclick())

'''on ecrit notre stratégie sur un bout de papier; la !:

Monopoly:

  lancement de dés(aléatoire)
  déplacement automatique des pions

  décisions d'achats ou non:
   si solde suppérieur a prix achat (clic droit sur la case ou l'on est)
  
  décisions de ventes:
   hypothèque
   ventes de terrain à un autre joueur

  obligation de cases:
   paiments de loyer à un autre joueur
   paiments/gains de cartes(chances|caisse de communauté) (à générer aléatoirement) à parc gratuit
   cases d'obligation d'action:
     "allez en prison"
     paiments d'impots
     parc gratuit


    tour suivant sur clic / apres un certain temps (on revient au début)

'''
cartes_chance = {
    
    0: "Avancez jusqu'à la case départ",
    1: "Allez en prison. Ne passez pas par la case départ, ne touchez pas 20 000 €",
    2: "Avancez jusqu'à la case Avenue Henri-Martin. Si vous passez par la case départ, touchez 20 000 €",
    3: "Amende pour excès de vitesse : 15 000 €",
    4: "Reculez de trois cases",
    5: "Avancez jusqu'à la case Rue de la Paix",
    6: "Rendez-vous à la Gare de Lyon",
    7: "Payez pour frais de scolarité : 150 000 €",
    8: "Prenez une carte 'Caisse de communauté'",
    9: "Allez directement en prison. Ne passez pas par la case départ, ne touchez pas 20 000 €",
    10: "Avancez jusqu'à la case Rue de la Bourse. Si vous passez par la case départ, touchez 20 000 €",
    11: "Payez une amende de 10 000 € ou tirez une carte 'Caisse de communauté'",
    12: "Faites des réparations dans toutes vos maisons : 25 000 € par maison, 100 000 € par hôtel",
    13: "Avancez jusqu'à la case Boulevard de la Villette. Si vous passez par la case départ, touchez 20 000 €",
    14: "Rendez-vous à la case départ",
    15: "Payez une amende de 5 000 € ou tirez une carte 'Caisse de communauté'",
}

cartes_caisse = {

    0: "Avancez jusqu'à la case départ",
    1: "Allez en prison. Ne passez pas par la case départ, ne touchez pas 20 000 €",
    2: "Payez une cotisation de 10 000 € ou tirez une carte 'Chance'",
    3: "Avancez jusqu'à la case Rue de la Paix",
    4: "Vous êtes libéré de prison. Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée",
    5: "Avancez jusqu'à la case Boulevard de la Villette. Si vous passez par la case départ, touchez 20 000 €",
    6: "Avancez jusqu'à la case Gare de Lyon. Si vous passez par la case départ, touchez 20 000 €",
    7: "Payez une amende de 10 000 € ou tirez une carte 'Chance'",
    8: "Rendez-vous à la case départ",
    9: "Tirez une autre carte 'Caisse de communauté'",
    10: "Payez une amende de 2 000 €",
    11: "Tirez une autre carte 'Caisse de communauté'",
    12: "Recevez votre intérêt sur l'emprunt à 7% : 25 000 €",
    13: "Tirez une autre carte 'Caisse de communauté'",
    14: "Payez une cotisation d'assurance de 50 000 €",
    15: "Tirez une autre carte 'Caisse de communauté",
}


Tour='joueur1'

root.mainloop()