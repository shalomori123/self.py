def choose_word(file_path, index):
	"""the func provide the secret word to the game from text file.
	:param file_path: a text file that include only words and spaces.
	:param index: the index of the word in the file.
	:type file_path: string
	:type index: int
	:return: a tuple in length 2. the first element is the number of the words in the file. the second is the choosen secret word.
	:rtype: tuple"""
	file_text = open(file_path, 'r')
	content = file_text.read()
	words_list = content.split(" ")
	small_list = words_list.copy()
	for word in small_list:
		while small_list.count(word) > 1:
			small_list.remove(word)
	words_num = len(small_list)
	choosen_word = words_list[(index - 1) % len(words_list)]
	output_tuple = (words_num, choosen_word)
	return output_tuple

print(choose_word('words.txt', 3)) # ניסיון
print(choose_word('words.txt', 15))