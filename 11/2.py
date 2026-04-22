print('Старинная задача')
for bull in range (1, 11):
    for cow in range (1, 21):
        for calve in range (1, 201):
            total_cost = bull * 10 + cow * 5 + calve * 0.5
            if total_cost == 100:
                print(f'Быки: {bull} | коровы: {cow} | телята: {calve}')
