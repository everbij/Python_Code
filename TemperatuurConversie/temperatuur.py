temperatuur = 35

def fahrenheit2celsius(tempFahrenheit):
    return (tempFahrenheit - 32) * (5/9)

def celsius2fahrenheit(tempCelsius):
    return (tempCelsius * (9/5)) + 32

def celsius2kelvin(tempCelsius):
    return tempCelsius + 273.15

def fahrenheit2kelvin(tempFahrenheit):
    return celsius2kelvin(fahrenheit2celsius(tempFahrenheit))

if __name__ == "__main__":
    print("Fahrenheit to Celsius")
    print("35 graden Fahrenheit is " + str(fahrenheit2celsius(temperatuur)) + " graden Celsius.")
    print()
    print("Celsius to Fahrenheit")
    print("35 graden Celsius is " + str(celsius2fahrenheit(temperatuur)) + " graden Fahrenheit.")
    print()
    print("Celsius to Kelvin")
    print("35 graden Celsius is " + str(celsius2kelvin(temperatuur)) + " graden Kelvin.")
    print()
    print("Fahrenheit to Kelvin")
    print("35 graden Fahrenheit is " + str(fahrenheit2kelvin(temperatuur)) + " graden Kelvin.")