# Q. Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take  marks as an input from the user.

# By - Meetali Jain 
# Date of Creation - 30-09-2021
# Last Modified - 30-09-2021

mark = []
print("Enter 3 different marks : ")
x=1
for i in range(3):
    mark.append(int(input("sub " + str(x) + " marks =")))
    x=x+1
P = (sum(mark)/300)*100
print("percentage of students = ",P)

if (P>=40):
    # F=1
    for i in mark:
        if (i>=33):          
            continue
        else:
            print("Student Failed...")
            exit
else:
    print("Student Failed...")
    exit

# Output : Enter 3 different marks : 
#          sub 1 marks =77
#          sub 2 marks =89
#          sub 3 marks =86
# percentage of students =  84.0   
#          Enter 3 different marks : 
#          sub 1 marks =22
#          sub 2 marks =33
#          sub 3 marks =39
# percentage of students =  31.333333333333336
# Student Failed...