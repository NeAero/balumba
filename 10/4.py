print('Кассовый аппарат')
sum = 0
while True:
    price = int(input('Введите стоимость товара: '))
    if price == 0:
        break
    if price < 0:
        print('Ошибка цены!')
        continue
    sum += price
if sum > 1000:
    print(f'Итоговая сумма составляет {sum} руб')
    print(f'Итоговая сумма с учетом скидки {sum * 0.9} руб')
else:
    print(f'Итоговая сумма составляет {sum} руб')
