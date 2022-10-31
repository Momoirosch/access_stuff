#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):

    # does the file exist?
    if not os.path.exists(path):
        return None

    # open the file
    file = open(os.path.join(path))

    # saving the values of the sum_of_all_grades and the num_of_grades
    sum_of_all_grades = 0.0
    num_of_grades = 0

    # calculating sum_of_all_grades and num_of_grades
    for line in file.readlines():
        # compress into string
        line = line.replace("\n", "")
        line = line.replace("\t", "")

        # skip lines that are (empty, comments, non grades)
        if len(line) == 0:
            continue
        # starts with "#"
        if "".join(line.split()) == "#":
            continue
        # ends with ":"
        if line.find(":") == -1:
            continue

        # grade is the element 1 of the line
        grade = line.split(":")[1]

        # remove blank from grade
        grade = grade.strip()

        num_of_grades += 1
        sum_of_all_grades += float(grade)

    file.close()

    # prevent divide by zero error
    if num_of_grades == 0:
        return 0.0

    # calculate average grade
    average_grade = sum_of_all_grades / num_of_grades
    return average_grade




    # checking if there are grades at all to prevent a divide by 0 error
    # and returning 0.0
    print(f"sum_of_all_grades = {sum_of_all_grades}")
    print("num_of_grades = %f" % num_of_grades)
    if num_of_grades == 0:
        return 0.0

    # calculating the average_grade
    average_grade = sum_of_all_grades / num_of_grades
    return average_grade



    # 0.0 if there are no grades in the file

    return -1


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("my_grades.txt"))

