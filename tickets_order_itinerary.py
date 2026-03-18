from dataclasses import dataclass

"""
Дан массив билетов. Он не упорядочен. Нужно вернуть массив билетов в порядке передвижения по маршруту. Петель и циклов нет.
"""


@dataclass
class Ticket:
    departure: str
    arrival: str

    def __str__(self):
        return f'{self.departure} --> {self.arrival}'


def order_tickets(ticket_data):
    if not ticket_data:
        return []

    tickets = {}  # тут будут билеты по depaerture, чтобы их можно было быстро обойти по цепочке
    start_cities = set()  # города departure
    end_cities = set()  # города arrival

    for td in ticket_data:
        tickets[td.departure] = td
        start_cities.add(td.departure)
        end_cities.add(td.arrival)

    if len(start_cities) != len(ticket_data):
        raise ValueError('Маршрут не может быть построен: найдены дубликаты городов отправления')

    # ищем разностью множеств тот город, которого нет в arrival: это и есть начало пути
    start_path_city = start_cities - end_cities

    if not start_path_city:
        raise ValueError('Начальный город отправления не найден')
    if len(start_path_city) > 1:
        raise ValueError('Начальных городов несколько')

    result = []
    current_city = start_path_city.pop()  # достаём начальный город из множества

    # цикл пока это не финальный город: обходим билеты по маршруту
    while current_city in tickets:
        ticket = tickets[current_city]
        result.append(ticket)
        # перемещаемся в следующий город по маршруту
        current_city = ticket.arrival

    if len(result) != len(ticket_data):
        raise ValueError('В данных есть несвязанные сегменты')

    return result


# Проверка
tickets = (
    Ticket('Vancuver', 'Moscow'),
    Ticket('Berlin', 'London'),
    Ticket('London', 'Vancuver'),
    Ticket('NY', 'Berlin'),
)

print(*order_tickets(tickets), sep='\n')
print()

tickets = (
    Ticket('Москва', 'Иркутск'),
    Ticket('Лас-Вегас', 'Нью-Йорк'),
    Ticket('Хабаровск', 'Токио'),
    Ticket('Нью-Йорк', 'СПБ'),
    Ticket('Токио', 'Сиэтл'),
    Ticket('Сиэтл', 'Лас-Вегас'),
    Ticket('Иркутск', 'Хабаровск'),
)

print(*order_tickets(tickets), sep='\n')
