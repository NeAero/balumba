labirint = input('введите 25 символов в лабиринт: ')

if len(labirint) != 25:
    print('ошибка должно быть 25 символов')
else:
    n_index = labirint.find('H')
    if n_index == -1:
        print('ошибка вход в лабиринт не найден')
    else:
        row_n = n_index // 5
        col_n = n_index % 5
        print(f'вход в лабиринт находится в строке {row_n} и столбце {col_n}')
    f_index = labirint.find('ф')
    if f_index == -1:
        print('нету выхода апо')
    else:
        row_f = f_index // 5
        col_f = f_index % 5
        distant = abs(row_n - row_f) + abs(col_n - col_f)
        print(f'выход находится в строке {row_f} и столбце {col_f}')
        print(f'кол-во шагов которое нужно пройти {distant}')
coin = labirint.count('M')
print(f'монеты в лабиринте {coin}')
full_hp = 100
trapa = labirint.count('n')
enemin = labirint.count('B')
damag = trapa * 10 + enemin * 50
bol = full_hp - damag
heart_ostalos = bol // 10
lost = damag // 10
dislpayhp = '❤️' * heart_ostalos + '💔' * lost
print(f'здоровье игрока: {dislpayhp} ( осталось {heart_ostalos} очков здоровья')
