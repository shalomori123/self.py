def shift_left(my_list):
	"""to take a list and shift it one place to left.
	:param my_list: get a list of 3 elements
	:type my_list: list
	:return: new list shifted
	:rtype: list"""
	new_list = [my_list[1], my_list[2], my_list[0]]
	return new_list

print(shift_left([4, 5, 6]))
print(shift_left([0, 1, 2]))
print(shift_left(["monkey", 2.0, 1]))