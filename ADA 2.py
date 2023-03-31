phrase = "\"We're so glad you're here!\" they said.\n"
print(phrase)
phrase = 'hello \nscholar!\n'
print(phrase)
phrase= 'ada\\lovelace'
print(phrase)
phrase = "ada\\lovelace\n"
print(phrase)

phrase= "A single backslash escape character at the end of a line "\
    "goes outside of the quotation mark " \
    "as shown in this example.\n"
print(phrase)


x1 = 2021
x2 = 1
x3 = 13
print(f"{x1} + 20 = {x1 + 20}")
print(f"{x2} + 20 = {x2 + 20}")
print(f'{x3} + 20 = {x3 + 20}')

amount = 20
x1 = 2021
x2 = 1
x3 = 13
sum1 = x1 + amount
sum2 = x2 + amount
sum3 = x3 + amount
print(f"{x1} + 20 = {sum1} ,sum1 included")
print(f"{x2} + 20 = {sum2} ,sum2 included")
print(f"{x3} + 20 = {sum3} ,sum3 included")
print(f"{x3} + amount = {sum3} ,amount and sum3 included")

word_1 = "home"
word_2 = "work"
concatenated_words = word_1 + word_2
print(f"You can combine the words {word_1} and {word_2} \
to make the word {concatenated_words}.")

word_1 = "home"
word_2 = "work"
concatenated_words = word_1 + word_2 + ' '
duplicated_words = 3 * concatenated_words
print(f"These days, all I seem to do is {duplicated_words}.")

name = "Ada Lovelace"
print(name[4])
print(name[1:9])
print(name[1:9:5])
print(name[0:8:2])
print(name[8])

name = 'Solange Puti'
print(name[9])
print(name[0:9])
print(name[1:9:2])
print(name[0:11:2])

temp = 60
if temp == 0:
    print("It's ZERO DEGREES outside!")
elif temp == 100:
    print("It's ONE HUNDRED DEGREES outside!")
elif temp < 50:
    print("It's a bit chilly outside!")
elif temp < 100:
    print("It's warm outside!")

score = 21
if score > 21:
    print("Bust!")
elif score == 21:
    print("Black Jack!")
elif score < 21:
    print("Great Hand!")
elif score < 17:
    print("Hit Me!")

x = 2
if x:
    print(f"x = {x}, and therefore it's truthy")
else:
    print(f"x = {x}, and therefore it's falsey")


y = 14
x = 5
print(y/x)
if (x%y):
    print(f"{y} is divisible by 5")
else:
    print(f"{y} is not divisble by 5")

x = 4
if x % 5 == 0:
    print(f"{x} is divisible by 5")
else:
    print(f"{x} is not divisble by 5")

coffee = False
good_sleep = True
if coffee or good_sleep:
    print("It's going to be a great day!")
else:
    print("Eh. Today's going to be a wash.")

x = 17
y = 13
if x == y:
    print('equals')
elif x < y:
    print('less')
elif x > y:
    print('greater')

x=23
y= 14
if x == y:
    print(f"{x} is equal to {y}.")
elif x > y:
    print(f"{x} is greater than {y}.")
elif x < y:
    print(f"{x} is less than {y}.")

cookies = False
cake = False

if cookies:
    print("I am the cookie monster!")

if cake:
    print("Yum, I love cake!")
else:
    print("fine, I'll have the cookies")

person_age = 25
ada_age = 6
if person_age < ada_age:
    print("This person is younger")
elif ada_age < person_age:
    print("Ada is younger.")
else:
    print("They are the same age")

pet = "dog"
food = "broccoli"

if pet == "cat":
    print("meow!")
elif pet == "dog":
    print("woof")
else:
    print("some other sound")

if food =="broccoli":
    print("eh.")
elif food == "ice cream":
    print("yum!")
else:
    print("gross")

x = 7
y = 7
if x >= y:
    if x > y:
        print("x is bigger than y")
    else:
        print("x = y")
else:
    print("y is bigger")

if x > y or x == y:
    if x > y:
        print("x is bigger")
    else:
        print("x = y")
else:
    print("y is bigger")

if x >= y:
    print("x is d")
else:
    print("y is bigger")
if x == y:
    print("x = y")


player1 = "scissors"
player2 = "rock"

# tie
if player1 == player2:
    print("It's a tie!")

# player 2 is rock
if player2 == "rock":
    if player1 == "paper":
        print("Player 1 won!")
    elif player1 == "scissors":
        print("Player 2 won!")
    elif player1 == "paper":
        print("It's a tie")
# player 2 is paper
if player2 == "paper":
    if player1 == "rock":
        print("Player 2 won!")
    elif player1 == "scissors":
        print("Player 1 won!")
    elif player1 == "paper":
        print("It's a tie!")
# player 2 is scissors
if player2 == "scissors":
    if player1 == "rock":
        print("Player 1 won!")
    elif player1 == "paper":
        print("Player 2 wins")
    elif player1 == "scissors":
        print("It's a tie!")

print(round(2.6))

import math
print(math.sqrt(16))

import random
print(random.randint(1,10))

import random
print(random.random())

def say_hello(name):
    print(f"welcome {name}! hello world!")
say_hello("Ada")

def traffic_stop(name):
    print(f"please stop at a {name} light.")
traffic_stop("red")

def traffic_stop(colors):
    print(f"the three stop light colors are: {colors}.")
traffic_stop("red, yellow, and green")

num_one = 10
num_two = 9
def add(num_one, num_two):
    """
    input: two numbers
    output: the sum of the arguments
    """
    return num_one + num_two

the_sum = add(num_one, num_two)
print(f"the sum of {num_one} and {num_two} is {the_sum}")

def say_hello(name):
    print(f"welcome {name}! hello world!")
no_return_value = say_hello("becca")
print(no_return_value)