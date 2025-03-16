# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    new_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            new_word = new_word + letter
    return new_word == secret_word


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    new_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            new_word = new_word + letter
        else:
            new_word = new_word + '*'
    return new_word
        


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in letters_guessed:
        #a, p , p, l, e
        if letter in letters:
            letters.remove(letter)
    return ''.join(letters)

def hint_reveal(secret_word, available_letters):
    """

    Parameters
    ----------
    secret_word : the secret word as a string that the user is guessing
    available_letters : letters that were still not guessed

    Returns
    -------
    revealed_letter : returns the random letter in the word as 

    """
    choose_from = ""
    for letter in secret_word:
        if letter in available_letters:
            choose_from = choose_from + letter
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter

def unique_letters(secret_word):
    """
    

    Parameters
    ----------
    secret_word : takes in the secret word as a string

    Returns
    -------
   returns a string of all the unique letters in the string

    """
    unique = ""
    for letter in secret_word:
        if letter not in unique:
            unique = unique + letter
    return unique

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess = 10
    letters_guessed = []
    available_letters = get_available_letters(letters_guessed)
    word = get_word_progress(secret_word, letters_guessed)
    hint_letter = ""
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    while (guess >= 0):
        if (guess <= 0):
            print("---")
            print(f"Sorry, you ran out of guesses. The word was {secret_word}")
            break
        print("---")
        print(f"You have {guess} guesses left")
        print(f"Available letters: {available_letters}")
        letter = str(input("Please guess a letter: "))
        if (with_help == True):
            if(guess < 3 and letter == "!"):
                print(f"Oops! Not enough guesses left: {word}")
            while (letter.isalpha() == False and letter != '!'):
                letter = str(input("Oops! That is not a valid letter. Please input a letter from the alphabet: "))
        else:
            while (letter.isalpha() == False):
                letter = str(input("Oops! That is not a valid letter. Please input a letter from the alphabet: "))
        letters_guessed.append(letter.lower())
        word = get_word_progress(secret_word, letters_guessed)
        
        if (letter in secret_word and letter in available_letters):
            print(f"Good guess: {word}")
        elif (letter == '!' and with_help == True and guess > 3):
            guess = guess - 3
            hint_letter = hint_reveal(secret_word, available_letters)
            letters_guessed.append(hint_letter.lower())
            word = get_word_progress(secret_word, letters_guessed)
            print(f"Letter revealed: {hint_letter}")
            print(f"{word}")
        elif (letter not in available_letters):
            print(f"Oops! You've already guessed that letter: {word}")    
        else:
            if(letter not in 'aeiou'):
                guess = guess - 1
            else:
                guess = guess - 2
            print(f"Oops! That letter is not in my word: {word}")
    
        available_letters = get_available_letters(letters_guessed)
        if (has_player_won(secret_word, letters_guessed)):
            unique = unique_letters(secret_word)
            total_score = (guess + 4 * len(unique)) + 3 * len(secret_word)
            print("---")
            print("Congratulations, you won!")
            print(f"Your total score for this game is {total_score}")
            break
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test
if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = "hi"
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

