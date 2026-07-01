"""
score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("Grade: A!")
elif score >= 80 and score < 90:
    print("Grade: B!")
elif score >= 70 and score < 80:
    print("Grade: C!")
elif score >= 60 and score < 70:
    print("Grade: D!")
else:
    print("Grade: F!")

#Let's optimize this code
score = int(input("Enter your score: "))

if 90 <= score and score <= 100:
    print("Grade: A!")
elif 80 <= score and score < 90:
    print("Grade: B!")
elif 70 <= score and score < 80:
    print("Grade: C!")
elif 60 <= score and score < 70:
    print("Grade: D!")
else:
    print("Grade: F!")

#Let's further optimize this code
score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Grade: A!")
elif 80 <= score < 90:
    print("Grade: B!")
elif 70 <= score < 80:
    print("Grade: C!")
elif 60 <= score < 70:
    print("Grade: D!")
else:
    print("Grade: F!")

#Further improvement
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A!")
elif score >= 80:
    print("Grade: B!")
elif score >= 70:
    print("Grade: C!")
elif score >= 60:
    print("Grade: D!")
else:
    print("Grade: F!")


#Let's deal with Parity
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()

#Let's improve this code
def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

main()


#Further optimization
def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()
"""


name = input("What is your name? ").capitalize()

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

#Let's optimize this code
name = input("What is your name? ").capitalize()

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

#Let's further optimize this code
name = input("What is your name? ").title()

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


#More optimization
name = input("What is your name? ").title()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


#One more optimization
name = input("What is your name? ").title() 

if name in ["Harry", "Hermione", "Ron"]:
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")