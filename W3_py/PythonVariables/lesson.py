from traceback import print_tb


x = 5  # * it type is int
y = "Mounir"  # * it type is str
print(y)
print(x)

# * this is swap : )
z = x

x = y
y = z
# * after i change the value of variables it type change too
print(f"this is x: {x} and it type is :{type(x)}")
print(f"this is y: {y} and it type is : {type(y)}")

# * casting
float(y)
print(f"this is y: {y} and it type is : {type(y)}")

y = str(y)
print(f"this is y: {y} and it type is : {type(y)}")

y = float(y)
print(f"this is y: {y} and it type is : {type(y)}")

"""

Rules for Python variables:

    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores
    (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different
    variables)
    A variable name cannot be any of the Python keywords.

"""

# * assign multi variables on single line
a, b, c = "hello I am", 21, "years old"
print(a)
print(b)
print(c)

# * assign one value to multi variables
a = b = c = "value"

print(a)
print(b)
print(c)

# * unpack an collection
langs = ["ty", "js", "py"]
a, b, c = langs

print(a)
print(b)
print(c)

# * global variables is variable out side function


def sayMyPrectLang(c):
    print("my fav lang is :", c)


sayMyPrectLang(c)

def TestingGlobalVariable():
    global myFavIDE
    myFavIDE = "VSC"
    print(myFavIDE)
TestingGlobalVariable()
print(myFavIDE)