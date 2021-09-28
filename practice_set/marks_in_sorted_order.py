# Write a program to enter marks of 6 students and display them in sorted order.

# By - Meetali Jain
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

marks = []
print("Enter marks of 6 students: ")
for i in range(6):
    marks.append(input("Enter marks: "))

  print("unsorted marks =")
  print(marks)

marks.sort()
  print("sorted marks = ")
  print(marks)


# Output: Enter marks of 6 students: 
# Enter marks: 12
# Enter marks: 54
# Enter marks: 82
# Enter marks: 91
# Enter marks: 45
# Enter marks: 30
# unsorted marks =
# ['12', '54', '82', '91', '45', '30']
# sorted marks =
# ['12', '30', '45', '54', '82', '91']