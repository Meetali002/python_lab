# python program to detect double spaces

# By - Meetali Jain
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021


string = input("Enter String: ")
res = "  " in string
print("Does string contain double space ? " + str(res))

# OUTPUT:- Enter String: Meetali Jain
# Does string contain double space ? False
# Enter String: Meetali  Jain 
# Does string contain double space ? True
