"""This funny project will allow user to guess a number and will generate random by its won. If the both numbers match the user will win otherwise lose."""
from random import randint 
from time import sleep

def guess_the_number():                 #this function returns the user input.
  guess=int(input ("Guess your lucky number: "))
  return guess

def roll_dice(number_of_side):
  roll1=randint(1,number_of_side)       #generates the first random number.
  roll2=randint(1,number_of_side)       #generates the second random number.
  max_val=number_of_side*2
  print ('The maximum posiible value is  %d ' % max_val)
  guess=guess_the_number()
  if guess > max_val:
    print ('Guess a number not larger than %d' % max_val)
  else: 
    print ('Rolling the dice .....')
    sleep(2)
    print ('The first roll is : %d' %roll1)
    sleep(1)
    print ('The second roll is : %d' %roll2)
    sleep(1)
    total_roll= roll1+roll2
    print ("The total_rolling point is : %d" %total_roll)
    print ("Getting your result......")
    sleep(1)
    if guess==total_roll:
      print ("Hey you have won!!!!eeeeyyy")
    else: 
      print ("Sorry you have lost.Better luck next time.")
 
roll_dice (6)                           #calling the funciton 
  
