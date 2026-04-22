name_Sasha = False
count = 0
while True:
    name = input("Введите имена: ")
    if name == "Александра":
        name_Sasha = True
    elif name_Sasha and name != "Левон":
        count += 1
    elif name == "Левон":
        break
print()
print(f"В очереди еще {count} человека")
