def binaryToDecimal(binaryNumber):
    reverted = str(binaryNumber)[::-1]
    get_length = len(reverted)
    decimal_value = 0

    for i in range(get_length):
        temp = reverted[i]
        decimal_value += int(temp)*2**i

    return(decimal_value)

binary = 1101
print(binaryToDecimal(binary))

def decimalToBinary(decimalNumber):
    binary_list = []

    while (decimalNumber >= 1):
        modulo = decimalNumber%2
        print(f"{decimalNumber} | {modulo}")
        binary_list.insert(0,modulo)
        decimalNumber = int(decimalNumber/2)
    
    # print(f"Length: {len(binary_list)}; list: {binary_list}")
    return(f"Length: {len(binary_list)}; list: {binary_list}")

decimal = 13
print(decimalToBinary(decimal))
