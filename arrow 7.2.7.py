def arrow(my_char, max_length):
	mystring = ""
	for i in range(max_length):
		output = my_char * i
		mystring += output + "\n"
	for i in range(max_length, 0, -1):
		output = my_char * i
		mystring += output + "\n"
	return mystring

print(arrow('*', 5))
print(arrow('7', 7))
print(arrow('w', 3))