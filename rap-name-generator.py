# Guided Exploration No. 3
# Jason Fischer

# import random graphics library
import random

# initialize list to store possible names
possible_names = []

# open text file that stores rap names
outputFile = open('rap-names-output.txt', 'w')

# open file to store rap names
with open('rap-names.txt', 'r') as dataFile:
    # initalize string accumalator
    for name in dataFile:
        # edit rap names
        possible_names.append(name.rstrip()

# enter how many rap names you want to create and how many parts it should contain
count=int(input('How many rap names would you like to create? '))
# enter how many parts should the name contain
parts=int(input('How many parts should the name contain? '))

# initialize string accumulator
for i in range(count):
    # initialize list to store names_parts
    name_parts=[]
    # initialize string accumulator
    for j in range(parts):
        # edit name_parts
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

# add to name_parts
outputFile.write(f"{' '.join(name_parts)}\n")
# display results of name_parts
print(f"{' '.join(name_parts)}")

# close windows
outputFile.close()
