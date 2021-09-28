# Write a program to print the sum of first n natural numbers using while loop.

#  By - Meetali Jain
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

number = int(input("Enter a positive number: ")) 
sum = 0
   
while(number > 0):
       sum += number
       number -= 1
print("The result is", sum)

# OUTPUT:- Enter a positive number: 12
#          The result is 78