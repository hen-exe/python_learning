#Python3 "print" statement is a function.
#Indentation for blocks instead of curly braces (4 spaces)

# Data Types
# - object oriented, not statically typed
# - simple operators can be executed on numbers and strings
# int, float, str, bool


# Lists
# - contains any type of variable
# - can be iterated over

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

for x in mylist:
    print(x)
    print(mylist)

# Conditions
x = 1
y = 10
w = True

if (y % 2 == 0):
    print("even number")
elif (y == 2):
    print("y is equal to %d" % y)
else:
    print("not an even number")

# numpy
# - perform calculations across entire arrays

import numpy as np 

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_weight_kg = np.array(weight_kg)

np_weight_lbs = np_weight_kg / 2.2

print(np_weight_lbs)


# pandas
# - data manipulation tool
# - DataFrames allow you to store and manipulate tabular data in rows of observations & columns of variables

import pandas as pd 

dict = {
    "Country": ["Philippines", "America", "Italy", "Mexico"],
    "Capital": ["Manila", "Washington DC", "Rome", "Mexico City"],
    "Area": ["6.516", "12.10", "3.824", "1.212"],
    "Population": ["200.4", "143.5", "1345", "2314"]
}

locs = pd.DataFrame(dict)
print(locs)

locs.index = ["PH", "USA", "IT", "MX"]
print(locs)

# importing csv
days = pd.read_csv(r"C:\Users\flora\OneDrive\Desktop\elinnov\Code\python_learning\day.csv", index_col=0)
                   
print (days)

print(days['Numeric-Suffix'])

print(days[0:10])