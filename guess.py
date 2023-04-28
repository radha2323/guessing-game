//importing random module
import random
import time       //time module
n=random.randrange(1,100)
print("welcome to the number guessing game:")
time.sleep(5)   // for delaying
guess=int(input("guess a number:"))
while(n!=guess):
  if(n>guess):
    print("too low")
    guess=int(input("guess again")
  elif(n<guess):
    print("too high")
    guess=int(input("guess again")
  else:
     break
print("***you nailed it!***")
    
