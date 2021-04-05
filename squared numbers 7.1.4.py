def squared_numbers(start, stop):
	i = start
	list = []
	while i <= stop:
		list.append(i**2)
		i += 1
	return list

print(squared_numbers(4, 8))
print(squared_numbers(-3, 3))
print(squared_numbers(0, 4))
print(squared_numbers(-3, 20))