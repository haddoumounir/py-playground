# Arithmetic Operators
print("Arithmetic Operators")
# * Addition operator +
print(5 + 5)
# * Subtraction -
print(5 - 5)
# * Multiplication *
print(5 * 5)
# *div /
print(5 / 5)
# *Modulus %
print(5 % 5)
# *Exponentiation **
print(5**5)
# * Floor division
print(5 // 5)

# *Comparison Operators
print("Comparison Operators")
# * Equal operator
print(10 == 10)
# * not equal operator
print(10 != 0)
# * Greater than operator
print(10 > 0)
# * Less than
print(0 < 10)
# *Greater than or equal to

# * Greater than or equal to operator
print(10 >= 0)
# * Less than or equal to operator
print(0 <= 10)

# * Logical operators
print("Logical operators")
# * and operator &&
x = 5
print(x > 0 and x < 10)

# * or operator ||
print(x > -10 or x < -10)

# * not !
print(not (x > 0 and x < 10))


# * Identity Operators
print("Identity Operators")
x = 10
y = 10

print(x is y)

a = 10
b = 11
print(a is not b)

# * Membership Operators
print("Membership Operators")

cars = ["dacia", "toyota", "peugeot"]
print("dacia" in cars)  # * this check if dacia present on cars

print(not ("citroen" not in cars))
