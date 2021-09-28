#  Write a program to fill in a letter template given below with name and date:
# letter = ‘’’ Dear <|Name|>  You are selected <|Date|>’’’

# By - Meetali Jain
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

Name= input("Enter your name: ")
Date = input("Enter date: ")
print("Dear " +  Name + "\n You have selected" + "\n" + Date )

# OUTPUT:- 
# Enter your name: Meetali
# Enter date: 28/08/2021 
# Dear Meetali
# You have selected
# 28/08/2021