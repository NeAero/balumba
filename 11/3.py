print('Гипотеза Эйлера о сумме степеней')
for a in range (1, 151):
    for b in range (1, 151):
        for c in range (1, 151):
            for d in range (1, 151):
                sum = a**5 + b**5 + c**5 + d**5

                for e in range (1, 151):
                    if e**5 == sum:
                        print(f'a⁵ + b⁵ + c⁵ + d⁵ = e⁵')
                        print(f'Сумма равняется: {a + b + c + d + e}')
