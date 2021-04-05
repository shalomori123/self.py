import re  # ביטויים רגולריים

def is_valid_input(letter_guessed): #שודרג ב6
	"""the func checking if the chararcter is an english letter.
	:param letter_guessed: the character
	:type letter_guessed: string
	:return: boolean value if the string is valid.
	:rtype: bool"""
	if len(letter_guessed) > 1:
		return False
	elif re.search('[^a-zA-Z]', letter_guessed):
		return False
	else:
		return True

print(is_valid_input('a')) #ניסיון
print(is_valid_input('A'))
print(is_valid_input('$'))
print(is_valid_input("ab"))
print(is_valid_input("app$"))
