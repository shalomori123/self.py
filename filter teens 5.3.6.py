def fix_age(age):
    if 13 <= age <= 19 and not 15 <= age <= 16:
        age = 0
    return age


def filter_teens(a=13, b=13, c=13):
    fixed_a = fix_age(a)
    fixed_b = fix_age(b)
    fixed_c = fix_age(c)
    ages_sum = fixed_a + fixed_b + fixed_c
    return ages_sum


print(filter_teens())
print(filter_teens(1, 2, 3))
print(filter_teens(2, 13, 1))
print(filter_teens(2, 1, 15))
