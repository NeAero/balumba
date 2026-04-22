print('Строго возрастающая последовательность')
num1 = int(input('Введите первое число: '))
while True:
    num2 = int(input('Введите второе число: '))
    if num2 > num1:
        break
    else:
        print('Ошибка❌ Второе число должно быть больше!')

while True:
    num3 = int(input('Введите третье число: '))
    if num3 > num2:
        break
    else:
        print('Ошибка❌ Третье число должно быть больше!')

print(f'Последовательность принята: {num1}, {num2}, {num3}')
