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
		

print(check_win('friends', ['m', 'p', 'j', 'i', 's', 'k'])) #ניסיון
print(check_win('yes', ['d', 'g', 'e', 'i', 's', 'k', 'y']))
