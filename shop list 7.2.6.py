my_string = input('Please enter your shopping list: ')

my_list = [] #היה יותר נכון להשתמש בספליט
every_word = ""
for character in my_string:
	if character == ',':
		my_list.append(every_word)
		every_word = ""
	else:
		every_word += character
my_list.append(every_word)


def main_output():
	if my_number == "1":
		print("You choose to see your list:")
		print(my_list)
	
	if my_number == "2":
		print("You choose to see products number:")
		print(len(my_list))
	
	if my_number == "3":
		print("You choose to check if a product exist in your list.")
		selected_product = input("which product? ")
		print(selected_product in my_list)
	
	if my_number == "4":
		print("You choose to check how much times a product exist in your list.")
		selected_product = input("which product? ")
		print(my_list.count(selected_product))
	
	if my_number == "5":
		print("You choose to remove a product from your list.")
		selected_product = input("which product? ")
		if selected_product in my_list:
			my_list.remove(selected_product)
		else:
			print("this product is not in the list!")
	
	if my_number == "6":
		print("You choose to add a product to your list.")
		selected_product = input("which product? ")
		my_list.append(selected_product)
	
	if my_number == "7":
		print("You choose to see the invalid products in your list:")
		invalid_list = []
		for product in my_list:
			if len(str(product)) < 3:
				invalid_list.append(product)
			elif not product.isalpha():
				invalid_list.append(product)
		print(invalid_list)
	
	if my_number == "8":
		print("You choose to remove multiplied products from your list.")
		for product in my_list:
			while my_list.count(product) > 1:
				my_list.remove(product)
	

my_number = input('Please enter the number of your wanted operate: ')
main_output()

while my_number != "9":
	my_number = input('Please enter the number of your wanted operate: ')
	main_output()
