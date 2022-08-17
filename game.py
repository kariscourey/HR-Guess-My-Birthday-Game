from random import randint

# Initialize variables
rounds = 5
answer = ""

# Obtain user name
name = input("Hi! What is your name? ")

# Evaluate round
for i in range(rounds):

    # Initialize month, year
    month = randint(1, 12)
    year = randint(1924, 2004)

    if answer != "Y":

        # Report guess and obtain user answer
        print("Guess " + str(i + 1) + ": " + name + ", you were born in " + str(month) + " / " + str(year) + ".")
        answer = input("Y/N? ")
        answer = answer.upper()

        # Evaluate answer in loop
        if i != (rounds - 1):
            if answer == "N":
                print("Drat! Lemme try again.")
            elif answer != "Y":
                print("Invalid input!")

    else:
        exit()

# Evaluate answer after loop
if answer == "Y":
    print("I knew it!")
else:
    print("I have other things to do. Goodbye.")
