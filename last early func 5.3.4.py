def last_early(my_str):
    low_string = my_str.lower()
    boolean_value = low_string[-1] in low_string[:-1]
    return boolean_value


print(last_early('happy birthday'))
print(last_early('best of luck'))
print(last_early('Wow'))
print(last_early('X'))
