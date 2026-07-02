'''
i = 3
while i != 0:
    print("meow")
    i = i - 1


#Let's improve this code
i = 0
while i < 3:
    print("meow")
    i = i + 1

#Even better
i = 0
while i < 3:
    print("meow")
    i += 1


#Let's add a for loop
for i in [0, 1, 2]:
    print("meow")


#Let's use the range function
for i in range(5):
    print("meow")


#Let's take this a step further
print("meow\n" * 5, end="")

#Let's involve the user
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break

#Let's further optimize this code
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
'''

#Let's create a function
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()