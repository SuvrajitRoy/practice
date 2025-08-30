# import math

# num = float(input("Enter a number: "))
# sqrt = math.sqrt(num)

# print("The square root of", num, "is", sqrt)

#print("Hello, World!")  #This is a comment

# x = 5.786
# y = "John"
# print(x)
# print(y)

# x = 5
# y = "John"
# print(type(x))
# print(type(y))

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# Function to calculate grade
def calculate_grade(avg):
    if avg >= 80:
        return "A+"
    elif avg >= 70:
        return "A"
    elif avg >= 60:
        return "A-"
    elif avg >= 50:
        return "B"
    elif avg >= 40:
        return "C"
    elif avg >= 33:
        return "D"
    else:
        return "F"

# Input section
name = input("Enter student's name: ")
roll = input("Enter roll number: ")

subjects = ["Bangla", "English", "Math", "Science", "ICT"]
marks = []

for subject in subjects:
    score = float(input(f"Enter marks for {subject}: "))
    marks.append(score)

# Calculation
total = sum(marks)
average = total / len(subjects)
grade = calculate_grade(average)

# Result Sheet Output
print("\n========== RESULT SHEET ==========")
print(f"Name      : {name}")
print(f"Roll No   : {roll}")
print("----------------------------------")
for i in range(len(subjects)):
    print(f"{subjects[i]:<10}: {marks[i]}")
print("----------------------------------")
print(f"Total     : {total}")
print(f"Average   : {average:.2f}")
print(f"Grade     : {grade}")
print("==================================")
