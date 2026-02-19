a = str(10)
# ! b = int("100.15") we can't do this error
b = int(float("100.15"))
c = float(b)
d = complex(c)

print(a)
print(b)
print(c)
print(d)
