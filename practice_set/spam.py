# Q. A spam comment is defined as a text containing following keywords: “buy now” , “make a lot of money”, “subscribe this”, “click this”. Write a program to detect these spams (hint: use ‘in’).

# By - Meetali Jain
# Date of Creation - 10-10-2021
# Last Modified - 10-10-2021

spamw = input("Enter your comment: ")    

if 'buy now' in spamw:
    print("Spam word detected : 'buy now'")
else:
    print("Spam word not detected : 'buy now'")


if 'make a lot of money' in spamw:
    print("Spam word detected : 'make a lot of money'")
else:
    print("Spam word not detected : 'make a lot of money'")
    

if 'subscribe this' in spamw:
    print("Spam word detected : 'subscribe this'")
else:
    print("Spam word not detected : 'subscribe this'")


if 'click this' in spamw:
    print("Spam word detected : 'click this'")
else:
    print("Spam word not detected : 'click this'")


# Output  :   Enter your comment: its an amazing shoe shop click this and buy now
#             Spam word detected : 'buy now'
#             Spam word not detected : 'make a lot of money'
#             Spam word not detected : 'subscribe this'
#             Spam word detected : 'click this'