print('Меню операций банкомата')
balance = 1000
while True:
    print('Меню')
    print('1. Узнать баланс')
    print('2. Снять 100 руб')
    print('3. Положить 100 руб')
    print('4. Выход')
    print()

    komanda = int(input('Выберите номер команды: '))

    if komanda == 1:
        print(f'Ваш баланс {balance} руб')
    elif komanda == 2:
        if balance >= 100:
            balance -= 100
            print('Снято 100 руб')
        else:
            print('Недостаточно средств')
    elif komanda == 3:
        balance += 100
        print('Зачислено 100 руб')
    elif komanda == 4:
        print('До свидания!')
        break
    else:
        print('Неверная команда')
