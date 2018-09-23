"""
This is a funny game widly known as Rock, Paper, Scissors. 
"""
import random 
option=["ROCK","PAPER","SCISSORS"]
message={"tie":"opppss its a tie!","won":"yayyy you have won!!!","lost":"Awww you have lost!"}

def decide_winner(user_choice,computer_choice):     #here decide the winners 
  print ('your choice : %s' % user_choice)
  print ('computer\'s  choice: %s' % computer_choice)
  if  user_choice ==computer_choice:
    print (message["tie"])
  elif (user_choice ==option[0] and computer_choice==option[2]):
    print (message["won"])
  elif (user_choice ==option[1] and computer_choice==option[0]):
    print (message["won"])
  elif (user_choice ==option[2] and computer_choice==option[1]):
    print (message["won"])
  else: 
    print (message["lost"])
   
def play_RPS():
  user_choice=input('Enter Rock, Paper or Scissors:').upper() 
  computer_choice=random.choice(option)
  decide_winner(user_choice,computer_choice)
  
play_RPS()
