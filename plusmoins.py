"""Donc le but du jeu c'est de définir un int aléatoire et de demander au joueur de le trouver
en lui donnant des indices 'supérieur ou inférieur'"""

# On définit un int aléatoire
from random import randint
but = randint(0,100)
victoire = False
vie = 5

# On a notre chiffre et notre variable condition de victoire créés, on lance la boucle de comparaison
while not victoire and vie > 0:
    print("Vie(s) : ", vie, "\n")
    nombre_utilisateur = input("Choisissez un nombre :")
    nombre_utilisateur = int(nombre_utilisateur)
    if nombre_utilisateur < but:
        print("C'est trop petit mon con")
        vie = vie - 1
    elif nombre_utilisateur > but:
        print("C'est trop grand mon con")
        vie = vie - 1
    else:
        print("C'est gagné, yes we did it !")
        victoire = True
if vie == 0:
        print("La mort, la mort, la moooooort")