import time
import random

tempFahrenheit = 35


def fahrenheit2celsius(tempFahrenheit):
    return (tempFahrenheit - 32) * (5/9)

def add(a, b):
    return a + b

def divide(a, b):
    return a / b

def priemgetalbepalen(getal):
    if getal < 2:
        return False

    for i in range(2, getal):
        if getal % i == 0:
            return False

    return True

def greater_or_smaller(a, b):
    if a > b:
        return True
    else:
        return False

def return_values():
    x = random.randint()
    return x

if __name__ == "__main__":
    print("Fahrenheit to Celsius")
    print("35 graden Fahrenheit is " + str(fahrenheit2celsius(tempFahrenheit)) + " graden Celsius.")
    print()
    print(greater_or_smaller(3,5))
    print(greater_or_smaller(7,2))