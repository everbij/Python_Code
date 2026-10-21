# Gokkast
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING

# bepalen van het aantal dubbele waarden in de reesks van de wielen
# kan bepaald worden met een standaard functie lijst.count(i)
def aantal_gelijken():
    aantal = 0
    print(lijst)
#    print(aantal_wielen)
    for i in range(max_waarde):
#        print(lijst.count(i+1))
        print("Het aantal gelijken van waarde " +str(i+1) + " is " + str(lijst.count(i+1)))
        if lijst.count(i+1) == aantal_wielen:

            print("Je hebt gewonnen en " + str((i+1)*lijst.count(i+1)) + " punten gewonnen!")
            inzet = inzet + (lijst.count(i+1) * (i+1))
    print()

# de gebruiker moet aangeven hoeveel punten hij wil inzetten
global inzet 
inzet = int(input("Hoeveel punten wil je inzetten in deze gokkast?"))

# de gebruiker wordt gevraagd om het aantal wielen van de gokkast op te geven
aantal_wielen = int(input("Hoeveel wielen wil je in de gokkast? "))

# de gebruiker wordt gevraagd om de maximale waarde per wiel op te geven
max_waarde = int(input("Wat is de maximale waarde per wiel? "))

# gebruiker wordt gevraagd om een eerste poging te wagen.
answer = askokcancel("Wilt u nog een poging wagen?",message='Eerste poging.', icon="info")    
while answer:
    lijst = []
    # lijst wordt met dummy waarde 0 gevuld
    for i in range(aantal_wielen):
        lijst.append(0)

    # lijst wordt met random getallen gevuld
    for i in range(aantal_wielen):
        lijst[i] = random.randint(1,max_waarde)

    # methode wordt aangeroepen
    aantal_gelijken()

    # gebruiker wordt gevraagd om nog een poging te wagen
    inzet = inzet - 1
    if inzet == 0:
        print("U heeft uw complete inzet verspeeld! \n Zonde van uw geld!")
        break

    answer = askokcancel("Wilt u nog een poging wagen?",message='Nieuwe poging. De inzet =' + str(inzet), icon="info")    


