# This program determines the love compatibility between two people 

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.


name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2

true_score = (combined_string.lower().count("t") + combined_string.lower().count("r") + combined_string.lower().count("u") + combined_string.lower().count("e"))
love_score = (combined_string.lower().count("l") + combined_string.lower().count("o") + combined_string.lower().count("v") + combined_string.lower().count("e"))

total_love_score = int(str(true_score) + str(love_score))


if total_love_score < 10 or total_love_score > 90:
  print(f"Your score is {total_love_score}, you go together like coke and mentos.")
elif total_love_score >= 40 and total_love_score <= 50:
  print(f"Your score is {total_love_score}, you are alright together.")
else:
  print(f"Your score is {total_love_score}.")


