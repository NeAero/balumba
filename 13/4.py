print("Корректный IP‑адрес")
ip = input('Введите айпи: ').strip()
parts = ip.split('.')
is_valid= True
if len(parts) != 4:
    is_valid = False
else:
    for part in parts:
        if not part.isdigit():
            is_valid = False
            break
        num = int(part)
        if num < 0 or num > 255:
            is_valid = False
            break
if is_valid:
    print("ДА")
else:
    print('НЕТ')
