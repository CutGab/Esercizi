import random

def guessing (n_min, n_max):

    n_min = n_min
    n_max = n_max
    i = 0


    generate = random.randrange(n_min, n_max)

    print("It's time to guess! You have 5 attempts to do this.")
    print(' ')
    print("############################################################")
    print(' ')

    while i <= 5:

        guess = input("Insert the number you believe to be correct: ")
        guess = int(guess)

        i += 1

        if i == 5:

            print("You reached the maximum number of attempts, try again!")

            break

        if guess == generate:

            print("Congratulations! Your guess was correct.")

            break

        if guess > generate:

            print("Too high! Try a little lower.")

        if guess < generate:

            print("Too low! Try a little higher.")



guessing(5, 10)