"""
Learning about type casting and all that
"""
# # Ask a question
# print("What is your name?")
# # ask for input from user
# name = input()
# # print the user's name
# print("Hello, " + name + ".")

# ask user aboout their day
print("How was your day?\nRate it from 1 - 10")

# take in value
rate = int(input())

# display message
if rate < 5:
  print("Man, {}?, that was harsh. I hope you get a better one next time.".format(rate))
elif rate == 5:
  print("Damn son, {}? That was not soo bad after all eh?".format(rate))
else:
  print("Holy cow, {}? That was a mighty good day innit?".format(rate))