import time
from time import *
#1 megabyte = 8 megabit

file_size = int(input("Enter size of file in megabytes: "))
internet_speed = int(input("Enter speed of internet: "))

file_size  *=8
download_time = file_size/internet_speed

print("Time to complete download", download_time, "seconds")

countdown =round(download_time)
while countdown>0:
  print(countdown)
  countdown-=1
  sleep(1)
print("Download completed.!")
