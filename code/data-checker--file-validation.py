import os

def check_dir(text_file_name):
    invalid_num = 0
 
    # loop through each line in file
    with open(text_file_name, "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            if not os.path.isfile(stripped_line):
                invalid_num += 1
                print("This file does not exist: ", stripped_line)

    return invalid_num


if check_dir('code/data-checker--file-output-MASTER.txt') > 0:
    print("***********************************************************")
    print("Data not valid")
else:
    print("***********************************************************")
    print("Data is valid")