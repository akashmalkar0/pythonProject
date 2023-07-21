from art import logo
from replit import clear
import random
from art import vs
from game_data import data

def information():
  win=True
  count=0
  B=random.choice(data)
  while win:
    print(logo)
    A=B
    B=random.choice(data)
    while A==B:
      B=random.choice(data)
    follower_A=int(A['follower_count'])
    follower_B=int(B['follower_count'])
    print(f"A person Details is\nName:{A['name']}\nDescription: {A['description']}\nCuntry: {A['country']} {vs} \n B person Details is\nName:{B['name']}\nDescription: {B['description']}\nCuntry: {B['country']} ")
    user_guess=input(f"Who has more Follower A: {A['name']} or B:{B['name']}\n").lower()
    clear()
    if user_guess=="a" and follower_A>follower_B:
      count+=1
      print("You Right")
    elif user_guess=="b" and follower_B>follower_A:
      count+=1
      print("You Right")
    else:
      print("you Wrong")
      win=False
    # clear()  
    print(f"Your Score is {count}")  
    

information()