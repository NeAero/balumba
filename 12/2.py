print('Анализ цен')
prices = [1500, 500, 2000, 3500, 1000, 4500]
print('Цены:', *prices)
print(f'Самый дорогой: {max(prices)} руб')
print(f'Самый дешевый товар: {min(prices)} руб')
print(f'Общая стоимость всех товаров: {sum(prices)} руб')
print(f'Средняя цена товара: {sum(prices) // len(prices)} руб')
