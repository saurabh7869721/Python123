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

