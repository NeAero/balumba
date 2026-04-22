print("Количество совпадающих пар")
numbers = list(map(int, input("Введите числа через пробел: ").split()))
pair_count = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            pair_count += 1

print(f"Количество совпадающих пар: {pair_count}")
