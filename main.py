def binaryToDecimal(binaryNumber):
    reverted = str(binaryNumber)[::-1]
    get_length = len(reverted)
    decimal_value = 0

    for i in range(get_length):
        temp = reverted[i]
        decimal_value += int(temp)*2**i

    return(decimal_value)


def decimalToBinary(decimalNumber, printOperations = False):
    binary_list = []
    binary_value = ""

    while (decimalNumber >= 1):
        modulo = decimalNumber%2
        if (printOperations):
            print(f"{decimalNumber} | {modulo}")
        binary_list.insert(0,modulo)
        decimalNumber = int(decimalNumber/2)
    
    # return(f"Length: {len(binary_list)}; list: {binary_list}")

    for i in binary_list:
        binary_value = binary_value + str(i)

    return binary_value

