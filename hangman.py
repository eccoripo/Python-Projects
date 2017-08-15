import time
import random

#welcoming the user
name = raw_input("What is your name? ")

print "Hello, " + name, "\nTime to play hangman!"

print ""

#wait for 1 second
time.sleep(1)

print("Guess a children character...")
time.sleep(0.5)

# store words in a list and randomly pick an answer from the list
words = ["elsa", "winnie the pooh", "bugs bunny", "daffy duck", "mickey mouse","cinderalla", "peter pan"]
word = (random.choice(words))

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:

    # make a counter that starts with zero
    failed = 0

    # for every character in secret_word
    for char in word:

    # see if the character is in the players guess
        if char in guesses:

        # print then out the character
            print char,

        else:

        # if not found, print a dash
            print "_",

        # and increase the failed counter with one
            failed += 1

    # if failed is equal to zero

    # print You Won
    if failed == 0:
        print "\nYay, you won! :)"

    # exit the script
        break

    print

    # ask the user go guess a character
    guess = raw_input("\nType a letter: ")

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:

     # turns counter decreases with 1 (now 9)
        turns -= 1

    # print wrong
        print "Sorry, not a correct character"

    # how many turns are left
        print "You have", + turns, 'more guesses left'

    # if the turns are equal to zero
        if turns == 0:

        # print "You Loose"
            print "\nSorry, you couldn't guess it this time :("
