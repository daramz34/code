#COUNTDOWN TIMER
#note: learn how to use % properly
import time 
 
clock = int(input("Enter time in seconds: "))


for x in reversed(range(0,clock)):
    seconds = x % 60
    minutes =int( x / 60 ) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("time's up")