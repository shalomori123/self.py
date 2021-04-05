def copy_file_content(source, destination):
	src_txt = open(source, 'r')
	dest_txt = open(destination, 'w+')
	dest_txt.write(src_txt.read())
	dest_txt.close()
	src_txt.close()

copy_file_content('/sdcard/python/documents/copy.txt', '/sdcard/python/documents/paste.txt')