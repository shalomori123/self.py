def count_chars(my_str):
	my_dict = {}
	for letter in my_str:
		if letter != " ":
			my_dict[letter] = my_str.count(letter)
	return my_dict

print(count_chars("abra cadabra"))