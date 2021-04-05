def sequence_del(my_str):
	new_str = ""
	prev_letter = ""
	for i in my_str:
		if i != prev_letter:
			new_str += i
		prev_letter = i
	return new_str
	
print(sequence_del("ppyyyyythhhhhooonnnnn"))
print(sequence_del("SSSSsssshhhh"))
print(sequence_del("Heeyyy   yyouuuu!!!"))
	