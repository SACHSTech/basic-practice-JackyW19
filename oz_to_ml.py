
print("****** Welcome to the Oz to ml Converter ******")

# get amount of fluid from the UserWarning
amount_of_fluid = int(input("Enter the amount of fluid in ounces: "))
number_of_servings = int(input("Enter the amount of people to serve: "))

# compute the ounces of fluids to milliliters
ml_in_a_oz = 29.57
amount_of_ml = (amount_of_fluid * ml_in_a_oz)

# output the number amount_of_ml to the UserWarning
print(f"you will need {amount_of_ml} ml")
