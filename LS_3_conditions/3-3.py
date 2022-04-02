# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("This is leap year")
        else:
            print("This year is not leap")
    else:
        print("This is leap year")
else:
    print("This year is not leap")