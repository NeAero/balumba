print('Ручной подсчет')
marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]
count_5 = 0
count_2 = 0
for score in marks:
    if score == 5:
        count_5 += 1
    elif score == 2:
        count_2 += 1
print('Оценки:', *marks, sep = ' ')
print(f'Количество пятерок: {count_5}')
print(f'Количество двоек: {count_2}')
