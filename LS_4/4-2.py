# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

person = random.randint(0, len(names)-1)
print(f"{names[person]} is going to buy the meal today!")