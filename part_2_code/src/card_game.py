### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

# I've done task 1, which was correcting the code by doing static testing

class CardGame:

# two == symbols are needed (one = is an assignment operator so 
# for like declaring a variable for example)
# after else there should be a colon : because that's how the syntax 
# is for if else statements in python
  def check_for_ace(self, card):
    if card.value == 1:
      return True
    else:
      return False


# it said dif so I changed it to do def as when you create a method in
# python you have to start it with def
  def highest_card(self, card1, card2):
        if card1.value > card2.value:
            return card1
        else:
            return card2
  
# the total variable is supposed to be set to 0 as it is the initialiser thing
# this means that total is at 0 but then whatever value is added to it 
# to make the new total amount
# I've put strings together and converted the total number to a string
# using that in built method
  def cards_total(self, cards):
        total = 0  
        for card in cards:
            total += card.value
        return "You have a total of" + " " + str(total)