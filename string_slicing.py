#print username from email.
email=input("Enter your email:")

#find index number of @.
at_index=email.index("@")

#username.
username=email[:at_index]

#domain.
domain=email[at_index+1:]

print("username:",username)
print("domain:",domain)

#print date,month,year from customer_id.
customer_id="cust20241025A"
at=customer_id.index("2")

year=customer_id[at:at+4]
month=customer_id[at+4:at+6]
date=customer_id[at+6:at+8]

print("year:", year)
print("month:", month)
print("date:", date)

#change date format using slicing.

Date="2024-04-15"

date=Date[8:10]
month=Date[5:7]
year=Date[0:4]

print(date + "/", month  + "/", year)

#phine number masking(data privacy).

phone="8770584723"

result=phone[:3]+"****"+phone[-3:]

print(result)

#print file extension.

file = "sales_data_2025.csv"

extension = file[-3:]

print(extension)

#print name initials.

name = "saurabh shrivastava"

first, last = name.split()

initial = first[0] + last[0]

print(initial)

