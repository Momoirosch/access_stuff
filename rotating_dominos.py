# this here is a resubmit even tho it was already working well
# but I realised that it didn't check if the most frequent (aka the used one)
# was on every domino or no
# it basically also checks for wrong inputs
# it now recognizes:
#   print(min_domino_rotations([4, 4, 4, 2, 4], [4, 4, 4, 5, 4]))
# as False (output is -1)

#!/usr/bin/env python3


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top, bottom):
    if len(top) != len(bottom):
        # print("not same length")
        return -1
    else:
        # checking that the number of elements that should be sorted for = len(top) + the amount of times
        # it is on top and bottom
        same_sided_domino = 0
        position = 0

        # finding most frequent number
        both = top + bottom
        most_frequent = both[0]
        most_frequent_count = 0
        counter = 0

        for i in both:
            current_frequency = both.count(i)
            if current_frequency > counter:
                counter = current_frequency
                num = i
        # while position < len(top) -1:
        for x in range(len(top)):
            # if they are different there is no same sided domino
            if top[position] != bottom[position] \
                    and top[position] == most_frequent or bottom[position] == most_frequent:
                if top[position] or bottom[position] == most_frequent:
                    most_frequent_count += 1
                    # print(f"{position} not same")
            # checking if said domino has the most frequent number, if yes then it will add 2 to most_frequent_count
            elif top[position] == bottom[position]:
                if top[position] == most_frequent:
                    same_sided_domino += 1
                    most_frequent_count += 2
                    # print(f"{position} same")
                else:
                    # print("top and bottom have a value that is not the most frequent number")
                    return -1
            position += 1

        # print(f"most_frequent_count {most_frequent_count}")
        # checking if enough dominos have the desired number
        if len(top) <= most_frequent_count - same_sided_domino:

            # checking what side is more efficient to flip to
            if top.count(most_frequent) >= bottom.count(most_frequent):
                # how many dominos have to be turned
                return len(top) - top.count(most_frequent)
            else:
                return len(bottom) - bottom.count(most_frequent)
        else:
            # print("not enough dominos to flip")
            return -1




# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))
