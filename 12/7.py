print('Ручной поиск индекса')
numbers = [10, 20, 30, 40, 50]
num = int(input('Введите число: '))
found = False
for i in range(len(numbers)):
    if numbers[i] == num:
        print(f'{numbers[i]} имеется')
        found = True
        break
if not found:
    print('Нет такого числа')
