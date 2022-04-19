# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
index = int( weight / height ** 2)
print(index)
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
if index < 18.5:
    print(f"Your BMI is {index}, you are underweight.")
elif index < 25:
    print(f"Your BMI is {index}, you are normal weight.")
elif index < 30:
    print(f"Your BMI is {index}, you are slightly overweight.")
elif index < 35:
    print(f"Your BMI is {index}, you are obese.")
else:
    print(f"Your BMI is {index}, you are clinically obese.")
