'''print("Hello World")
'''

# Drawing a Shape

'''
print("   /|")
print("  / |")
print(" /  |")
print("/___|") # order of instructions matter a lot.
'''
# Variables and data types

# Working With Strings

'''
print("Pankaj \"Hello\" Academy")

phrase = "Pankaj Goswami"
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase[::2])
print(phrase.index("G"))
print(phrase.find("P"))
print(phrase.replace("Goswami","GoSu"))

'''

# Working With Numbers.

'''
print(-2)
print(3+4.5)
print(3**2)
print(3 * (4 + 5))

print(10%3) # To get reminder

my_num = 735
print(my_num)
x = -5
print(abs(x))
print(pow(3,3)) # 3^3
print(max(4,5,5,8))
print(min(4,5,5,8))
print(round(3.49))

from math import * # when we do this we importing all math functions so no need to do math.ceil or math.floor
# import math
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))
'''

# Getting Input from user
'''
name = input("Enter your name: ")

print(f"Hello {name} !")

'''

# Building a Basic Calculator
num1 = int(input("Enter Your First number : "))
num2 = int(input("Enter Your Second number : "))

operation = input("What operation you want to perform : ")
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
else:
    print("Check your inputs and try again")

