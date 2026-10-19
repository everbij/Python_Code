boolPriemgetal = True
getal = 15

def priemgetalbepalen(getal):
    if getal < 2:
        return False

    for i in range(2, getal):
        if getal % i == 0:
            return False

    return True

    