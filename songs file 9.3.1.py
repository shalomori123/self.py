def my_mp3_playlist(file_path):
	file_txt = open(file_path, 'r')
	lines_list = file_txt.readlines()
	main_list = []
	for line in lines_list:
		main_list.append(line.split(';'))
	
	len_list = []
	for list in main_list:
		len_list.append(list[2])
	longest_song = main_list[len_list.index(sorted(len_list)[-1])][0]
	
	singer_list = []
	for list in main_list:
		singer_list.append(list[1])
	count_list = []
	for singer in singer_list:
		count_list.append(singer_list.count(singer))
	popular_singer = singer_list[count_list.index(sorted(count_list)[-1])]
	
	output_tuple = (longest_song, len(main_list), popular_singer)
	return output_tuple
	
print(my_mp3_playlist("/sdcard/python/documents/songs file.txt"))
