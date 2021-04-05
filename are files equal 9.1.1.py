def are_files_equal(file1, file2):
	file1_txt = open(file1, 'r')
	file2_txt = open(file2, 'r')
	if file1_txt.read() == file2_txt.read():
		return True
	else:
		return False
	file1_txt.close()
	file2_txt.close()


work_txt = '/sdcard/python/documents/work.txt'
vacation_txt = '/sdcard/python/documents/vacation.txt'
print(are_files_equal(work_txt, vacation_txt))