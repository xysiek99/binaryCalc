from main import decimalToBinary, binaryToDecimal
import os

options = ["Binary to decimal", "Decimal to binary", "Exit"]
options_range = range(1, len(options) + 1)
binary_values = range(0,2)
decimal_values = range(0,10)

# def menuLoop():
#     incorrectInput = True
#     while incorrectInput:
#         user_input = input()
#         if (checkInt(user_input, options_range)):
#             incorrectInput = False
    
#     if (int(user_input) == 1):
#         print(options[0])
#     if (int(user_input) == 2):
#         print(options[1])
#     if (int(user_input) == 3):
#         print(options[2])
    
def checkOption(input_number, input_range):
    try:
        if int(input_number) in input_range:
            return True
        else:
            raise Exception
    except:
        print("Incorrect input")

def checkValue():
    pass

class Menu:
    def __init__(self, header, options = None, input_range = None, accepted_values = None):
        self.header = header
        self.options = options
        self.input_range = input_range
        self.accepted_values = accepted_values
        self.incorrect_input = False

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
        self.incorrect_input = True
        while self.incorrect_input:
            user_input = input()
            if (checkOption(user_input, self.input_range)):
                self.incorrectInput = False
                break

class BinaryMenu(Menu):
    def __init__(self, header, options = None, input_range = None, accepted_values = None):
        super().__init__(header, options, input_range, accepted_values)

class DecimalMenu(Menu):
    def __init__(self, header, options = None, input_range = None, accepted_values = None):
        super().__init__(header, options, input_range, accepted_values)


mainMenu = Menu("BINARY & DECIMAL CALCULATOR", options = options, input_range = options_range)
binaryMenu = BinaryMenu("Enter binary value", accepted_values = binary_values)
decimalMenu = DecimalMenu("Enter decimal value", accepted_values = decimal_values)

mainMenu.loopMenu()