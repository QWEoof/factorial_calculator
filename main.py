number = int(input("Введіть число: "))
factorial = 1

if number < 0:
    print("Факторіал не визначений для від'ємних чисел.")
elif number == 0:
    print("Факторіал числа 0 дорівнює 1.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print("Факторіал числа", number, "дорівнює", factorial)