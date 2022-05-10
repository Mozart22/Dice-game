import random
import os
import time

locked = True

while locked:

 username = input("Please enter your username ")
 password = input("Please enter your password ")

 if username == "sba" and password == "007":
  locked = False
  print ("Welcome sba!")
 else:
   print ("Password or Username incorrect")



locked2 = True

while locked2:

 username2 = input("Player 2 please enter your username ")
 password2 = input("Player 2 please enter your password ")

 if username2 == "abc" and password2 == "123":
  locked2 = False
  print ("Welcome abc!")
 else:
   print ("Password or Username incorrect")

player1points = 0
player2points = 0

rounds = 1
while rounds <=5:
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  print (f'round {rounds}')
  player1points = dice1+ dice2
  print (f"Player one has {player1points}")
  player2points = dice1+ dice2
  print (f"Player two has {player2points}")
  print ('..........................')

  
  
  rounds +=1
  
if dice1 == dice2:
  print ('add another roll')
elif (dice1 + dice2) % 2 ==0:
  print ('even')
else:
  print ('odd')

