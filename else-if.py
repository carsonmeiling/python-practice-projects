# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to5 , print Not Weird
# If  is even and in the inclusive range of 5 to 20 , print Weird
# If  is even and greater than 20 , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.


# def evenOdd(n):
#   if (n % 2) == 0 and (2 <= n <= 5):
#     print('Not Weird')
#   elif (n % 2) == 0 and (5 <= n <= 20):
#     print('Weird')
#   elif (n % 2) == 0 and (n >= 20):
#     print('Not Weird')
#   elif (n % 2) != 0:
#     print('Weird')
#   else:
#     print(n)

# evenOdd(3)
# evenOdd(29)

# for i in range(0,1000):
#   evenOdd(i)

# print(a+b)
# print(a-b)
# print(a*b)

# print(int(a/b))
# print(float(a/b))

# for i in range(0,n):
# #   print i**2
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

# def is_leap(year):
#     leap = False
    
#     # Write your logic here
    
#     if (year % 4 == 0) and (year % 100 != 0): 
#       # Note that in your code the condition will be true if it is not..
#       leap = True
#     elif (year % 100 == 0) and (year % 400 != 0):
#       leap = False
#     elif (year % 400 == 0):
#       # For some reason here you had False twice
#       leap = True
#     else:
#       leap = False

#     return leap


# print(isinstance(100, int))

# num = ''
# for i in range(6):
#   num = num + str(i)
#   print(num)
  

# import xml.etree.ElementTree as etree

# def get_attr_number(node):
#   count = 0
#   for tag in node:
#     count = count + get_attr_number(tag)
#   return count 
    # your code goes here
# arr = [8,5,3,4,5]
# arr.sort(reverse=True)
# x = max(arr)
# for i in len(arr):
#     if arr[i] == x:     
#         arr.remove(x)
        
# print(max(arr))
        # print('else')

# content = open('content_file', 'a')
# content.write('Hello World')

import xlrd 

loc = ('practice.xlsx')
content = xlrd.open_workbook(loc)
sheet = content.sheet_by_index(0)

print(sheet.cell_value(0,0))