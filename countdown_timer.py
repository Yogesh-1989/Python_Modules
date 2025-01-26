from time import *

countdown_start = int(input("Enter a starting number: "))
countdown = countdown_start

while countdown > 0 :
  print(countdown)
  countdown-=1
  sleep(1)
  
print(" Your contdown finished after", countdown, "Seconds")