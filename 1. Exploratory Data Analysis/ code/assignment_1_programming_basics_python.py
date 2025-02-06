# -*- coding: utf-8 -*-
"""Assignment_1 Programming Basics - Python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EtV8apDqXqyXG4DI-2FoXntYIAyPvvCY

# Assignment_1 Programming Basics - Python

## Create a matrix with three rows A, B and C and four columns with names Q, W, E and R. Fill the matrix with any numbers between 1 and 10.
"""

import numpy as np
import pandas as pd

mat = np.random.randint(1, 11, size=(3, 4))
mat_df = pd.DataFrame(mat, index=['A', 'B', 'C'], columns=['Q', 'W', 'E', 'R'])
print(mat_df)

"""## x = 24, y =”Hello World”, z = 93.65. Identify the class of x, y and z and convert all three into factor."""

x = 24
y = "Hello World"
z = 93.65

print (type(x))
print (type(y))
print (type(z))

factor_x = str(x)
factor_y = str(y)
factor_z = str(z)

print (type(factor_x))
print (type(factor_y))
print (type(factor_z))

"""## q = 65.9836 a. Find square root of q and round it up to 3 digits. b. Check if log to the base 10 of q is less than 2."""

import math

q = 65.9836
sqrt_q = round(math.sqrt(q), 3)
sqrt_q

print("Is log10(q) less than 2?:", (math.log10(q) < 2), "\n")

"""##  x = c(“Intelligence”, “Knowledge”, “Wisdom”, “Comprehension”) y = “I am” z = “intelligent” a. Find first 4 letters of each word in x. b. Combine y and z to form a sentence “I am intelligent” c. Convert all the words in x to upper case."""

x = ["Intelligence", "Knowledge", "Wisdom", "Comprehension"]
first_4_letters = [word[:4] for word in x]
first_4_letters

y = "I am"
z = "intelligent"
sentence = y + " " + z
sentence

x_upper = [word.upper() for word in x]
x_upper

"""## a = c(3,4,14,17,3,98,66,85,44) Print “Yes” if the numbers in ‘a’ are divisible by 3 and “No” if they are not divisible by 3 using ifelse()."""

a = [3, 4, 14, 17, 3, 98, 66, 85, 44]
for item in a:
  if item % 3 == 0:
    print(item, "Yes")
  else:
    print(item, "No")

"""## b = c(36,3,5,19,2,16,18,41,35,28,30,31) List all the numbers less than 30 in b using for loop."""

b = [36, 3, 5, 19, 2, 16, 18, 41, 35, 28, 30, 31]
numbers_less_than_30 = []

for item in b:
    if item < 30:
        numbers_less_than_30.append(item)

numbers_less_than_30

"""## Date = “01/30/18” a) Convert Date into standard date format (yyyy-mm-dd) and name it as Date_new. b) Extract day of week and month from Date_new. c) Find the difference in the current system date and Date_new."""

from datetime import datetime

date_str = "01/30/18"
Date_new = datetime.strptime(date_str, "%m/%d/%y").date()
print(Date_new)

day_of_week = Date_new.strftime("%A")
month = Date_new.strftime("%B")
print(day_of_week, month)

current_date = datetime.now().date()
date_difference = current_date - Date_new
print(date_difference.days)

