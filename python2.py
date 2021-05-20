import numpy as np


def input_pckt():   # Function to take input from user
    flag = 1
    while flag:     # Test Case: No more than 8 packets
        number_of_packets = int(input("Enter number of packets(8 max): "))
        if number_of_packets < 9:
            flag = 0
    pckt = np.zeros(number_of_packets, dtype=int)   # Intialise empty numpy array with zeros.

    for i in range(0, number_of_packets):
        print("Packet ", i+1, ":")
        flag = 1
        while flag: # Take the actual input, Test Case: Packet value should be between 0 & 7
            ip = int(input("Enter Output Port Number (0-7): "))
            if 0 <= ip < 8:
                flag = 0
        pckt[i] = ip
    return pckt


def sort_packets(array):    # Sort Input Array
    return np.sort(array)


def intToBi(num):           # Convert integer to Binary.
    res = (bin(num).replace("0b", ""))
    while len(res) != 3:  # To always get an 8-bit output irrespective of the input.
        res = '0' + res
    return res

# Batcher-Banyan Network
# 1 -> 1,3; 1: 1,2
# 2 -> 2,4; 2: 1,2
# 3 -> 1,3; 3: 3,4
# 4 -> 2,4; 3: 3,4


def bbn(packet):        # Function for Batcher-Banayan Network.
    for i, ip in enumerate(packet): # i contains the index, ip contains the actual packet.

        op_bin = intToBi(ip)    # Store binary value of packet.
        path = ['','','']       # Initialise path array.

        for j, val in enumerate(op_bin):    # Iterate through every bit, starting from Left Most Bit.
            if val == '0':                  # if 0 then set output of switching element to high,
                path[j] = 'High'
            else:                           # if 1 then set output to low.
                path[j] = 'Low'
        print("\nInput:", str(ip))          # Print Input (packet)
        print("Switching Element: ", (int(i/2) + 1))    # Print Switching Element number.
        print(path, "\nOutput: ", str(ip))              # Print Output port number.


pckt = input_pckt()                     # Function call for taking input from the user.
print("\n")
print("Input (Unsorted):", pckt)        # Print input packets.
sorted_packet = sort_packets(pckt)      # Sort the input packets.
print("Input (Sorted): ", sorted_packet) # Print sorted input packets.
print("\n")

bbn(pckt)                               # Function call for batcher-banyan network simulation.
