# import necessary libraries
from random import randint
import datetime
import os
import json

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
    json.dump(staff_data, f)

#define function to verify staff entry
def ver_user(username, password):
    with open("staff.txt", "r") as f:
        data = json.load(f)
        staff1_name = data['staff1']['Username']
        staff1_pass = data['staff1']['Password']
        staff2_name = data['staff2']['Username']
        staff2_pass = data['staff2']['Password']
        if (x == staff1_name and y == staff1_pass) or (x == staff2_name and y == staff2_pass):
            return True
        else:
            return False


#define function to generate account number
def gen_acc_num():

    length = 10
    random_acc_num = ''.join(["{}" .format(randint(0,9)) for i in range(length)])
    return random_acc_num


#define function to store user session in file
def store_sess(username):
    currentDT = datetime.datetime.now()
    with open("user_session.txt", "w") as ss:
        ss.write(f'{x}\t Last Login: {currentDT}')
    return "saved"


#define function to delete user session
def del_sess(username):
    file = open("user_session.txt","r+")
    for username in file:
        file.truncate(0)
        file.close
    return "deleted" 


#define a function to save customer data
cust_data = {}

def save_cust(acc_num, acc_name, open_bal, acc_type, acc_email):
    user_details = {
        acc_num : {"Account Name" : acc_name, "Opening Balance" : open_bal, "Account Type" : acc_type, "Account email" : acc_email}
    }
    cust_data.update(user_details)
    with open("customer.txt", "w") as s:
        json.dump(cust_data, s)
    return "saved"






# PROGRAM STARTS
status = True

while status:
    print("Please select (a/b):\n ")
    print("(a) Staff Login\n ")
    print("(b) Close App ")
    selection = input().lower()

    if selection == "a":
        status = False
        login = True
        while login:
            print("Please enter the following:\n ")
            x = input("Username: ")
            y = input("Password: ")

            if ver_user(x, y) is False:
                print("Invalid username or password. Try again")
                
            else:
                login = False
                status = True
                while status:
                    store_sess(x)
                    print("Please select (a/b/c):\n ")
                    print("(a) Create New Bank Account\n ")
                    print("(b) Check Account Details\n ")
                    print("(c) Logout ")
                    selection = input().lower()

                    if selection == "a":
                        print("Please enter the following:\n ")
                        acc_name = input("Account Name: ")
                        open_bal = input("Opening Balance: ")
                        acc_type = input("Account Type: ")
                        acc_email = input("Account email: ")

                        new_acc_num = gen_acc_num()
                        save_cust(new_acc_num, acc_name, open_bal, acc_type, acc_email)

                        print("Account successfully created! Your new account number is:\n " + new_acc_num)
                        

                    elif selection == "b":
                        check_details = True
                        while check_details:
                            print("Please enter account number:\n ")
                            acc_num = input()
                            with open("customer.txt", "r") as s:
                                data = json.load(s)
                                if acc_num in data:
                                    for key, value in data[acc_num].items():
                                        print(key, " : ", value)

                                    break
                                else:
                                    print("Invalid account number. Try again")

                    elif selection == "c":
                        #delete session file
                        del_sess(x)
                        print("Thank you for banking with us!")
                        status = False
                        quit

                    else:
                        print("Invalid input. Try again")
                   

    elif selection == "b":
        print("Thank you for banking with us!")
        status = False
        quit

    else:
        print("Invalid input. Try again")