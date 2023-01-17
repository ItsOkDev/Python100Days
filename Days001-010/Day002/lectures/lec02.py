# TypeError
# print(len(4837))

num_char = len(input("What is your name? "))

# TypeError
# print("Your name has " + num_char + " characters.")

# Len Functiom does not work in integers
# Error will Generater TypeError: can only concatenate str (not "int") to str
num_char = len(input("What ur Name>? "))
print("Your Name has " + num_char + "Characters.")
# your Name has = is a Strning num_char = is Integer so we cannot concinate it

# For Such Problems we use type( ) Function
# num_char = len(input("What ur Name>? "))
# print("Your Name has " + num_char + "Characters.")
# Converintg into string NOTE DOWN
num_char = len(input("What ur Nmae? "))
new_num_char = str(num_char)
print("Your Name has " + new_num_char + "Characters.")

print(type(num_char))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
print()

a = 123
print(type(a)) # We will get the Type like String, Int, Float 

a = str(123)
print(type(a))

a = float(123)
print(type(a))
print()

print(70 + float("100.5"))
print(str(70) + str(100))
