# Write a program to calculate the factorial of the given number.

# By - Meetali Jain 
# Date of Creation - 28-09-2021 
# Last Modified - 28-09-2021

num = int(input("Enter any positive Number: "))
fact=1
while(num>0):
    fact=fact*num;
    num -=1

print("Factorial of number = ", fact)

# OUTPUT:-Enter any positive Number: 6
#         Factorial of number =  720