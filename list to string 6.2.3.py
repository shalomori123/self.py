def format_list(my_list):
	"""the odd elements in list, and the last one.
	:param my_list: odd list of strings
	:type my_list: list
	:rtype: string"""
	new_list = my_list[:-1:2]
	output = ", ".join(new_list) + ', and ' + my_list[-1]
	return output
	
print(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))