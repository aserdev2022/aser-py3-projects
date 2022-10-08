# while condition:
#     body

a = 1
while a < 5:
    print(a)
    a = a + 1
print("out of while loop")

# While loop is generally used when you are not aware of
# the number of iterations upfront

# While loop is executed till condition specified returns false

# Body of while loop is determined by the indentation

# You can use non boolean value in place of condition,
# any non zero value will be treated as true and 0 will be treated as false


a = 5
while a:
    print(a)
    a = a - 1
print("out of while loop")

# while loop with else
a = 5
while a:
    print(a)
    a = a - 1
else:
    print("out of while loop")
