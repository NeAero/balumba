print('Все вместе')
num = int(input('Введите число: '))
count_3 = 0
count_last = 0
count_chet = 0
sum_bolshe_5 = 0
prod_bolshe_7 = 1
count_0_and_5 = 0
last_num = num % 10
if_bolshe_7 = False
temp = num
while temp > 0:
    digit = temp % 10

    if digit == 3:
        count_3 += 1

    if digit == last_num:
        count_last += 1

    if digit % 2 == 0:
        count_chet += 1

    if digit > 5:
        sum_bolshe_5 += digit

    if digit > 7:
        prod_bolshe_7 *= digit
        if_bolshe_7 = True

    if digit == 0 or digit == 5:
        count_0_and_5 += 1

    temp //= 10

if not if_bolshe_7:
    prod_bolshe_7 = 1

print(f'Количество троек: {count_3}')
print(f'Последняя цифра встречается {count_last} раз')
print(f'Количество четных цифр: {count_chet}')
print(f'Сумма цифр больше 5 равняется {sum_bolshe_5}')
print(f'Произведение цифр, больших семи, равняется {prod_bolshe_7}')
print(f'5 и 0 встречаются {count_0_and_5} раз')
