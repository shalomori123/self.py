def chocolate_maker(small, big, x):
    length_of_big = big * 5
    if length_of_big > x:
        boolean_value = small >= x % 5
    elif length_of_big == x:
        boolean_value = True
    else:
        boolean_value = length_of_big + small >= x
    return boolean_value


print(chocolate_maker(3, 1, 8))
print(chocolate_maker(3, 1, 9))
print(chocolate_maker(3, 2, 10))
print(chocolate_maker(1, 2, 7))
print(chocolate_maker(346326, 128347, 832176))
print(chocolate_maker(873, 137474382, 275274240))
print(chocolate_maker(3, 137474382, 275274240))
print(chocolate_maker(3, 137474382, 675274240))
