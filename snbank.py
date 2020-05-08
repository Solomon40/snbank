# import necessary libraries
import numpy as np 
from random import randint

#create staff data
staff1 = [
"Lagbaja Nothing",
"Lagbaja",
"lagbaja@ymail.com",
"12345"
]

staff2 = [
"Fela Water",
"Fela",
"fela@ymail.com",
"98765"
]

#save staff data
with open("staff.txt", "w") as f:
    f.write('{} {}\n' .format(staff1, staff2))

#define function to verify staff entry
def ver_user(a):
    with open("staff.txt", "r") as f:
        data = f.read()
        if a in data:
            return True
        else:
            return False

#define function to generate account number

#define function to store user session in file


# PROGRAM STARTS
print("Please select (a/b):\n ")
print("(a) Staff Login\n ")
print("(b) Close App ")
selection = input().lower()

if selection == "a":
    print("Please enter the following:\n ")
    x = input("Username: ")
    y = input("Password: ")

    if ver_user(x) or ver_user(y) is False:
        print("Invalid username or password. Please try again")
    else:
