a = 5
while a:
    print(a)
    a = a - 1
    if a == 2:
        break
    print("While loop last statement")
print("Outside while")

a = [1, 2, 3, 4, 5]
for i in a:
    print(i)
    if i == 3:
        break
    print("Last statement of for loop")
print("Outside for")
