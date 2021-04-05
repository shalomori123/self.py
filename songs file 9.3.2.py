def my_mp4_playlist(file_path, new_song):
	file_txt = open(file_path, 'r')
	lines_list = file_txt.readlines()
	file_txt.close()
	main_list = []
	for line in lines_list:
		main_list.append(line.split(';'))
	if len(main_list) < 3:
		for num in range(3 - len(main_list)):
			main_list.append([])
	main_list[2][0] = new_song
	for i in range(len(main_list)):
		main_list[i] = ';'.join(main_list[i])
	main_string = "".join(main_list)
	to_write = open(file_path, 'w')
	to_write.write(main_string)
	to_write.close()
	
my_mp4_playlist("/sdcard/python/documents/songs file.txt", "Python Love Story")