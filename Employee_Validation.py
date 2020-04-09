#import necessary librabries
import string
import random

#a function to generate random password (from first two and last two characters of first_name and last_name respectively, as well as a random 5 letter string)
def get_password(details):
    characters = string.ascii_letters
    length = 5
    random_string = ''.join(random.choice(characters) for i in range(length))
    password = details[0][0:2] + details[1][-2:] + random_string

    return password

# PROGRAM BEGINS
status = True

container = {}
user_id = 1

while status:
    #get user details 
    first_name = input("Please enter your First Name: ")
    last_name = input("Please enter your Last Name: ")
    email = input("Please enter your email: ")

    #store details as list
    details = [first_name, last_name, email]

    

    #display generated password 
    new_password = get_password(details)
    print("Your new password is: " + new_password)

    #get satisfaction/unsatisfaction feedback 
    password_like = input("Satisfied with it? (Yes/No): ")

    if (password_like == "Yes"):
        #add password to details
        details.append(new_password)

        #add details to container
        container.update({user_id : details})

    else:
        #get password from user
        user_password = input("Enter a password longer or equal to 7: ")    

        #validate password
        password_len = True
        while password_len:
            if (len(user_password) >= 7):

                #add user password to details
                details.append(user_password)

                #add user details to Container
                container.update({user_id : details})


                password_len = False

            else:
                user_password = input("Please enter a password longer or equal to 7: ")

    #enter new user
    new_user = input("Would you like to enter a new user? (Yes/No): ")

    #no new user
    if (new_user == "No"):
        status = False

        #print out user details nicely
        for user_id in container:
            print (user_id, container[user_id])

    else:
        status = True
        user_id += 1


