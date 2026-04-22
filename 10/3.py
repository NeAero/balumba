print('Рекордсмен')
num = int(input('Введите число: '))
if num == 0:
    print('Ошибка❌ Нельзя начинать с нуля')
else:
    max_num = num
    while True:
        num = int(input('Введите число: '))
        if num == 0:
            break
        if num > max_num:
            max_num = num

    print(f'Максималное число: {max_num}')
