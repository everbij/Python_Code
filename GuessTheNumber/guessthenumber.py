import random   # zorgt ervoor dat er een random getal gekozen kan worden

random_int = random.randint(1,100)  # het getal ligt tussen 1 en 100
print(random_int)

getal_geraden = False   # boolean waarde die aangeeft dat het getal niet geraden is

for i in range(5):  # in een reeks van 5 pogingen kan er een gok gewaagd worden
    str_getal = input("Geef in de terminal een waarde op tussen de 1 en 100 \n Je hebt 5 pogingen, dit is poging " + str(i+1) + " > ")

    # input levert een string op, deze moet omgezet worden naar een integer om te vergelijken met het random getal
    getal = int(str_getal)  

    if getal == random_int:
        print()
        print("Je hebt het getal geraden, het was " + str(random_int))
        print()
        getal_geraden = True
        break
    elif getal < random_int:
        print()
        print("Het geheime getal is groter dan " + str(getal))
        print()
    else:
        print()
        print("Het geheime getal is kleiner dan " + str(getal))
        print()

if getal_geraden == False:
    print()
    print("je hebt het geheime getal helaas niet geraden, het was " + str(random_int))
