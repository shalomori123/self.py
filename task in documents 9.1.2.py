file_path = input('Enter a file path: ')
file_txt = open(file_path, 'r')

task = input('Enter a task: ')

if task == 'sort':
	my_list = []
	every_word = ""
	for character in file_txt.read():
		if character == ' ' or character == '\n':
			my_list.append(every_word)
			every_word = ""
		else:
			every_word += character
	my_list.append(every_word)
	my_list.sort()
	for item in my_list:
		while my_list.count(item) > 1:
			my_list.remove(item)
	print(my_list)

if task == 'rev':
	my_list = file_txt.readlines()
	for line in my_list:
		print(line[::-1])

if task == 'last':
	number = int(input('Enter a number: '))
	my_list = file_txt.readlines()
	for i in my_list[-number:]:
		print(i)
		

file_txt.close()