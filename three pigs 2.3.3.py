bricks_number = input("enter number with three digits that represent the number of bricks that every pig find: ")
num=int(bricks_number)
sum = int(num / 100) + int((num % 100) / 10) + int(num % 10)

print(sum)
print(int(sum / 3))
print(sum % 3)
print(sum % 3 == 0)