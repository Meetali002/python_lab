# Q. Write a program to check whether a username consists of less than 10 characters or not.

# By - Meetali Jain
# Date of Creation - 30-09-2021
# Last Modified - 30-09-2021

username = input("Enter your Username: ")
C = len(username)
if(C<10):
    print("Username contains less than 10 characters")
else:
    print("Username contains equal or more than 10 characters")

# Output :-     Enter your Username: meetalij002
#               Username cotains equal or more than 10 characters

#               Enter your Username: mj002
#               Username contains less than 10 characters