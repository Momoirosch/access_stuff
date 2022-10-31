#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):
    mergelist = []
    if len(a) == 0 or len(b) == 0:
        return mergelist
    elif len(a) == len(b):
        for i in range(0, len(a)):
            mergelist.append((a[i], b[i]))
        return mergelist
    else:
        if len(a) < len(b):
            x = len(b) - len(a)
            while x > 0:
                a.append(a[-1])
                x -= 1
            for i in range(0, len(a)):
                mergelist.append((a[i], b[i]))
            return mergelist
        else:
            x = len(a) - len(b)
            while x > 0:
                b.append(b[-1])
                x -= 1
            for i in range(0, len(b)):
                mergelist.append((a[i], b[i]))
            return mergelist



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([0, 1, 2], [5, 6]))
