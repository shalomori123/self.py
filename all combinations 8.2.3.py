def mult_tuple(tuple1, tuple2):
	big_tuple = ()
	for a in tuple1:
		for b in tuple2:
			big_tuple += ((a, b),)
			big_tuple += ((b, a),)
	return big_tuple
	
print(mult_tuple((1, 2), (4, 5)))
print(mult_tuple((1, 2, 3), (4, 5, 6)))
