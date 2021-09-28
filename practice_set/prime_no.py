# Write a program to check whether a number is prime or not.

#  By - Meetali Jain
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

num= int(input("Enter the number :" ))
if (num > 1):
 
    for i in range(2, int(num/2)+1):
 
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
 
else:
    print(num, "is not a prime number")

# OUTPUT:- Enter the number :45
# 45 is not a prime number
# Enter the number :13
# 13 is a prime number