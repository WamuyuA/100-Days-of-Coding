print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you?"))
    if age <= 12:
        print("Make a 7$ payment at the cashier")
    elif age <= 18: #has to have a semicolon after the statement not at the end of elif command
        print("Make a 10% payment at the cashier")
    else:
        print("Make a 18$ payment at the cashier ")
else:
    print("Sorry you have to grow taller before you can ride.")
