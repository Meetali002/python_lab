# Write a program to calculate the grade of a student from his marks of the following scheme:
# 90-100: Excellent
# 80-90: A
# 70-80: B
# 60-70: C
# 50-60: D
# Less than 50 : Fail

# By - Meetali Jain
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

mark = []
print("Enter 5 different marks : ")
x=1
for i in range(5):
    mark.append(int(input("sub " + str(x) + " marks =")))
    x=x+1
p = (sum(mark)/500)*100
print("percentage of students = ",p)

if ((p<=100) and (p>90)):
    print("Grade : Excellent")
elif ((p<=90) and (p>80)):
    print("Grade : A")
elif ((p<=80) and (p>70)):
    print("Grade : B")
elif ((p<=70) and (p>60)):
    print("Grade : C")
elif ((p<=60) and (p>50)):
    print("Grade : D")
else:
    print("Grade : Fail")


# OUTPUT:- Enter 5 different marks : 
#          sub 1 marks =45
#          sub 2 marks =80
#          sub 3 marks =90
#          sub 4 marks =76
#          sub 5 marks =88
# percentage of students =  75.8
# Grade : B
    
    
