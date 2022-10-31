#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def invert(d):
    # implement this function
    d = dict(sorted(d.items()))
    x = {}
    length = len(d)
    for key in d:
        if d[key] not in x:
            x[d[key]] = [list(d.keys())[-length]]
            length -= 1
        # if key already has a value the new value should be a tuple of old and new
        else:
            x[d[key]].append(list(d.keys())[-length])
            length -= 1
    # Changing the dictionary to a list, so I can sort it
    x = dict(sorted(x.items()))
    return x

def invrt(d):
    d.list


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(invert({"a":2, "d":2, "c":1, "b":2}))
