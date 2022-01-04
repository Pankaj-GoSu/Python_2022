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
phrase =phrase.replace("Goswami","GoSu")
print(phrase)
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

'''
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

'''

# Mad libs Game

# Lists

'''
friends = ["Kaushal","Bhanu","Kakku"]
print(friends[-1])

print(friends.index("Kaushal"))
'''
# List Functions

'''
friends = ["Kaushal","Bhanu","Kakku"]
numbers = [2,3,5,4,6]
print(friends)
# Adding Two List 
friends.extend(numbers) # This function is used for appending one list in other list.
print(friends)
list2 = [ 6,7,8]
friends.append(list2)
print(friends)

friends.insert(1, "Pankaj")
print(friends)
friends.remove(2)
print(friends)
friends.pop() # pop out the last element
print(friends.count(2))
#==> To reset List or clear list 
numbers.sort()
print(numbers)
# friends.clear()
# print(friends)

# Reversing a list
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)
'''

# Tuples
'''
tuple1 = (1,2,3)
coordinates = (4,5) # inmutable it means we can not modify it.

print(coordinates[0])

coordinates1 = [(4,5),(6,7),(7,8)]
print(coordinates1)
'''

# Functions

'''
def say_hi(name,age):
    print(f"Hello {name} you are {age}")

say_hi("Pankaj" ,25)
'''

# Return Statement

'''
def cube(num):
    return num**3

print(cube(5))
'''

# If Statements

'''
is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a male")
elif is_male and not(is_tall):
    print("You are male but not tall")
elif not(is_male) and is_tall:
    print("You are not male but you are tall")
else:
    print("You are not a male")

'''

# If Statements And Comparisons

'''
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(6,8,9)) 

'''

# Dictionaries (Key Value Pairs)
'''
monthConversion = {
    "jan":"January",
    "Feb":"February",
    "Mar": "March" ,
    "Apr" : "April"
}
# monthConversion["jan"] = "Hello"
print(monthConversion.get("jan","Not a valid key") )
'''

# While Loop
'''
i = 1
while i <= 10 :
    print(i)
    i += 1

print("Done with loop")
'''

# Basic Guessing Game
'''
secret_word = "GoSu"
guess = ""
i = 0
while guess != secret_word and i < 3:
    guess = input(" Enter guess : ")
    i += 1
if i == 3 and guess != "GoSu":
    print("Out of Guess")


else:
    print("You Win!")

'''

# For Loop 

'''
for letter in "Pankaj Academy":
    print(letter)


friends = [1,2,3]
for frd in friends:
    print(frd)

for index in range(10,5,-1):
    print(index)

for index, item in enumerate(friends):
    print(index,item)

'''

# Exponent Function
'''
# print(2**3)
num1 = 1
num = 2
for i in range(4):
    num1 = num1*num
print(num1)

'''

# 2D Lists And Nested Loops

'''
number_grid = [
    1,
    2,
    3,
    4
]

number_grid1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

# print(number_grid1[3][0])

for row in number_grid1:
    for col in row:
        print(col)

'''

# Build a Translator

'''
# Pankaj Language

# vowels -> g 
# Like dog ->dgg
# cat -> cgt
word = input("Enter a Word ")
for i in word:
    if i == "a" or i == "e" or i =="i" or i =="o" or i == "u":
        word = word.replace(i,"g")
print(word)

'''

# Comments



