# problem 1
greeting = "Hello"
my_name = "Andrew"
my_age = "23"
print(greeting + " " + my_name + "!!! I hear that you are " + my_age + " today!!!") #this concatenates all variables and strings together
print(f"{greeting} {my_name}!!! I hear that you are {my_age} today!!!") #this formats the entire string together like a template

#problem 2
# asks for a password and then asks another user to guess it
userPass = input("What is your password? ")
userGuess = input("Guess the password: ")
while userPass != userGuess:
    userGuess = input("Try again: ")
print("Correct!") #could put this inside the loop, but if the very first guess is correct then the user would never get a "correct!" alert


# problem 3
# takes each number between 1 and 51 (not including) and prints them 3 in a row
for x in range(1, 51, 1):
    print(f"{x} {x} {x}")


# problem 4
# generates a random number, asks the user to guess and tells them if they need to guess higher or lower
import random
random_num = random.randint(1, 50)
userGuess = 0

while userGuess != random_num:
    userGuess = int(input("Guess the correct number between 1 and 50: "))
    if userGuess > random_num:
        print("Guess lower!")
    elif userGuess < random_num:
        print("Guess higher!")
    else:
        print("That's correct!")


# Extra
# asks the user to give a number, then the computer generates random numbers until the program sees that it matches the user input
userNum = int(input("Please enter a number between 1 and 10000 for the computer to guess: "))
computerInput = 0
x = 0

while computerInput != userNum:
    computerInput = random.randint(1, 10000)
    if computerInput != userNum:
        x = x + 1
    elif computerInput == userNum:
        print(f"GOT IT! It took {x} tries to find your number.") #tells the user how many times the computer attempted to guess