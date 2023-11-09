# define and set variables from user input (casted to a float)
bill = float(input("How much is the meal? "))
tax = float(input("What is the sales tax (percentage)? "))
tip = float(input("What is the tip (percentage)? "))

# calculate and add tax
tax_amount = (bill * tax) / 100  # calculate the tax amount
total = bill + tax_amount   # add tax and bill total to final bill

# calculate and add tip
tip_amount = (total * tip) / 100   # calculate the tip
total = total + tip_amount   # add tip to the final total

# round the toal to 2 decimal points
total = round(total, 2) # round the total amount to 2 decimal points

# print the final amount
print("The toal bill is $", total, sep = "")
