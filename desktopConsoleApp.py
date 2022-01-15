from main import decimalToBinary, binaryToDecimal
import os

options = ["Binary to decimal", "Decimal to binary", "Exit"]

menu_options = range(1,4)
binary = range(0,2)

def header():
    print("BINARY & DECIMAL CALCULATOR")
    print("---------------------------")

def checkInt(number):
    try:
        int(number)
        return True
    except:
        print("Incorrect input")

def checkRange(numberList):
    incorrect_input = True
    while (incorrect_input):
        try:
            inp = int(input())
            if inp not in numberList:
                raise TypeError
            else:
                incorrect_input = False
                os.system('cls||clear')
        except:
            print("Incorrect input")

def mainMenu():
    header()
    i = 1

    for opt in options:
        print(f"{i}. {opt}")
        i += 1

    while True:
        userInput1 = input()
        if (checkInt(userInput1)):
            break


mainMenu()