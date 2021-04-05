def numbers_letters_count(my_str):
	my_list = [0, 0]
	for i in my_str:
		if i.isnumeric():
			my_list[0] += 1
		else:
			my_list[1] += 1
	return my_list
	
print(numbers_letters_count("Python 3.6.3"))