def distance(num1, num2, num3):
    first_condition = abs(num1 - num2) == 1 or abs(num1 - num3) == 1
    second_condition = (abs(num3 - num2) >= 2 and abs(num3 - num1) >= 2) or (abs(num3 - num2) >= 2 and abs(num2 - num1) >= 2)
    boolean_value = first_condition and second_condition
    return boolean_value


print(distance(1, 2, 10))
print(distance(4, 5, 3))
