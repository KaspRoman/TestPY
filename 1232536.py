month = int(input("Введите месяц  ", ))

def season():
    global month
    if month == 1 or month == 2 or month ==12:
        print("Сейчас зима")
    elif month == 3 or month == 4 or month == 5:
        print("Сейчас весна")
    elif month == 6 or month == 7 or month == 8:
        print("Сейчас лето")
    elif month == 9 or month == 10 or month == 11:
        print("Сейчас лето")
    else:
        print("В году только 12 месяцев. Введи число от 1 до 12")


season()