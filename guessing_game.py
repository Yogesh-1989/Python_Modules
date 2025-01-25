import random
from random import randint

guess = int(input("Enter a number between 1 and 10: "))

random_number = randint(1,10)
if guess < random_number:
  print("Guessing too low")
elif guess > random_number:
  print("Guess too high")

else:
  print("Congratulations, Correct guess: ")
   

