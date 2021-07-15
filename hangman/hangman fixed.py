import re
from os.path import isfile
from random import randint


HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ """
MAX_TRIES = 6

HANGMAN_PHOTOS = {1: """
    x-------x
""", 2: """
    x-------x
    |
    |
    |
    |
    |
""", 3: """
    x-------x
    |       |
    |       0
    |
    |
    |
""", 4: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
""", 5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""", 6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""", 7: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""}


def print_hangman(num_of_tries):
    """the func prints a draw according to the user fails.
    :param num_of_tries: num of wrong guesses
    :type num_of_tries: int
    :return: None"""
    print(HANGMAN_PHOTOS[num_of_tries + 1])
    return None


def check_valid_input(letter_guessed, old_letters_guessed):
    """the func checking if the character is a new english letter.
    :param letter_guessed: the character
    :param old_letters_guessed: list of the letters that guessed already
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: boolean value if the string is valid.
    :rtype: bool"""
    low_letter = letter_guessed.lower()
    if len(letter_guessed) > 1:
        return False
    elif re.search('[^a-zA-Z]', letter_guessed):
        return False
    elif low_letter in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """the func add the new english letter to the list of the old letters.
    :param letter_guessed: the character
    :param old_letters_guessed: list of the letters that guessed already
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: boolean value if the addition success.
    :rtype: bool"""
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X\ninvalid pattern")
        old_letters_guessed.sort()
        print(" -> ".join(old_letters_guessed))
        return False


def show_hidden_word(secret_word, old_letters_guessed):  # 7.3.1
    """the func showing to rhe user his progress in the word.
    :param secret_word: the word
    :param old_letters_guessed: list of the letters that guessed already
    :type secret_word: string
    :type old_letters_guessed: list
    :return: word with letters who guessed and '_' when it didn't guessed
    :rtype: string"""
    output_string = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            output_string += letter + " "
        else:
            output_string += "_ "
    return output_string


def check_win(secret_word, old_letters_guessed):
    """the func checking if the user won the game.
    :param secret_word: the word
    :param old_letters_guessed: list of the letters that guessed already
    :type secret_word: string
    :type old_letters_guessed: list
    :return: boolean value if mission completed.
    :rtype: bool"""
    bool_list = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            bool_list.append(True)
        else:
            bool_list.append(False)
    if False in bool_list:
        return False
    else:
        return True


def choose_word(file_path, index):
    """the func provide the secret word to the game from text file.
    :param file_path: a text file that include only words and spaces.
    :param index: the index of the word in the file.
    :type file_path: string
    :type index: int
    :return:a tuple in length 2. the first element is the number of the words in the file.
        the second is the chosen secret word.
    :rtype: tuple"""
    file_text = open(file_path, 'r')
    content = file_text.read()
    words_list = content.split(" ")
    small_list = words_list.copy()
    for word in small_list:
        while small_list.count(word) > 1:
            small_list.remove(word)
    words_num = len(small_list)
    secret_word = words_list[(index - 1) % len(words_list)]
    output_tuple = (words_num, secret_word)
    return output_tuple


def main():
	print(HANGMAN_ASCII_ART, "\nYou have %d tries." % MAX_TRIES)
	#words_file_path = input("Please enter the path of your words file: ")
	#while not isfile(words_file_path):
	    #print("Your path is invalid. Try again.")
	    #words_file_path = input("Please enter the path of your words file: ")
	words_file_path = 'words.txt'
	    
	#pos_in_file = input("Please choose any number: ")
	#while not pos_in_file.isnumeric() or int(pos_in_file) <= 0:
	    #print("It must be positive number. Try again")
	    #pos_in_file = input("Please choose any number: ")
	#pos_in_file = int(pos_in_file)
	pos_in_file = randint(0, 1000)
	
	chosen_tuple = choose_word(words_file_path, pos_in_file)
	chosen_word = chosen_tuple[1]
	print("The secret word chosen successfully!\nLet's start!")
	print_hangman(0)
	print("_ " * len(chosen_word))
	
	letters_guessed_list = []
	current_try = 0
	while current_try < MAX_TRIES:
	    the_guess = input("Guess a letter: ")
	    low_guess = the_guess.lower()
	    if try_update_letter_guessed(low_guess, letters_guessed_list):
	        if check_win(chosen_word, letters_guessed_list):
	            print(show_hidden_word(chosen_word, letters_guessed_list))
	            print("\n\tWIN!\tWIN!\tWIN!\n")
	            break
	        if low_guess not in chosen_word:
	            current_try += 1
	            print(":(")
	            print_hangman(current_try)
	        print(show_hidden_word(chosen_word, letters_guessed_list))
	
	if not check_win(chosen_word, letters_guessed_list):
	    print("\nLOSE!\n")


if __name__ == "__main__":
    again = 'y'
    while again == 'y':
    	main()
    	again = input('do you want to play again? (y/n) ')
