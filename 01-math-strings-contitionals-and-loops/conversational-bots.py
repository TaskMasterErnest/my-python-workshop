"""
A program that has two conversational bots

First bot will ask the user questions and include the answers in follow-up questions

Second bot will ask questions that require numerical answers.
"""

# First bot
# question 1
print("What is your name?")
answer_1 = input()
# question 2
print("What is your favourite movie?")
answer_2 = input()
# response
print("Nice to meet you {}. We can watch {} sometime later.".format(answer_1, answer_2))

# Second bot
print("On a scale of 1 - 10, how good are you with a violin?")
answer_3 = abs(int(input()))
# response based on answer
if answer_3 < 3:
  print("Damn son, you need to start learning")
elif answer_3 < 6:
  print("That's incredible. Do better though lol!")
elif answer_3 < 9:
  print("Okay okay, you know something")
else:
  print('Maestro! or sonething like that.')