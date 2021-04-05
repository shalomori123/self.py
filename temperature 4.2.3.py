temperature = input("Enter the temperature: ")

if temperature[-1] == 'c' or temperature[-1] == 'C':
    c_degreese = float(temperature[:-1])
    convert_to_f = (9 * c_degreese + 160) / 5
    print(str(convert_to_f) + 'F')

elif temperature[-1] == 'f' or temperature[-1] == 'F':
    f_degreese = float(temperature[:-1])
    convert_to_c = (5 * f_degreese - 160) / 9
    print(str(convert_to_c) + 'C')

else:
    print("please insert the units.")
