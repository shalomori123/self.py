input_string = input("Please enter a string: ")
first_letter = input_string[0]
output_string = first_letter + input_string[1:].replace(first_letter, "e")

print(output_string)
