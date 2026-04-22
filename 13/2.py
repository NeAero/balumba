print("Символы всех строк")
n = int(input("Введите количество строк: "))
all_simvoli = []
for _ in range(n):
    text_line = input("Введите строку: ")
    all_simvoli.extend(list(text_line))
print(f"Список всех символов: {all_simvoli}")
