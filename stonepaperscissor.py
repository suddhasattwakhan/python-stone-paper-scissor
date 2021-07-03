import random

rock= '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissor= '''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper= '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
flag=1
while(flag==1):
 num = int(input("Enter 1 for Rock,2 for scissor, 3 for paper\n"))
 if num==1:
    print("So you chose Rock\n")
    print(rock)
 elif num==2:
    print("You chose scissor\n")
    print(scissor)
 else:
    print("You chose paper\n")
    print(paper)
 ai_number= random.randint(1,3)
 if ai_number==1:
    print("The computer chose rock\n")
    print(rock,"\n")
 elif ai_number==2:
    print("The computer chose scissor\n")
    print(scissor,"\n")
 else:
    print("The computer chose paper\n")
    print(paper,"\n")
 if(ai_number==num):
    print("There is a draw\n")
 elif ai_number==1 and num==2:
    print("You lost\n")
 elif ai_number == 1 and num == 3:
    print("You win\n")
 elif ai_number==2 and num==1:
    print("You win\n")
 elif ai_number==2 and num==3:
    print("You lost\n")
 elif ai_number== 3 and num==1:
    print("You lost\n")
 else:
    print("You won\n")
 playagain= int(input("Do you want to play again?\n press1 for yes and 2 for no\n"))
 if playagain==1:
    flag=1
 elif playagain==2:
     flag=2
     break







