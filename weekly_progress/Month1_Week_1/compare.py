x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print(f"{x} is less than {y}")
if x > y:
    print(f"{x} is greater than {y}")
if x == y:
    print(f"{x} is equal to {y}")

#Lets improve this
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print(f"{x} is less than {y}")
elif x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is equal to {y}")

#Further optimization
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")

#Further optimization
x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")

#Lastly
x = int(input("What's x? "))
y = int(input("What's y? "))

if x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is not equal to {y}")