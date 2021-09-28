# Write a program to sum a list with 4 numbers.

# By - Meetali Jain
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

num = []
print("Enter 4 numbers: ")
x=1
for i in range(4):
    num.append(int(input("Num " + str(x) + " =")))
    x=x+1

print("Sum of all 4 numbers = ",sum(num))

# OUTPUT:- Enter 4 numbers: 
# Num 1 =40
# Num 2 =56
# Num 3 =112
# Num 4 =240
# Sum of all 4 numbers =  448