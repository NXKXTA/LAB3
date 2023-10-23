# 4
from datetime import *

# Ввод даты рождения
try:
    print("Введите дату рождения в формате ДД/ММ/ГГГГ")
    born_date = datetime.strptime(input(), "%d/%m/%Y")
except ValueError:
    print("Дата в неверном формате")
    exit()

# Сколько ему будет через 10000 дней
_10k_days = timedelta(days=10_000)
a_10k_days = born_date + _10k_days
print(f"10_000 дней ему исполнится в этот день: {a_10k_days}")

# Сколько ему будет через 1_000_000 минут
_1m_minutes = timedelta(minutes=1_000_000)
a_1m_minutes = born_date + _1m_minutes
print(f"1_000_000 минут ему исполнится в этот день: {a_1m_minutes}")

# Сколько ему будет через 1_000_000 минут
_1b_sec = timedelta(seconds=1_000_000_000)
a_1b_sec = born_date + _1b_sec
print(f"1_000_000_000 секунд ему исполнится в этот день: {a_1b_sec}")
