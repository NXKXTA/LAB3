# 2
import math


def is_natural_and_positive(num):
    if num.isnumeric() and int(num) > 0:
        try:
            num = int(num)
            return True
        except ValueError:
            print("Введено не натуральное число")
            exit()
    print("Введено не натуральное число")
    exit()


def nod(a, b):
    if a > b:
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if (a % i == 0) and (b % i == 0):
            nod = i
    return nod


a = input("Ведите первое число:")
is_natural_and_positive(a)

b = input("Ведите второе число:")
is_natural_and_positive(b)

print(f"НОД моей функцией = {nod(int(a), int(b))}")
print(f"НОД функцией из math = {math.gcd(int(a), int(b))}")
