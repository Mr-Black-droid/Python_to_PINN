'''
students = ["Hermione", "Harry", "Ron"]
print(students)
print(students[0])
print(students[1])
print(students[2])

#Let's make this simpler
for student in students:
    print(student)

#Let's utilize len() to get the length of the list
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1, students[i])
'''

#Let's utilize dicts now
students = ["Hermione", "Harry", "Ron", "Draco"]
Houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

#How we link these, is as follows:
students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor", 
            "Ron": "Gryffindor", 
            "Draco": "Slytherin"
            }

for student in students:
    print(student, students[student], sep=", ")

#Let's associate more than one value with each key
Students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in Students:
    print(student["name"], student["house"], student["patronus"], sep=", ")