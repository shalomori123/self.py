def who_is_missing(file_name):
	file_txt = open(file_name, 'r')
	my_list = file_txt.read().split(',')
	my_list.sort()
	for i in my_list:
		if int(i) != my_list.index(i) + 1:
			new_file = open("/sdcard/python/documents/found.txt", 'w+')
			new_file.write(str(int(i)-1))
			new_file.close()
			return int(i)-1
			break
	file_txt.close()

print(who_is_missing("/sdcard/python/documents/findMe.txt"))