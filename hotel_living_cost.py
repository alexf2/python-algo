# Необходимо написать функцию расчета стоимости проживания посетителя в отеле
# Функция может принимать 4 аргумента
# 1. Количество ночей проживания в отеле (обязательный параметр)
# 2. Дата заселения (необязательный параметр). Если значение не указано, то отсчет ведется от текущего дня
# Стоимость проживания в будние дни (с понедельника по пятницу) стоит 1500 руб.
# Стоимость проживания в выходные дни (суббота, воскресенье) стоит 2200 руб.

from datetime import date, timedelta
from decimal import Decimal

DAY_STEP = timedelta(days=1)


def get_total_cost(nights_count, check_in_date=None, *, weekday_cost=Decimal('1000'), weekend_cost=Decimal('1500')):
    if nights_count < 1:
        raise ValueError(f'Число ночей {nights_count} должно быть больше 0')
    if weekday_cost < 1 or weekend_cost < 1:
        raise ValueError('Стоимости проживания должны быть положительными')

    night = int(nights_count)
    curr_date = check_in_date or date.today()
    total_cost = Decimal('0')
    while night > 0:
        if curr_date.isoweekday() in (6, 7):
            total_cost += weekend_cost
        else:
            total_cost += weekday_cost

        curr_date += DAY_STEP
        night -= 1

    return total_cost


# Проверка
print(get_total_cost(7, date(2026, 3, 20), weekday_cost=Decimal('1500'), weekend_cost=Decimal('2200')))
