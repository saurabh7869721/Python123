# Number pattern printer using end parameter


num=int(input("Enter number:"))

for i in range(1,num+1):

    print(i, end=("  "))


#multiplication table printer.


num=int(input("Enter number:"))

for i in range(1,11):
    print(num*i, end=(" "))
