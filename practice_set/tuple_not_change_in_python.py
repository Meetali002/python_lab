# Q. Check that a tuple cannot be changed in python.

# By - Meetali Jain 
# Date of Creation - 30-09-2021
# Last Modified - 30-09-2021

tuple= ("potato", "kapsikum", "onion")
# change onion to brocoli
tuple[2] = brocoli
print(tuple)

# Output : TypeError: 'tuple' object does not support item assignment