import math
import struct
from decimal import *

getcontext().prec = 64

decimal = float(input("Enter number in decimal: "))
if decimal >= 0:
    sign = 0
else:
    decimal *= (-1)
    sign = 1

intPart = int(math.modf(decimal)[1])
decPart = round(math.modf(decimal)[0], 64)

print(decimal, "\nInteger: ", intPart, "Decimal:", decPart)


def intToBi(num):
    return int(bin(num).replace("0b", ""))


def decToBi(num, prec):
    binary = '0.'
    n = prec
    while prec:

        # Find next bit in fraction
        num *= 2
        fract_bit = int(num)

        if fract_bit == 1:

            num -= fract_bit
            binary += '1'

        else:
            binary += '0'

        prec -= 1
    return Decimal(binary)


biInt = intToBi(intPart)
biDec = decToBi(decPart, 64)
binary = biInt + biDec

print("Binary:", binary)

def biToFloat(binary, sign):

    if binary == 0:
        return ['0', '00000000', '00000000000000000000000']

    biInt = intToBi(intPart)
    biDec = decToBi(decPart, 64)
    norm = 0
    if format(binary).find('E') != -1:
        i = format(binary).find('E')
        norm = int(format(binary)[i + 1:])
        sig_str = (format(binary)[2:i - 1])

        while len(sig_str) < 23:
            sig_str = sig_str + '0'

        sig_str = sig_str[:23]
        floatpoint = [str(sign), format(intToBi(norm + 127), '8.0f').replace(" ", "0"),
                      sig_str]
        return floatpoint

    else:
        if biInt == 0:
            while biDec < 1:
                biDec *= 10
                norm += -1

        elif biInt != 1:
            norm = len(str(biInt)) - 1

        if norm > 0:
            i = format(binary).find('.')
            sig_str = format(binary).replace(".", "")
            sig_str = sig_str[i - norm:i - norm + 23]
            floatpoint = [str(sign), format(intToBi(norm + 127), '8.0f').replace(" ", "0"),
                          sig_str]
            return floatpoint

        elif norm < 0:
            sig = (binary * Decimal(math.pow(10, -norm)))

        else:
            sig = binary

        floatpoint = [str(sign), format(intToBi(norm + 127), '8.0f').replace(" ", "0"),
                          (format(sig, '.23f')).replace("1.", "").replace(" ", "0")]
        return floatpoint


res = biToFloat(binary, sign)
res1 = res[0] + res[1] + res[2]
print("\nFloating Point Representation:\n['Sign','Exponent','Mantissa']:")
print(res, "\nor")
print(res1)
