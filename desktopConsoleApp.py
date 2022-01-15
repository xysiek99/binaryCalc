from main import decimalToBinary, binaryToDecimal
import os

options = ["Binary to decimal", "Decimal to binary", "Exit"]
menu_range = range(1,4)
binary_range = range(0,2)

def headerDisplay():
    os.system('cls||clear')
    print("BINARY & DECIMAL CALCULATOR")
    print("---------------------------")

def menuDisplay():
    i = 1
    for opt in options:
        print(f"{i}. {opt}")
        i += 1

def checkInt(number, numberList):
    try:
        if int(number) in numberList:
            return True
        else:
            raise Exception
    except:
        print("Incorrect input")


def menuLoop():
    incorrectInput = True
    while incorrectInput:
        userInput = input()
        if (checkInt(userInput, menu_range)):
            incorrectInput = False
    
    if (int(userInput) == 1):
        print(options[0])
    if (int(userInput) == 2):
        print(options[1])
    if (int(userInput) == 3):
        print(options[2])
    


headerDisplay()
menuDisplay()
menuLoop()