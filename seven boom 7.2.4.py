def seven_boom(end_number):
	numbers_list = []
	for i in range(end_number + 1):
		if '7' in str(i):
			numbers_list.append('BOOM')
		elif i % 7 == 0:
			numbers_list.append('BOOM')
		else:
			numbers_list.append(i)
	return numbers_list
	
print(seven_boom(17))
print(seven_boom(800))
