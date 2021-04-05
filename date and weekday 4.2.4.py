import calendar

date = input("Please enter the date in template dd/mm/yyyy: ")
day_in_month = int(date[:2])
month = int(date[3:5])
year = int(date[6:])

weekday = calendar.weekday(year, month, day_in_month)

if weekday == 0:
    print("Monday")
elif weekday == 1:
    print("Tuesday")
elif weekday == 2:
    print("Wednesday")
elif weekday == 3:
    print("Thursday")
elif weekday == 4:
    print("Friday")
elif weekday == 5:
    print("Saturday")
elif weekday == 6:
    print("Sunday")
