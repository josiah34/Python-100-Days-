## Height
height = input ("What is your height in m? \n")

## Weight
weight = input ("What is your weight in kg? \n")

# Calculate bmi using the formula bmi = weight / height ** 2
# square can be calculated using ** 2, height * height or pow(height, 2)
bmi = int(weight) / float(height) ** 2

# Round the bmi to 2 decimal places
bmi = round(bmi, 2)

# Output the bmi
print(f"Your BMI is {bmi}.")


if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25 and bmi > 18.5:
    print("You are normal weight.")
elif bmi < 30 and bmi > 25:
    print("You are overweight.")
else :
    print("You are obese.")
