# Write a program to print multiplication table for a given number using for as well as while loop

# By - Meetali Jain 
# Date of Creation - 28-09-2021 
# Last Modified - 28-09-2021

num = int(input("Enter Number: "))
print("Table of " + str(num) + " =")
while(num>0):
        for i in range(1,11):
                print(num, 'x', i, '=', num*i)
        break

# Output:- Enter Number: 5
#          Table of 5 
#          5 x 1 = 5   
#          5 x 2 = 10  
#          5 x 3 = 15  
#          5 x 4 = 20  
#          5 x 5 = 25
#          5 x 6 = 30
#          5 x 7 = 35
#          5 x 8 = 40
#          5 x 9 = 45
#          5 x 10 = 50