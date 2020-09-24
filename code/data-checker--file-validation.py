import os

def check_dir(file_path):
    invalid_num = 0
 
    # loop through files in file_path
    for files in os.listdir(file_path):
        if files == '.DS_Store' or files == '.gitkeep':
            print("Ignored: ", os.path.join(file_path, files))
        elif files.endswith(".zip"):
            invalid_num += 1
            print("Make sure data is unzipped: ", os.path.join(file_path, files))
        else:
            for dirname in os.listdir(os.path.join(file_path, files)):
                if dirname == 'calib' or dirname == 'label_2' or dirname == 'image_3' or dirname == 'image_2':
                    for filename in os.listdir(os.path.join(file_path, files, dirname)):
                        if dirname == 'calib' or dirname == 'label_2':
                            if filename == '.DS_Store':
                                print("Ignored: ", os.path.join(file_path, files, dirname, filename))
                            elif filename.endswith(".txt") != True:
                                invalid_num += 1
                                print("File does not match proper structure: ", os.path.join(file_path, files, dirname, filename))
                        elif dirname == 'image_3' or dirname == 'image_2':
                            if filename == '.DS_Store':
                                print("Ignored: ", os.path.join(file_path, files, dirname, filename))
                            elif filename.endswith(".png") != True:
                                invalid_num += 1
                                print("File does not match proper structure: ", os.path.join(file_path, files, dirname, filename))

    return invalid_num


if check_dir('data') > 0:
    print("***********************************************************")
    print("Data not valid")
else:
    print("***********************************************************")
    print("Data is valid")

