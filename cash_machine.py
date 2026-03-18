from collections import OrderedDict

"""
Требуется выдать сумму средств amount, которую клиент может запросить в банкомате.
1 <= amount, целое число.
В банкомате загружены купюры: 1, 5, 10, 50, 100, 200, 500, 1000, 5000 руб.
Количество каждой из купюр задано целым неотрицательным числом.
Если запрос можно выполнить, то необходимо вернуть список кортежей (номинал, количество),
иначе выбросить исключение.
"""


class CashMachine:
    # экономим память, выключаем __dict__
    # total храним для оптимизации, чтобы всегда знать сразу, сколько есть денег в банкомате
    __slots__ = ('__money_store', '__total')

    # загрузку купюрами передаём как argument list кортежей
    # (500, 20) - где 500 - номинал, а 20 - количество купюр
    def __init__(self, *args):
        self.__money_store = OrderedDict()
        self.deposit(*args)

    def deposit(self, *args):
        for nominal, amount in args:
            # тут, если номинал уже есть в словаре, то плюсуется, иначе добавится новый номинал
            self.__money_store[nominal] = self.__money_store.get(nominal, 0) + amount

        # тут сортируем по убыванию номиналов, это нужно для жадного алгоритма
        self.__money_store = OrderedDict(sorted(self.__money_store.items(), key=lambda v: v[0], reverse=True))
        self.__total = sum(v[0] * v[1] for v in self.__money_store.items())

    def __repr__(self):
        # это для поддержки print
        return ', '.join((f'{nom}: {count}' for nom, count in self.__money_store.items())) + \
            f' = {self.__total} руб.'

    def withdraw(self, amount):
        amt = int(amount)
        if self.__total < amt:
            raise ValueError(f'Not enough money in cash machine, only {self.__total} available')

        if amt < 1:
            raise ValueError('Bad argument: amount should be 1 or greater')

        if amt == self.__total:
            result = list((it for it in self.__money_store.items() if it[1] > 0))
            self.__money_store.clear()
            self.__total = 0

            return result

        result = []
        snapshot = OrderedDict(self.__money_store)
        total_old = self.__total

        # тут идём от старших номиналов к младшим и пытаемся максимально выдать сумму старшими купюрами,
        # а остатки младшими
        for nominal in self.__money_store.keys():
            if amt >= nominal:
                count = min(amt // nominal, self.__money_store[nominal])
                if count > 0:
                    given_amount = nominal * count
                    result.append((nominal, count))

                    amt -= given_amount
                    self.__total -= given_amount
                    self.__money_store[nominal] -= count

                    # если мы уже собрали сумму, то дальше нет смысла идти
                    if amt == 0:
                        break

        # если нужных номиналов купюр не хватило, то откатываемся назад и сообщаем клиенту об этом
        if amt > 0:
            self.__money_store = snapshot
            self.__total = total_old
            raise ValueError(f'There is a lack of banknotes to satisfy {amount} руб. out')

        return result


cc = CashMachine((10, 5), (50, 7), (100, 9), (200, 10), (500, 5))
print(cc)
print(cc.withdraw(900))
print(cc)
