import random

def numGuess():
  num = random.randint(1,51)
  for i in range(6):
    guess = input('Guess the correct number between 1 and 100.')
    if guess > num:
      print('That is too high.')
    elif guess < num:
      print('That is too low.')
    else:
      print('Wow, good guess.')
  print('The number was ' + str(num))

numGuess()
