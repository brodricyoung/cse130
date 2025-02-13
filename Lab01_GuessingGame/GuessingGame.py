# 1. Name: 
#    Brodric Young

# 2. Assignment Name: 
#    Lab 01: Python Review

# 3. Assignment Description:
#    Guessing game

# 4. What was the hardest part? Be as specific as possible.
#    The assignment was pretty simple for me, the hardest part was probably trying 
#    to figure out if there was a better way to count the number of guesses or to 
#    initialize the while loop without having to set the 'guess' variable to 0 beforehand. 
#    Any other way I could think of to do it was more work than it was worth and this 
#    was the simplest and easiest to my knowledge.

# 5. How long did it take for you to complete the assignment?
#    About 50 minutes. 


def guessing_game():
    import random

    # Game introduction.
    print('This is the "Guess a Number" game.')
    print('You try to guess a random number in the smallest number of attempts.')
    print()

    # Prompt the user for how difficult the game will be. Ask for an integer.
    value_max = int(input('Pick a positive integer: '))

    # Generate a random number between 1 and the chosen value.
    value_random = random.randint(1, value_max)

    # Give the user instructions as to what he or she will be doing.
    print(f'Guess a number between 1 and {value_max}.')

    # Initialize the sentinal and the array of guesses.
    guesses_list = []
    num_of_guesses = 0
    guess = 0

    # Play the guessing game.
    while guess != value_random:

        # Prompt the user for a number.
        guess = int(input('> '))
        num_of_guesses += 1

        # Store the number in an array so it can be displayed later.
        guesses_list.append(guess)

        # Make a decision: was the guess too high, too low, or just right.
        if guess > value_random:
            print('     Too high!')

        if guess < value_random:
            print('     Too low!')

    # Give the user a report: How many guesses and what the guesses where.
    print(f'You were able to find the number in {num_of_guesses} guesses.')
    print(f'The numbers you guessed were: {guesses_list}')



if __name__ == '__main__':
    guessing_game()