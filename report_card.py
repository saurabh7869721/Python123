
#studenr report card.

# Student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Marks input
math = int(input("Math marks: "))
science = int(input("Science marks: "))
english = int(input("English marks: "))

# Total & Percentage
total = math + science + english
percentage = total / 3

# Report Card
report = """
------ Report Card ------
Name      : {}
Roll No   : {}
Math      : {}
Science   : {}
English   : {}
Total     : {}
Percentage: {:.2f}%
""".format(name, roll_no, math, science, english, total, percentage)

print(report)




#student report using if elif  else.


name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
maths = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))
english = int(input("Enter English Marks: "))


total = maths + science + english
average = total / 3
percentage = (total / 300) * 100


if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "F"


print("\n_______report  card_______")

print(f"Name        :{name}")
print(f"Roll No     :{roll_no}")
print(f"Maths       :{maths}")
print(f"Science     :{science}")
print(f"English     :{english}")


print(f"Total       :{total}")
print(f"Average     :{average}")
print(f"Percentage  :{percentage:.2f}%")
print(f"Grade       :{grade}")


