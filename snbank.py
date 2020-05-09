# import necessary libraries
import numpy as np 
from random import randint
import datetime
import os

#create staff data 
staff_data = {
"staff1" : {
"Full Name" : "Lagbaja Nothing",
"Username" : "Lagbaja",
"email" : "lagbaja@ymail.com",
"Password" : "12345"
},

"staff2" : {
"Full Name" : "Fela Water",
"Username" : "Fela",
"email" : "fela@ymail.com",
"Password" : "98765"
}
}

#save staff data
with open("staff.txt", "w") as f:
    f.write('{} \n' .format(staff_data))

#define function to verify staff entry
def ver_user(a):
    with open("staff.txt", "r") as f:
        data = f.read()
        if a in data:
            return True
        else:
            return False

#define function to generate account number
def gen_acc_num():

    length = 10
    random_acc_num = ''.join(["{}" .format(randint(0,9)) for i in range(length)])
    return random_acc_num


#define function to store user session in file
def store_sess(x):
    currentDT = datetime.datetime.now()
    with open("user_session.txt", "w") as ss:
        ss.write(f'{x}\t Last Login: {currentDT}')
    return "saved"


#define function to delete user session
def del_sess(x):
    file = open("user_session.txt","r+")
    if x in file:
        file.truncate(0)
        file.close()

#define a function to save customer details
def save_cust(p, a,b,c,d):
    cust_details = {
        p + " details" : {"Account Name" : a, "Opening Balance" : b, "Account Type" : c, "Account email" : d}
    }
    with open("customer.txt", "w") as s:
        s.write('{}\n' .format(cust_details))
    return "saved"



# PROGRAM STARTS
print("Please select (a/b):\n ")
print("(a) Staff Login\n ")
print("(b) Close App ")
selection = input().lower()

while selection == "a":
    print("Please enter the following:\n ")
    x = input("Username: ")
    y = input("Password: ")

    if ver_user(x) or ver_user(y) is False:
        print("Invalid username or password. Please try again")
    else:
        store_sess()
        print("Please select (a/b/c):\n ")
        print("(a) Create New Bank Account\n ")
        print("(b) Check Account Details\n ")
        print("(c) Logout ")
        selection = input().lower()

        while selection == "a":
            print("Please enter the following:\n ")
            acc_name = input("Account Name: ")
            open_bal = input("Opening Balance: ")
            acc_type = input("Account Type: ")
            acc_email = input("Account email: ")

            new_acc_num = gen_acc_num()
            save_cust(new_acc_num, acc_name, open_bal, acc_type, acc_email)

            print("Account successfully created! Your new account number is:\n " + new_acc_num)
            break

        while selection == "b":
            print("Please enter account number:\n ")
            acc_num = input()
            with open("customer.txt", "r") as s:
                data = s.read()
                if acc_num in data:
                    print(data)
                    break
                else:
                    print("Invalid account number. Please try again")

        if selection == "c":
            #delete session file
            del_sess(x)
    break

if selection == "b":
    print("Thank you for banking with us!")
    quit