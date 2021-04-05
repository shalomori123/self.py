def are_lists_equal(list1, list2):
	list1.sort()
	list2.sort()
	boolean_value = list1 == list2
	return boolean_value
	
list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]
print(are_lists_equal(list1, list2))
print(are_lists_equal(list1, list3))
