#!/usr/bin/env python3


# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def hamming_dist(signal_1, signal_2):

    hamming_dist_output = []

    # find dict and tuple
    if type(signal_1) is dict and type(signal_2) is tuple:
        dic, tup = signal_1, signal_2
    else:
        dic, tup = signal_2, signal_1

    # checking if length are valid
    if (not len(dic["data"]) == len(tup)) or len(dic["data"]) == 0 or len(tup) == 0:
        return "Empty signal on at least one of the sensors"

    # check length of the strings in the dict and tuple
    for index in range(len(tup)):
        if not len(dic["data"][index]) == len(tup[index]):
            return "Sensor defect detected"

    # loop to check the rest
    for string in range(len(tup)):

        hamming_dist_count = 0

        # loop to check char.
        for char in range(len(tup[string])):

            # check if char. are the same
            if not dic["data"][string][char] == tup[string][char]:
                hamming_dist_count += 1

        # add error to output
        if hamming_dist_count > 0:
            hamming_dist_output.append((dic["data"][string], tup[string], hamming_dist_count))

    return hamming_dist_output

# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
print(hamming_dist(signal_sensor_1, signal_sensor_2))
