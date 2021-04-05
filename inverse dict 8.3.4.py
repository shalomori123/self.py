def inverse_dict(my_dict):
	new_dict = {}
	for value in my_dict.values():
		new_list = []
		for key in my_dict.keys():
			if my_dict[key] == value:
				new_list.append(key)
		new_dict[value] = new_list
	return new_dict
	
print(inverse_dict({'I': 3, 'love': 3, 'self.py!': 2}))