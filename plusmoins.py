"""Donc le but du jeu c'est de définir un int aléatoire et de demander au joueur de le trouver
en lui donnant des indices 'supérieur ou inférieur'"""

# On définit un int aléatoire
from random import randint
but = randint(0,100)
win = False
vie = 5

# On a notre chiffre et notre variable condition de victoire créés, on lance la boucle de comparaison
while win == False and vie != 0:
    print("Vie(s) : ", vie, "\n")
    nmb_ut = input("Choisissez un nombre :")
    nmb_ut = int(nmb_ut)
    if nmb_ut < but:
        print("C'est trop petit mon con")
        vie = vie - 1
    elif nmb_ut > but:
        print("C'est trop grand mon con")
        vie = vie - 1
    elif nmb_ut == but:
        print("C'est gagné, yes we did it !")
        win = True
if vie == 0:
        print("La mort, la mort, la moooooort")