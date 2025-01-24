import random
from random import randint

passenger = input("Enter name of passenger: ")
while passenger!="quit":
  flight_number = randint(1,4)
  print(passenger, "Your flight number is: ", flight_number)
  
  passenger = input("Enter name of passenger: ")