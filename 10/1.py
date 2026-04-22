print('Кодовый замок')
true_pin = 4590
password = False
while True:
    pin = int(input('Введите пин-код: '))
    if pin == true_pin:
        password = True
        break
    else:
        print('Пин-код неверный')
print('Открыто')
