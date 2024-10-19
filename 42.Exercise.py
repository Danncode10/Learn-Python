# import random

# name = str(input("Enter List of Names Seperated by Commas: "))
# nameList = name.split(",")
# size = len(nameList)

# pick = random.randint(0,size-1)

# print(nameList[pick])

import random

name = str(input("Enter List of Names Seperated by Commas: "))
nameList = name.split(",")

payer = random.choice(nameList)
print(payer)



