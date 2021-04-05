def sort_prices(list_of_tuples):
	sorted_list = sorted(list_of_tuples, reverse=True, key=last_element)
	return sorted_list

def last_element(tuple):
	return tuple[1]

print(sort_prices([('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]))