from main import decimalToBinary, binaryToDecimal
import os

options = ["Binary to decimal", "Decimal to binary", "Exit"]
options_range = range(1, len(options) + 1)
binary_values = range(0,2)
decimal_values = range(0,10)

def checkIfDecimal(user_inp):
    try:
        if int(user_inp):
            for i in user_inp:
                if not (i=="0" or i=="1"):
                    raise Exception
            print(binaryToDecimal(int(user_inp)))
        else:
            raise Exception
    except:
        print("Incorrect input")

def checkIfInt(user_inp):
    try:
        if int(user_inp):
            print(decimalToBinary(int(user_inp)))
        else:
            raise Exception
    except:
        print("Incorrect input")   

class Menu:
    def __init__(self, header, options = None):
        self.header = header
        self.options = options

    def displayHeader(self):
        os.system('cls||clear')
        print(self.header)
        print("---------------------------")

    def displayOptions(self):
        i = 1
        for option in self.options:
            print(f"{i}. {option}")
            i += 1

class BinaryMenu(Menu):
    def __init__(self, header, options = None):
        super().__init__(header, options)

class DecimalMenu(Menu):
    def __init__(self, header, options = None):
        super().__init__(header, options)


mainMenu = Menu("BINARY & DECIMAL CALCULATOR", options = options)
binaryMenu = BinaryMenu("Enter binary value")
decimalMenu = DecimalMenu("Enter decimal value")


def startBinaryMenu():
    binaryMenu.displayHeader()
    user_inp = input()
    checkIfDecimal(user_inp = user_inp)
    input("Press Enter...")
    startMainMenu()

def startDecimalMenu():
    decimalMenu.displayHeader()
    user_inp = input()
    checkIfInt(user_inp = user_inp)
    input("Press Enter...")
    startMainMenu()

def startMainMenu():
    display = True
    mainMenu.displayHeader()
    mainMenu.displayOptions()
    
    while display:
        my_inp = input()
        if my_inp == "1":
            display = False
            startBinaryMenu()
        elif my_inp == "2":
            display = False
            startDecimalMenu()
        elif my_inp == "3":
            break
        else:
            print("Incorrect input")


startMainMenu()