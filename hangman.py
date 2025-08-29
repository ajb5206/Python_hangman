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
    
    ## for empty string secret word
    if len(secret_word) == 0:
        return True
    
    # for char in secret_word:
    #     #char is r, a ,r ,e
    #     if char not in letters_guessed:
    #         return False
    
    for char in secret_word:
        # apple letters guess a p z d 
        if char not in letters_guessed:
            return False
    return True
    #pass


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    string = ""
    for char in secret_word:
        if char in letters_guessed:
            string = string+char
        else:
            string = string + "*"
    return string
    #pass


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #cast string as list
    alphabet_list = list(alphabet)
    for char in letters_guessed:
        if char in alphabet_list:
            #get index of char in alphabet list
            index = alphabet_list.index(char)
            alphabet_list.pop(index)
    return "".join(alphabet_list)


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
    secret_word_length = len(secret_word)
    guesses = 10
    letters_guessed = ""
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {secret_word_length} letters long")
    
    
    ## ROUNDS 
    while guesses > 0:
        print("--------------")
        print(f"You have {guesses} guesses left.")
        print(f"Available Letters: {get_available_letters(letters_guessed)}")
        user_guess = input("Please guess a letter: ")
        
        while user_input_check(user_guess, letters_guessed) == False:
            print("--------------")
            user_guess = input()
        
        
        letters_guessed += user_guess
        # print(get_word_progress(secret_word, letters_guessed))
        
        #Running check if player has won

        if guesses > 3 and user_input == "!":
            helper_letter_reveal(secret_word, get_available_letters(letters_guessed))
            
            
        if user_guess in secret_word:
            print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
        else:
            print(f"Opps! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
            if user_guess in "aeiou":
                guesses -= 2
            else:
                guesses -= 1
        # call game termination calculation
        if has_player_won(secret_word, letters_guessed):
            print("------")
            print(f"Congratulations, you won!")
            print(f"Your total score for this game is: {user_score_calc(secret_word, guesses)}")
            return

    if guesses <= 0:
        print("------")
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")
    

### change input to lower case somewhere
### check if already guessed 
def user_input_check(user_input, letters_guessed):
    if user_input == "!":
        with_help = True
        return True
    elif len(user_input) != 1:
        print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")
        return False
    elif user_input.isalpha() == False:
        print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")
        return False
    elif user_input in letters_guessed:
        print(f"Opps! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
        return False
    return True

def user_score_calc(secret_word, guesses):
    unique_letters_holder = ""
    word_length = len(secret_word)
    
    for char in secret_word:
        if char not in unique_letters_holder:
            unique_letters_holder += char
            
    unique_letters = len(unique_letters_holder)
    
    total_score = (guesses + 4 * unique_letters) + 3 * word_length
    return total_score


def helper_letter_reveal(secret_word, available_letters):
    # current_word_state = get_word_progress(secret_word, letters_guessed)
    choose_from = ""
    
    for char in secret_word:
        if char in letters_guessed and char not in choose_from:
            choose_from += char
    
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter
    
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
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

