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
	:param num_of_tries: num of worng guesses
	:type num_of_tries: int
	:return: None"""
	print(HANGMAN_PHOTOS[num_of_tries])
	return None


print_hangman(1) #ניסיון
print_hangman(2)
print_hangman(3)
print_hangman(4)
print_hangman(5)
print_hangman(6)
print_hangman(7)