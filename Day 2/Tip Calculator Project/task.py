# Ask what the bill amount is ie 150 - input level
# Ask how many people are splitting the bill ie 5 - input level
# Ask how much they are tipping ie 10%, 12% or 15% ie 12 - input level
# final bill - Amount = (150/5)* (12/100) - calculation
# Display - Each person will pay {amount}

print("Welcome to the tip calculator!")
total_bill = input("How much is the total bill? \n $")
tip = input("What percentage of the total bill would you like to tip, 10 , 12  or 15\n")
number_of_people = input("How many people are splitting the total bill\n")
total_amount = (int(total_bill)+ ((int(tip)/100)* int(total_bill)))/int(number_of_people)
Final_amount = round(total_amount,3)
print(f"Each person should pay {Final_amount} dollars")



