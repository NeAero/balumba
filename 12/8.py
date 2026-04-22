import random
print('Обмен значений')
A = [random.randint(1, 100) for i in range(5)]
print('Список чисел: ', *A)

min_A = A.index(min(A))

A[0], A[min_A] = A[min_A], A[0]

print('Измененная версия списка: ', *A)
