# Yathzee
#   6 dobbelstenen
#   speler kiest welke waarde hij wil sparen
#   dobbelstenen van gelijke waarde worden uit de reeks verwijderd



import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING
from ScoreCard import ScoreCard

card = ScoreCard

aantal_stenen = 5
spaarsteen = 0
aantal_van_waarde = 0
gespeeld = [0,0,0,0,0]
ronde = 0

# gebruiker wordt gevraagd om een eerste poging te wagen.
answer = askokcancel("Wilt u nog een poging wagen?",message='Eerste poging.', icon="info")    

while answer == True:
    ronde = 0
    while ronde < 3:

        lijst = []
        # lijst wordt met dummy waarde 0 gevuld
        for i in range(aantal_stenen):
            lijst.append(0)

        # lijst wordt met random getallen gevuld
        for i in range(aantal_stenen):
            lijst[i] = random.randint(1,6)
        
        # de gebruiker wordt gevraagd om het aantal wielen van de gokkast op te geven
        print("Dit bevat de huidige lijst:")
        print(lijst)
        print()

        if spaarsteen == 0:
            spaarsteen = int(input("Welke steen (1-6) wil je sparen? "))

        # tellen wat de totale waarde is
        aantal_van_waarde = aantal_van_waarde + (lijst.count(spaarsteen) * spaarsteen)

        # aantal stenen verminderen
        aantal_stenen = aantal_stenen - lijst.count(spaarsteen)

        # print de totale waarde tonen
        print(str(ronde + 2) + " De totale waarde van de spaarsteen " + str(spaarsteen) + " is " + str(aantal_van_waarde))

        # er zijn geen stenen in de lijst die overeenkomen met de spaarsteen
        #if lijst.count(spaarsteen) == 0:
        #    gespeeld[spaarsteen-1] = aantal_van_waarde
        #    print("Dit is er tot nu toe gespeeld: ")
        #    print(gespeeld)
        #    spaarsteen = 0
        #    aantal_van_waarde = 0
        #    aantal_stenen = 5
        #    break

        # answer = askokcancel("Wilt u nog een poging wagen? ",message='Poging: ' + str(ronde + 2), icon="info")    

        ronde = ronde + 1
        print("Ronde is" + str(ronde))

print("Het spel is ten einde, dit heb je bereikt:")
print(gespeeld)
totaleWaarde = 0
for i in range(6):
    print(str(i+1) + " x " + str(gespeeld[i]) + " = " + str((i+1) * gespeeld[i]))
    totaleWaarde = totaleWaarde + (i+1) * gespeeld[i]

print("Met een totale waarde van:" + str(totaleWaarde))