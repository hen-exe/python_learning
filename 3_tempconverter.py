import math
import time

def screen():

    # Get user input
    temp_from = input("Select the temperature type: | C (Celcius) | F (Fahreinheit) | K (Kelvin)").upper()
    temp_num1 = input("Input temp value:")
    
    try:
        temp_num1 = float(temp_num1)
    except ValueError:
        print("enter a valid number")
        screen()

    temp_to = input("Select target temperature type: | C (Celcius) | F (Fahreinheit) | K (Kelvin)").upper()

    temp_converter(temp_from, temp_num1, temp_to)

def temp_converter(a, num1, b):
    if a == 'C':
        if b == 'C':
            print("Can't convert same temperature type!")
            screen()
        elif b == 'F':
            result = (num1 * 9/5) + 32
            print("The value %.2f Celsius is %.2f Fahrenheit." % (num1, result))
            screen()
        elif b == 'K':
            result = num1 + 273.15
            print("The value %.2f Celsius is %.2f Kelvin." % (num1, result))
            screen()
        else:
            print("Empty! Input a temperature.")
            screen()
    elif a == 'F':
        if b == 'C':
           result = (num1 - 32) * 5/9
           print("The value %.2f Fahrenheit is %.2f Celsius." % (num1, result))
           screen()
        elif b == 'F':
            print("Can't convert same temperature type!")
            screen()
        elif b == 'K': 
            result = (num1 - 32) * 5/9 + 273.15
            print("The value %.2f Fahrenheit is %.2f Kelvin." % (num1, result))
            screen()
        else:
            print("Empty! Input a temperature.")
            screen()
    elif a == 'K':
        if b == 'C':
           result = num1- 273.15
           print("The value %.2f Kelvin is %.2f Celsius." % (num1, result))
           screen()
        elif b == 'F':
            result = (num1 - 273.15) * 9/5 + 32
            print("The value %.2f Kelvin is %.2f Celsius." % (num1, result))
            screen()
        elif b == 'K': 
            print("Can't convert same temperature type!")
            screen()
        else:
            print("Empty! Input a temperature.")
            screen()
    else:
        print("Empty! Input a temperature.")
        screen()

screen()