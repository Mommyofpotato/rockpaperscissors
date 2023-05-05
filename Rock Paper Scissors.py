#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


print("Welcome, lets Play!")


# In[26]:


def game():
    while True:
        play=input("Would You like to play Rock,Paper or Scissors?")
        play=play.lower()
        game=['rock','paper','scissors']
        computer=random.randint(0,2)
        computer_play=game[computer]
        if play=='rock':
            print("""   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\n You Played Rock""")
        elif play=='paper':
            print(""""    
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)\n You Played Paper""")
        elif play=='scissors':
            print("""    
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\n You Played Scissors""")
        else:
            print("I didn't understand that, check your spelling")
        if computer_play=='rock':
            print(""""   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\n Computer Played Rock""")
        elif computer_play=='paper':
            print(""""    
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)\n Computer Played Paper""")
        else:  
            print("""    
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\n Computer Played Scissors""")
        if play=='rock' and computer_play=='scissors':
            print('You Win!')
        if play=='scissors' and computer_play=='paper':
            print('You Win!')
        if play=='paper' and computer_play=='rock':
            print('You Win!')
        if computer_play=='rock' and play=='scissors':
            print('You Loose!')
        if computer_play=='scissors' and play=='paper':
            print('You Loose!')
        if computer_play=='paper' and play=='rock':
            print('You Loose!')
        answer = str(input('Run again? (y/n): '))
        if answer == 'y':
            continue
        elif answer=='n':
            print("Goodbye")
            break
        else:
            print("invalid input")
            break
        
        


# In[ ]:


game()


# In[ ]:




