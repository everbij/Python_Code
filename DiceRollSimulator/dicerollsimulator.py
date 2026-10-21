import random   # om een random getal door de computer te laten bepalen

# speler om invoer vragen
aantal_str = input("Hoeveel dobbelstenen wil je gooien? ")

# de invoer is tekst en moet worden omgezet in een getal
aantal_int = int(aantal_str)


totale_waarde = 0
# loop voor het aantal dobbelstenen dat is ingevoerd door de speler
for i in range(aantal_int):
    dobbelsteen = random.randint(1,6)   # er wordt een willekeurige waarde tussen 1 en 6 gekozen
    totale_waarde += dobbelsteen        # de waarde wordt opgeteld
    print("De gedobbelde waarde is " + str(dobbelsteen))

print("De totale waarde = " + str(totale_waarde))
