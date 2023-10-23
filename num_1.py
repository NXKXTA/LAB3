# 1
import math

try:
    a = float(input("Введите угол в градусах:"))
except ValueError:
    print("Введено неверное значение")
    exit()

angle_rad = math.radians(a)
sinus = math.sin(angle_rad)
print(f"sin({a}°) = {round(math.sin(angle_rad), 2)}")
print(f"cos({a}°) = {round(math.cos(angle_rad), 2)}")
print(f"tan({a}°) = {round(math.tan(angle_rad), 2)}")

# try:
#     grad = float(input("Введите угол в радианах:"))
# except ValueError:
#     print("Введено неверное значение")
#     exit()
#
# print(f"sin({grad}) = {math.sin(math.radians(grad))}")
# print(f"cos({grad}) = {math.cos(math.radians(grad))}")
# print(f"tan({grad}) = {math.tan(math.radians(grad))}")
