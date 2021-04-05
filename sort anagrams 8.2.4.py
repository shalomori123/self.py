def sort_anagrams(list_of_strings):
	list_of_lists = []
	for i in list_of_strings:
		small_list = []
		for j in list_of_strings:
			if sorted(list(i)) == sorted(list(j)):
				small_list.append(j)
		list_of_lists.append(small_list)
	for small in list_of_lists:
		while list_of_lists.count(small) > 1:
			list_of_lists.reverse()
			list_of_lists.remove(small)
			list_of_lists.reverse()
	return list_of_lists
	
print(sort_anagrams(['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']))