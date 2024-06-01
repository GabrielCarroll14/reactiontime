import time
import random
import keyboard

def main():
    
    randomnum = random.randint(1,3)
    
    print ("Press h when hi pops up")
    time.sleep(randomnum)
    print("hi")
    
main()