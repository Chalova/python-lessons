# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

sum_height = 0
n = 0
#Write your code below this row 👇
for height in student_heights:
    sum_height += height
    n += 1

avg = int(sum_height / n)
print(avg)