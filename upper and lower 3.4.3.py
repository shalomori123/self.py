input_string = input("Please enter a string: ")
string_length = len(input_string)
output_string = input_string[:(string_length // 2)].lower() + input_string[(string_length // 2):].upper()

print(output_string)
