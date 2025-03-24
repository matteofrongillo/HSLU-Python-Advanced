def user_input():
    try:
        i = int(input("Numer 1: "))
        j = int(input("Numer 2: "))
        division = round(i/j,3)

    except:
        raise ZeroDivisionError("Cannot divide by 0")

# print(user_input())


def user_input2():
    i = int(input("Numer 1: "))
    while True:
        try:
            j = int(input("Numer 2: "))
            division = round(i/j,3)

        except:
            continue

        else:
            return division

print(user_input2())