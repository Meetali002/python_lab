# Q. Write a program to find out whether a given name is present in a list or not.

# By - Meetali Jain 
# Date of Creation - 30-09-2021
# Last Modified - 30-09-2021

Names = ["Prateek","Pragya","Ishita","Manasvi","Prathmesh","Abhishek",]
X = input("Enter Name to search: ")

if(X in Names):
    print("Name is Present in list...")
    exit
else:
    print("Name is not Present in list...")

# Output :    Enter Name to search: Meetali
#             Name is not Present in list...

#             Enter Name to search: Manasvi
#             Name is Present in list...