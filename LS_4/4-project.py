import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
list1 = [rock, paper, scissors]
my_choice = int(input("What will I choose? 1, 2 or 3? "))
print(list1[my_choice - 1])
comp_choice = random.randint(1, 3)
print(list1[comp_choice - 1])


if (my_choice == 1 and comp_choice == 3) or (my_choice == 2 and comp_choice ==1) or (my_choice == 3 and comp_choice == 2):
    print("I win!")
elif my_choice == comp_choice:
    print("Draw!")
else:
    print("Comp wins!")


