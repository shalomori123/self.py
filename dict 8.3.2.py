my_dict = {"first_name": 'Mariah', "last_name": 'Carey', "birth_date": '27.03.1970', "hobbies": ['Sing', 'Compose', 'Act']}

def date_tuple():
	new_tuple = ()
	new_string = ""
	for i in my_dict['birth_date']:
		if i != ".":
			new_string += i
		else:
			new_tuple += (int(new_string),)
			new_string = ""
	new_tuple += (int(new_string),)
	my_dict['birth_date'] = new_tuple


number = input('enter a number: ')
if number == '1':
	print(my_dict['last_name'])

if number == '2':
	print(my_dict['birth_date'][3:5])

if number == '3':
	print(len(my_dict['hobbies']))

if number == '4':
	print(my_dict['hobbies'][-1])

if number == '5':
	my_dict['hobbies'].append("Cooking")

if number == '6':
	date_tuple()
	print(my_dict['birth_date'])

if number == '7':
	from datetime import date
	x = date.today()
	date_tuple()
	my_dict['age'] = x.year - my_dict['birth_date'][2]
	print(list(my_dict.items())[-1])
