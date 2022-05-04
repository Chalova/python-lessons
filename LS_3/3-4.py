# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Pepperoni for Medium or Large Pizza: +$3
cost = 0


if size == 'S':
    cost = 15
elif size == 'M':
        cost = 20
elif size == 'L':
        cost = 25

if add_pepperoni == 'y':
    if size == 'S':
        cost +=2
    else:
        cost +=3

if extra_cheese == 'y':
    cost +=1

print(f"Your cost is ${cost}")



