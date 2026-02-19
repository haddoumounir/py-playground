

print("hello")
print('hello')

a = 'hello'
print(a)

a = "hello"
print(a)

a = """  Do play they miss give so up. Words to up style of since world. We leaf to snug on no need. Way own uncommonly traveling now acceptance bed compliment solicitude. Dissimilar admiration so terminated no in contrasted it. Advantages entreaties mr he apartments do. Limits far yet turned highly repair parish talked six. Draw fond rank form nor the day eat.

However venture pursuit he am mr cordial. Forming musical am hearing studied be luckily. Ourselves for determine attending how led gentleman sincerity. Valley afford uneasy joy she thrown though bed set. In me forming general prudent on country carried. Behaved an or suppose justice. Seemed whence how son rather easily and change missed. Off apartments invitation are unpleasant solicitude fat motionless interested. Hardly suffer wisdom wishes valley as an. As friendship advantages resolution it alteration stimulated he or increasing. """


print(a)

# * slicing string 
# ! first character is index 0
b = "Hello, World!"
print("\n")
print(b[0:4]+"\n")


# * from start to 
print(b[:3]+"\n")

# * from index to the end 
print(b[1:] + "\n")


# * to upper case
print(b.upper())

# * to lower case
print(b.lower())

# * remove white spaces from the end and start 
b = "                                   [hello]                                  "
print(b.strip())

# * replace string 
b = "Hello, World"
print(b.replace("World","How are you ?")) # ! first arg is src part and sec arg is pasted part

# * split string 

print(b.split('o')) # ! the arg i just give it to method split is the del as we have on my 42 split

# * Concatenate string 


a = 'Hello'
b = "my name is"
c = "Mounir"

e = a+' '+ b + " "+c
print(e)

# * f strings

firstName = 'Mounir'
lastName = "haddou"
age = 22
allInfos = f"hello my full  name is {firstName} {lastName}, I'm {age}"

print(allInfos)

#* escape character
print("this is \"double quote\"")

