
#  * in python there is 3 types of variables  int, float, complex

from traceback import print_tb


a = 1 # * int
b = 1.99 # * float 
c = 2j # * complex are waiting with j as imagination part 

print(f"type of a:{type(a)} and it value is {a}")
print(f"type of b:{type(b)} and it value is {b}")
print(f"type of c:{type(c)} and it value is {c}")

# * Type Conversion


b = int(b)
print(f"type of b:{type(b)} and it value is {b}")

b = complex(b)
print(f"type of b:{type(b)} and it value is {b}")