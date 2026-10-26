tempFahrenheit = 35

def fahrenheit2celsius(tempFahrenheit):
    return (tempFahrenheit - 32) * (5/9)

if __name__ == "__main__":
    print("Fahrenheit to Celsius")
    print("35 graden Fahrenheit is " + str(fahrenheit2celsius(tempFahrenheit)) + " graden Celsius.")
    print()