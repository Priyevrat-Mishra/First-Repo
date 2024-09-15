# Game:Rock,Paper,Scissor
import random

''' 
r p w 1 -1
r s w 1 0
p r l -1 1
p s l -1 0 
s r l 0  1
s p w 0 -1
'''
comp=random.choice([0,1,-1])
ustr=input("Your Turn: ")
udict={"r":1,"p":-1,"s":0}
revdict={1:"rock",-1:"paper",0:"scissor"}
u=udict[ustr]
print(f"you choose {revdict[u]} and computer chose {revdict[comp]}")

if(u==comp):
  print("it's a draw")
else:
  if(u==1 and comp==0):print("u won")
  elif(u==1 and comp==-1):print("u won")
  elif(u==0 and comp==1):print("u loose")
  elif(u==0 and comp==-1):print("u won")
  elif(u==-1 and comp==0):print("u loose")
  elif(u==-1 and comp==1):print("u loose")
  else:print("Error!")