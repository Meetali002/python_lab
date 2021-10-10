# Q. Write a program to greet all the person names stored in a list L1 and which starts with S. (hint: use startswith("S") method)   L1 = [“Simarjeet”, “Sohan”, “Sachin”, “Rahul”]

# By - Meetali Jain
# Date of Creation - 10-10-2021
# Last Modified - 10-10-2021

L1 = ["Simarjeet", "Sohan", "Sachin", "Rahul"]

for i in L1:
    if i.startswith('S'):
        print("Hello ",i)


# Output : Hello  Simarjeet
#          Hello  Sohan
#          Hello  Sachin