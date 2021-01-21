class AddressBook():
    def __init__(self):
        self.n = []

    def add(self, a):
        return self.n.append(a)

    def remove(self, b):
        self.n.remove(b)

    def dis(self):
        return (self.n)


record = AddressBook()

while True:
    print("0. Выход")
    print("1. Добавить")
    print("2. Удалить")
    print("3. Вывести на экран")

    hi = int(input("Выберите действие: "))
    if hi == 1:
        record.add(input("Введите имя, фамилию и телефон через пробел"))
        print("Список: ", record.dis())
    elif hi == 0:
        print("Завершение")
        break
    elif hi == 2:
        record.remove(input("Введите, что нужно удалить"))
        print("Список: ", record.dis())
    elif hi == 3:
        print("Список: ", record.dis())
    elif hi != 0 or hi != 1 or hi != 2 or hi != 3:
        print("Введите корректное значение")
    else:
        False
