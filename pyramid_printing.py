#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
h = 5

# build a string
def build_string_pyramid():

    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    s = ""
    # Enter your code here
    # use nested loops and the range() function
    # changing h to h -1 otherwise the pyramid is 1 too long
    if h == 0:
        return s
    new_h = h -1
    for i in range(new_h):
        i += 2
        # starts with 1
        s += "1"
        # if there is more it adds a * inbetween and ads up
        count = i - 2
        while count > 0:
            s += "*" + str(i - count)
            count -= 1
        # go to next line
        s += "\n"
    # now do the same the other way around
    for i in range(new_h):
        # i = h-i to flip it
        i = new_h-i
        i += 2
        # starts with 1
        s += "1"
        # if there is more it adds a * inbetween and ads up
        count = i - 2
        while count > 0:
            s += "*" + str(i - count)
            count -= 1
        # go to next line
        s += "\n"
    # adding a 1 to end it
    s += "1"
    # You don't need to change the following line.
    # It simply returns the string created above.
    return s

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid())



