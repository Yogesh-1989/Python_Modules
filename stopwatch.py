
#Time module of python
#Stop watch code
from time import *

stop_watch = input("Enter 1 to start and 0 to end:")
while stop_watch!="0":
  
  if stop_watch=="1":
    start_timer = time()
  stop_watch=input("Enter 0 to end timer:")
  
end_timer = time()
total_time = end_timer - start_timer
updated_time = round(total_time, 2)

print("Total Time has been passed since start is:", updated_time,"sec")

point = 0
if updated_time < 10:
  point +=7
elif updated_time >=10 and updated_time  < 15:
  point+=3
else:
  point+=1
print("You were awarded: ", point, "points.!")