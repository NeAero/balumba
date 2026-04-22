print('Магия срезов')
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
first = data[:3]
last = data[7:10]
reserved = data[::-3]
nechet = data[1::2]
print(*data, sep = ', ')
print()
print('Первая тройка чисел:', *first)
print('Последняя тройка чисел:', *last)
print('Список в обратном порядке:', *reserved)
print('Числа с нечетными индексами:', *nechet)
