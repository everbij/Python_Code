import random

# lijst moet mogelijke keuzes
keuze =["steen", "papier", "schaar"]

# declaratie van de variabelen
comp = 0
speler = 0

print()
print("Het spel wordt in 3 rondes gespeeld, wie het hoogst aantal punten heeft gewonnen")
print()

i = 0
# gebruik hier een while-loop omdat je bij gelijkspel een extra speelronde krijgt
# de teller i wordt dan met 1 verlaagd
# dit kan niet wanneer je met een range(3) werkt
while i < 3:
    # de computer neemt een willekeurige waarde uit de lijst
    comp_random = random.randint(0,2)
    comp_keuze = keuze[comp_random]

    # de speler wordt om invoer gevraagd
    speler_keuze = input("Geef een keuze 1 = steen, 2 = papier, 3 = schaar, Uw keuze : ")
    speler_spel = keuze[int(speler_keuze)-1]

    # er wordt gekeken wie er gewonnen heeft
    if comp_keuze == "schaar" and speler_spel == "papier":
        comp = comp + 1
        i += 1
        print("De computer heeft gewonnen: schaar kan papier knippen")
        print()
    elif comp_keuze == "schaar" and speler_spel == "steen":
        print("Je hebt gewonnen: steen maakt een schaar bot")
        print()
        speler = speler + 1
        i += 1
    elif comp_keuze == "steen" and speler_spel == "papier":
        print("Je hebt gewonnen: papier kan de steen inpakken")
        print()
        speler = speler + 1
        i += 1
    elif comp_keuze == "steen" and speler_spel == "schaar":
        print("De computer heeft gewonnen: steen maakt een schaar bot")
        print()
        comp = comp + 1
        i += 1
    elif comp_keuze == "papier" and speler_spel == "steen":
        print("De computer heeft gewonnen: papier kan de steen inpakken")
        print()
        comp = comp + 1
        i += 1
    elif comp_keuze == "papier" and speler_spel == "schaar":
        print("Je hebt gewonnen: schaar kan papier knippen")
        print()
        speler = speler + 1
        i += 1
    elif comp_keuze == speler_spel:
        print("Jullie hebben hetzelfde gekozen, er is dus geen winnaar")
        i -= 1  # de teller i wordt met 1 verlaagd om een extra speelronde te maken
        print()

# het eindresultaat wordt getoonw
if comp > speler:
    print("De computer heeft gewonnen met " + str(comp) + " punten tegen de speler met " + str(speler) + " punten")
    print()
elif speler > comp:
    print("Jij hebt gewonnen met " + str(speler) + " punten tegen de computer met " + str(comp) + " punten")
    print()
else:
    print("Gelijk spel")    # kan eigenlijk niet voorkomen
    print()
