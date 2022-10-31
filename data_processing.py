#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    # checks if input file exists
    if not os.path.exists(path_reading):
        # what to do if the input file does not exist?
        return False
    # open path_reading as reading ("r" meaning read)
    with open(path_reading, 'r') as reading:
        # opens path_writing in "W" = writing mode. or creating the file if it does not exist
        with open(path_writing, "w") as writing:
            # write in file with writing.write(n) where n is the written part

            # making the lines readable
            lines = reading.readlines()
            # return empty file if input file is empty
            if len(lines) == 1:
                return
            # line counter so no "\n" will be added to the end
            line_counter = len(lines)
            # go through the lines
            for line in lines:
                # replace 1st line with Firstname,Lastname
                if line == lines[0]:
                    writing.write("Firstname,Lastname\n")
                    line_counter -= 1
                    continue
                # line is not empty
                if line.strip():

                    # removing ; if it exists
                    place = line.find(";") + 1
                    if place > 0:
                        # swap first and last name
                        temporary_line = line[place:] + " " + line[:place-1]
                        new_line = temporary_line.split()
                    else:
                        new_line = line.split()
                    # now checking if a last name exists
                    if len(new_line) > 1:
                        writing.write(new_line[0] + "," + new_line[-1])
                    # if not then write "Lastname" as last name
                    else:
                        writing.write(new_line[0] + ",Lastname")
                # line is empty so we write ","
                else:
                    writing.write(",")
                # if not last line then go 1 line down
                if line_counter > 1:
                    writing.write("\n")
                line_counter -= 1


    # the rest of your implementation


# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "public/my_data.txt"
OUTPUT_PATH = "public/my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")

