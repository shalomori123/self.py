import math

def func(num1, num2):
	"""the function taking 2 numbers and find their pythagorean theorem third value.
	:param num1: the first number
	:param num2: the second num
	:type num1: float
	:type num2: float
	:return: the pythagorean theorem third value
	:rtype: float"""
	num3 = math.sqrt(num1**2 + num2**2)
	return num3

def main():
	func(3, 4)

if __name__ == "__main__":
	main()

print(func(3, 4))
print(func(12, 9))
print(func(3, 78))
