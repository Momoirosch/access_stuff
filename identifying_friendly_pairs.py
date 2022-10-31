# You are completely free to change this variables to check your algorithm.
num1 = 6
num2 = 28


# Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    # You need to complete this function.
    # You need to return a boolean variable . If num1 and num2 are friendly pairs return True.
    # If they are not return False.
    # The numbers must be valid according to description before determining friendly parity situations.
    # Return "Invalid" if they are not valid.

    # checks if num1 and/or num2 are invalid
    if num1 == num2 or isinstance(num1, float) or isinstance(num2, float) or num1 < 1 or num2 < 1:
        return "Invalid"

    # looking up divisors of num1
    sum1 = 0
    for i in range(num1):
        i += 1
        if num1%i == 0:
            sum1 += i

    # looking up divisors of num2
    sum2 = 0
    for i in range(num2):
        i += 1
        if num2 % i == 0:
            sum2 += i

    if sum1/num1 == sum2/num2:
        return True
    else:
        return False


# This line prints your method's return so that you can check your output.
print(isFriendlyPair())