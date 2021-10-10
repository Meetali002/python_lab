# Q. Can you change the values inside a list which is contained in set S?  S = {8,7,12,”Simarjeet”,[1,2]}

# By - Meetali Jain 
# Date of Creation - 10-10-2021
# Last Modified - 10-10-2021

S = [8,7,12,"Simarjeet",[1,2]]
S[4]="Meetali Jain"
S[0]=9
print("Changed list = ",S)

# Output : Changed list =  [9, 7, 12, 'Simarjeet', 'Meetali Jain']