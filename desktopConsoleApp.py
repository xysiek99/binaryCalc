from main import decimalToBinary, binaryToDecimal
import os

options = ["Binary to decimal", "Decimal to binary", "Exit"]

menu_options = range(1,4)
binary = range(0,2)

def header():
    print("BINARY & DECIMAL CALCULATOR")
    print("---------------------------")

def checkInt(number, numberList):
    try:
        if int(number) in numberList:
            return True
        else:
            raise Exception
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
        if (checkInt(userInput1, menu_options)):
            break


mainMenu()