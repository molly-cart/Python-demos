character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ", ")
print("he was 70 years old. ")
character_name = "Henry"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ", ")

from math import*
print(floor(4.9))
print(ceil(4.2))

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby" ]
print(friends[1])

coordinates = [(4,5), (6,7), (80, 34)]
coordinates[0] = 10
print(coordinates)


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

class Student:


    def __init__(self):
