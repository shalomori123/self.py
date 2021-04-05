import re  # ביטויים רגולריים

def check_valid_input(letter_guessed, old_letters_guessed):
	"""the func checking if the chararcter is a new english letter.
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

old_letters = ['a', 'b', 'c'] #ניסיון
print(check_valid_input('a', old_letters))
print(check_valid_input('A', old_letters))
print(check_valid_input('$', old_letters))
print(check_valid_input("ab", old_letters))
print(check_valid_input("app$", old_letters))
print(check_valid_input("p", old_letters))
print(check_valid_input("P", old_letters))


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	"""the func add the new english letter to the list of the old letters.
	:param letter_guessed: the character
	:param old_letters_guessed: list of the letters that guessed already
	:type letter_guessed: string
	:type old_letters_guessed: list
	:return: boolean value if the addition succes.
	:rtype: bool"""
	if check_valid_input(letter_guessed, old_letters_guessed):
		old_letters_guessed.append(letter_guessed)
		return True
	else:
		print("X")
		old_letters_guessed.sort()
		print(" -> ".join(old_letters_guessed))
		return False

print(try_update_letter_guessed('A', old_letters)) #ניסיון
print(try_update_letter_guessed('c', old_letters))
print(try_update_letter_guessed('s', old_letters))
print(try_update_letter_guessed('d', old_letters))
print(try_update_letter_guessed('A', old_letters))

def main():
	check_valid_input("P", ['a', 'b', 'c'])
	try_update_letter_guessed("P", ['a', 'b', 'c'])

if __name__ == "__main__":
	main()
