## This program asks the user for a number and then prints out whether it is even or odd.


## Loop until the user enters a valid number
while True:
    try:
        num = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Please enter an integer number")

## Check if the number is even or odd
if type(num) == int:
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")