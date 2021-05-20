# Taking Input from the user.
dividend = int(input("Enter Dividend: "))
# Checking that the divisor is not zero.
while True:
    divisor = int(input("Enter Divisor: "))
    if divisor == 0:
        print("Sorry I can't divide by 0 yet.\nTry Again!")
    else:
        break
# Assigning sign bit for divisor & dividend.
signD1 = 0
signD2 = 0
if dividend < 0:
    signD1 = 1
if divisor < 0:
    signD2 = 1


# To convert Decimal to 8-bit Binary representation.
def intToBi(num):
    res = (bin(num).replace("0b", ""))
    while len(res) != 8:  # To always get an 8-bit output irrespective of the input.
        res = '0' + res
    return res


# To take 2's compliment
def twosCompliment(M):
    nM = -int(M, 2)
    res = bin(nM & 0b11111111).replace("0b", "")
    return res


# To perform Left Shift
def shiftLeft(AC, Q):
    AC = AC[1:] + Q[0]  # Shifting values of AC & Q to the LEFT by 1-bit.
    Q = Q[1:] + '_'  # Value of Q0(LSB) gets decided further in the algorithm.
    return AC, Q


# To perform Addition operation.
def acPlusM(AC, M):
    i = len(AC) - 1                       # To get the number of bits.
    ACnew = ''                            # Initializing variables.
    carry = 0                             # Initializing variables.
    while i >= 0:                         # Run till i is not negative.
        if AC[i] == '0' and M[i] == '0':  # When the two bits being added are both 0
            if carry == 1:                # And Carry is 1
                ACnew += '1'              # Assign 1
                carry = 0                 # Change carry to 0
            else:                         # And when Carry = 0
                ACnew += '0'              # Assign 0
        elif (AC[i] == '0' and M[i] == '1') or (AC[i] == '1' and M[i] == '0'):  # When the two bits being added are
                                          # either 0,1 or 1,0
            if carry == 1:                # And Carry is 1
                ACnew += '0'              # Assign 0
            else:                         # And when Carry = 0
                ACnew += '1'              # Assign 1
        else:                             # When the two bits being added are both 1.
            if carry == 1:                # And Carry is 1
                ACnew += '1'              # Assign 1
            else:                         # And when Carry = 0
                ACnew += '0'              # Assign 0
                carry = 1                 # Change carry to 1
        i -= 1                            # decrement i by 1
    return ''.join(reversed(ACnew))       # Reversing the bits to get the final output of addition.


# To perform restoring division
def division():
    # Initializing variables
    AC = "00000000"
    Q = intToBi(abs(dividend))          # Taking absolute values (Modulus) since restoring algorithm only works for unsiged integers.
    M = intToBi(abs(divisor))
    negM = twosCompliment(M)
    count = 8                           # Since we are simulating restoring division with 8-bit registers.

    print("A: ", AC)
    print("Q: ", Q)
    print("M: ", M)

    if dividend == divisor:             # TEST CASE 1
        return AC, '00000001'
    elif abs(dividend) < abs(divisor):  # TEST CASE 2
        return Q, '00000000'
    else:
        while count > 0:                # Running the loop till count is greater than 0
            AC, Q = shiftLeft(AC, Q)    # Performing Shift Left Operation
            AC = acPlusM(AC, negM)      # Performing AC => AC - M
            if AC[0] == '1':            # When AC is negative
                Q = Q[:7] + '0'         # Append '0' at Q0 (LSB)
                AC = acPlusM(AC, M)     # Revert AC, by AC => AC + M
            else:                       # When AC is positive
                Q = Q[:7] + '1'         # Append '1' at Q0 (LSB)
            count -= 1                  # Decrement value of count by 1
        return AC, Q                    # Return the content of AC & Q


# Storing the result in variable Remainder & Quotient
Remainder, Quotient = division()

# Checking the sign of the Divisor & Dividend
# And displaying the result appropriately
if signD1 == 0 and signD2 == 0:          # When Divisor & Dividend positive
    print("Quotient(AC): ", Quotient)
    print("Remainder(Q): ", Remainder)
    print("Result: ", int(Quotient, 2), "R", int(Remainder, 2))

elif signD1 == 0 and signD2 == 1:       # When Divisor positive & Dividend negative
    print("Quotient(AC): ", twosCompliment(Quotient))
    print("Remainder(Q): ", Remainder)
    print("Result: ", -int(Quotient, 2), "R", int(Remainder, 2))

elif signD1 == 1 and signD2 == 0:       # When Divisor negative & Dividend positive
    print("Quotient(AC): ", twosCompliment(Quotient))
    print("Remainder(Q): ", twosCompliment(Remainder))
    print("Result: ", -int(Quotient, 2), "R", -int(Remainder, 2))

elif signD1 == 1 and signD2 == 1:       # When Divisor negative & Dividend negative
    print("Quotient(AC): ", Quotient)
    print("Remainder(Q): ", twosCompliment(Remainder))
    print("Result: ", int(Quotient, 2), "R", -int(Remainder, 2))
