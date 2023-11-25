"""
A program to prompt a user to bid on real estate and returns a response as to whether bid has been accepted or not.
"""

# prompt user
print("A studio apartment in Accra has been listed at $599,000")
print("Enter your offer for the apartment: ")
# make offer a positive 
offer = abs(int(input()))

# set best offer
print("Enter your best offer currently for the apartment:")
best = abs(int(input()))

# prompt for increments
print("How much more do you want to offer each time?")
increment = abs(int(input()))

# start bidding wars
offer_accepted = False
add_increment = False

while offer <= best:
  # if offer is greater than 650000, they get the apartment
  if offer >= 650000:
    offer_accepted = True
    print("Your offer of ${} has been accepted".format(offer))
    break
  else: 
    print("Your offer of ${} has not been accepted. Get your money up mah gee!".format(offer))
    print("Wunna bid some more? (y/N)")
    answer = str(input())
    if answer == "y":
      offer += increment
    elif answer == "n":
      print("Well that's all, you bum. Go home!")
      break