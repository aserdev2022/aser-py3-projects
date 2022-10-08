# If condition:
#     Body of if
# elif condition:
#     Body of elif
# else:
#     Body of else

a = 10000
if (a > 0 and a < 100):
    print("This is positive number")
elif a == 0:
    print("This is zero")
elif a > 100 and a < 1000:
    print("Greater than 100")
elif a > 1000:
    print("Greater than 1000")
else:
    print("This is negative number")

age = 70
if age > 18:
    if age > 60:
        print("Senior citizen account")
    else:
        print("Open normal account")
else:
    print("Not eligible")
