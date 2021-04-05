import re  # ביטויים רגולריים

the_guess = input("Guess a letter: ")
#מכאן שודרג ב-5 ו6
if len(the_guess) > 1 and not re.search('[^a-zA-Z]', the_guess):
    print("E1")
elif len(the_guess) == 1 and not re.search('[a-zA-Z]', the_guess):
    print("E2")
elif len(the_guess) > 1 and re.search('[^a-zA-Z]', the_guess):
    print("E3")
elif len(the_guess) == 1 and re.search('[a-zA-Z]', the_guess):
    the_guess_low = the_guess.lower()
    print(the_guess_low)
