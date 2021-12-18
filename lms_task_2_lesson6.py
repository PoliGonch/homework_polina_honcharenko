x = str('0123456789')
if x.isdigit() == True:
    if len(x) == 10:
        print("Okey, it's a correct number")
    else:
        print("You numer must be 10 characters long")
else:
    print("It's not a number!")
