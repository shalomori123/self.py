def show_hidden_word(secret_word, old_letters_guessed):
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
	
print(show_hidden_word('mammals', ['s', 'p', 'j', 'i', 'm', 'k'])) #ניסיון