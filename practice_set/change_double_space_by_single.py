# Replace double spaces with single spaces in previous program

# By - Meetali Jain
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

string = input("Enter String - ")
while "  " in string:
   string=string.replace("  "," ") 
print( string)

# OUTPUT:-Enter String - Meetali  Jain
# Meetali Jain