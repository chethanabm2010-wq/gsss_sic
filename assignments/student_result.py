# Input marks for 3 subjects
name = input("Enter student name: ")
marks1 = int(input("Enter marks for Subject 1: "))
marks2 = int(input("Enter marks for Subject 2: "))
marks3 = int(input("Enter marks for Subject 3: "))

total = marks1 + marks2 + marks3
percentage = total / 3

print(f"\nStudent Name: {name}")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")

# Grade based on percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print(f"Grade: {grade}")
