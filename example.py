class Example:
    def __init__(self, v1: int, v2: str):
        self.v1 = v1
        self.v2 = v2
        self.reset()  # тут не хочу дублировать инициализацию полей, а хочу вызвать reset
        # self.a = ...
        # self.b = None

    def reset(self):
        self.a = 1
        self.b = 2

    def sum(self):
        return self.a + self.b


ex = Example(5, '12')
print(ex.v1)
print(ex.sum())
