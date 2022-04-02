# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = name1.lower() + name2.lower()
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

true = t + r + u + e
love = l + o + v + e
total = true*10 + love

if total < 10 and total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >40 and total <50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(total)