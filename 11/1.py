print('12 месяцев')
n = 0
k = 0
m = 0
for n in range (1, 13):
    for k in range (1, 12):
        for m in range (1, 11):
            if n*28 + k*30 + m*31 == 365:
                print(f'месяцев по 28 дней = {n}\nмесяцев по 30 дней = {k}\nмесяцев по 31 день = {m}')
