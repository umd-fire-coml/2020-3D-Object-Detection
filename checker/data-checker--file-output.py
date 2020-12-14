import os
from os import path

os.chdir(os.path.join(os.path.dirname(__file__), '..'))
filepaths= []
filename= 'data-checker--file-output.txt'

for root, dirs, files in os.walk('data', topdown=True):
    for i in files:
      filepaths.append(os.path.join(root, i).replace("\\","/"))

with open(os.path.join('checker', filename), 'w', encoding= 'utf8') as file:
    for i in filepaths:
        file.write(i+ '\n')
    file.close()

print(f'{len(filepaths)} files found, filepaths saved to {filename}')