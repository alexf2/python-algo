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


def order_tickets(tickets):
    if not tickets:
        return []

    tickets_mapper = {}  # тут будут билеты по depaerture, чтобы их можно было быстро обойти по цепочке
    departure_cities = set()
    arrival_cities = set()

    for ticket in tickets:
        tickets_mapper[ticket.departure] = ticket
        departure_cities.add(ticket.departure)
        arrival_cities.add(ticket.arrival)

    if len(departure_cities) != len(tickets):
        raise ValueError('Маршрут не может быть построен: найдены дубликаты городов отправления')

    # ищем разностью множеств тот город, которого нет в arrival: это и есть начало пути
    start_path_city = departure_cities - arrival_cities

    if not start_path_city:
        raise ValueError('Начальный город отправления не найден')
    if len(start_path_city) > 1:
        raise ValueError('Начальных городов несколько')

    result = []
    current_city = start_path_city.pop()  # достаём начальный город из множества

    # цикл пока это не финальный город: обходим билеты по маршруту
    while current_city in tickets_mapper:
        ticket = tickets_mapper[current_city]
        result.append(ticket)
        # перемещаемся в следующий город по маршруту
        current_city = ticket.arrival

    if len(result) != len(tickets):
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
