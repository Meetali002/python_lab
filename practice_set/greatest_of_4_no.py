# Write a program to find the greatest of 4 numbers entered by the user.

# By - Meetali Jain
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

maxno = []
print("Enter 4 number: ")
x=1
for i in range(4):
    maxno.append(int(input("number " + str(x) + " =")))
    x=x+1
print("Maximun number between 4 digit:", max(maxno))

# OUTPUT:-Enter 4 number: 
# number 1 =1
# number 2 =2
# number 3 =3
# number 4 =4
# Maximun number between 4 digit: 4