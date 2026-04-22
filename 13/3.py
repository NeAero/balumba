print("Windows OS")
file_path = input('Введите полный путь к файлу: ').strip()
path = file_path.split('\\')
print("Части пути: ")
for part in path:
    print(part)
print(f"\nВсего частей: {len(path)}")
