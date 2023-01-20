#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

## Get the bill amount

bill = float(input("What was the total bill? $\n"))

## Get the tip percentage

percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

## Get the number of people

people = int(input("How many people to split the bill?\n"))


total_per_person = (bill + (bill * percentage / 100)) / people

print(f"Each person should pay: ${total_per_person:.2f}")

