def out_numbers(n):
    summa = 0
    for numbers in range(1,n+1):
        summa += numbers * numbers * numbers
    print(summa)


def metod_name():
    return int(input("Write number: "))


def out_numbers2(n):
    null = 0
    summa = 0
    while n > null:
        null += 1
        summa += null * null * null
    print(summa)

out_numbers(metod_name())
out_numbers2(metod_name())