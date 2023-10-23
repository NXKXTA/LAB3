# 3
from datetime import *

# Ввод даты отправления
try:
    print("Введите дату отправления поезда в формате ДД/ММ/ГГГГ ЧЧ:ММ")
    start_date = datetime.strptime(input(), "%d/%m/%Y %H:%M")
except ValueError:
    print("Дата в неверном формате")
    exit()

# Ввод даты прибытия
try:
    print("Введите дату прибытия поезда в формате ДД/ММ/ГГГГ ЧЧ:ММ")
    finish_date = datetime.strptime(input(), "%d/%m/%Y %H:%M")
except ValueError:
    print("Дата в неверном формате")
    exit()

# Проверка на введённые даты в обратном порядке
if finish_date < start_date:
    print("Дата прибытия не может быть меньше даты отправления")
    exit()

# Время в пути
travel_time = finish_date - start_date
print(travel_time)
