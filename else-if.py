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


def evenOdd(n):
  if (n % 2) == 0 and (2 <= n <= 5):
    print('Not Weird')
  elif (n % 2) == 0 and (5 <= n <= 20):
    print('Weird')
  elif (n % 2) == 0 and (n >= 20):
    print('Not Weird')
  elif (n % 3) == 0:
    print('Weird')
  else:
    print(n)

# evenOdd(3)
# evenOdd(24)

for i in range(0,1000):
  evenOdd(i)