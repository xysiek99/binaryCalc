from main import decimalToBinary, binaryToDecimal
import os

options = ["Binary to decimal", "Decimal to binary", "Exit"]
options_range = range(1, len(options) + 1)
binary_values = range(0,2)
decimal_values = range(0,10)
    
def checkOption(input_number, input_range):
    try:
        if int(input_number) in input_range:
            return True
        else:
            raise Exception
    except:
        print("Incorrect input")

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
    def __init__(self, header, options = None, input_range = None, accepted_values = None):
        self.header = header
        self.options = options
        self.input_range = input_range
        self.accepted_values = accepted_values

    def displayHeader(self):
        os.system('cls||clear')
        print(self.header)
        print("---------------------------")

    def displayOptions(self):
        i = 1
        for option in self.options:
            print(f"{i}. {option}")
            i += 1

    def loopMenu(self):
        while True:
            user_input = input()
            if (checkOption(user_input, self.input_range)):
                break
                #return user_input

class BinaryMenu(Menu):
    def __init__(self, header, options = None, input_range = None, accepted_values = None):
        super().__init__(header, options, input_range, accepted_values)

class DecimalMenu(Menu):
    def __init__(self, header, options = None, input_range = None, accepted_values = None):
        super().__init__(header, options, input_range, accepted_values)


mainMenu = Menu("BINARY & DECIMAL CALCULATOR", options = options, input_range = options_range)
binaryMenu = BinaryMenu("Enter binary value", accepted_values = binary_values)
decimalMenu = DecimalMenu("Enter decimal value", accepted_values = decimal_values)


def startBinaryMenu():
    binaryMenu.displayHeader()
    user_inp = input()
    checkIfDecimal(user_inp = user_inp)
    input("Press any key...")
    startMainMenu()

def startDecimalMenu():
    decimalMenu.displayHeader()
    user_inp = input()
    checkIfInt(user_inp = user_inp)
    input("Press any key...")
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