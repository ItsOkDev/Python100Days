print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
# Because we are Converting String to Integer (whole Num)

if height > 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# IndentationError
# Spacing in Python is Very important
# if height > 120:
# print("You can ride the roller coaster!")

if height >= 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
