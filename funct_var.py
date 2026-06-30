#This is my very first Python program!
print("Hello, World!")

#Comment and ask for the user's name
name = input("What is your name? ")
print(f"Nice to meet you, {name}!")

#Let's optimize this code.
print("Hello, ", end="")
print(name)

#Printing literal qotation marks
print("Hello, \"friend\"")

#Removing the extra space in the output
name = name.strip()
print(f"Nice to meet you, {name}!")

#Capitalizing the first letter of the name
name = name.capitalize()
print(f"Nice to meet you, {name}!")

#Capitalizing the first letter of each word in the name
name = name.title()
print(f"Nice to meet you, {name}!")

#Doing evertyhing in one line
name = input("What is your name? ").strip().title()
print(f"Nice to meet you, {name}!")
#OR
name = name.strip().title()
print(f"Nice to meet you, {name}!")

#Splitting the name into first and last name
first, last = name.split()
print(f"Hello, {first}")