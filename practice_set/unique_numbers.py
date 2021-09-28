#Write a program to input 8 numbers from the user and display all the unique numbers (once).

# By - Meetali Jain 
# Date of Creation - 28-09-2021 
# Last Modified - 28-09-2021

numbers = []
while(len(numbers)<8):
    numbers.append(input("Enter Number : "))
    
print(set(numbers))

# OUTPUT:-Enter Number : 12
#         Enter Number : 12
#         Enter Number : 45
#         Enter Number : 36
#         Enter Number : 44
#         Enter Number : 45
#         Enter Number : 84
#         Enter Number : 16
# {'12', '44', '45', '84', '36', '16'}