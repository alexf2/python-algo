"""
Есть две целочисленные переменные: надо их поменять местами без использования третьей.
"""
value_a = 12
value_b = 197

# способ 1: через рапаковку кортежей
(value_a, value_b) = (value_b, value_a)

print(value_a, value_b)

value_a = 12
value_b = 197

# способ 2, через XOR
value_a ^= value_b
value_b ^= value_a
value_a ^= value_b

print(value_a, value_b)
