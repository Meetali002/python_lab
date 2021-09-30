# Q. Write a program to print the following star pattern:
#       *
#      * *
#     * * *   for n = 3

# By - Meetali Jain
# Date of Creation - 30-09-2021
# Last Modified - 30-09-2021

def pattern(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
 
n = 3
pattern(n)

# Output :      *   
#              * *  
#             * * *