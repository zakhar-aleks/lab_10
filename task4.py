import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print(f"Масив A: {a}")
print(f"Масив B: {b}")
print("-" * 30)

add = a + b
sub = a - b
mult = a * b
div = a / b

print("АРИФМЕТИЧНІ ОПЕРАЦІЇ:")
print(f"Сума (A + B):      {add}")
print(f"Різниця (A - B):   {sub}")
print(f"Добуток (A * B):   {mult}")
print(f"Частка (A / B):    {div}")
print("-" * 30)

combined_array = np.concatenate((a, b))

print("ОБ'ЄДНАННЯ:")
print(f"Об'єднаний масив: {combined_array}")
print("-" * 30)

max_val = combined_array.max()
min_val = combined_array.min()
total_sum = combined_array.sum()
product = np.prod(combined_array) 

print("СТАТИСТИКА ОБ'ЄДНАНОГО МАСИВУ:")
print(f"Максимальний елемент: {max_val}")
print(f"Мінімальний елемент:  {min_val}")
print(f"Сума елементів:       {total_sum}")
print(f"Добуток елементів:    {product}")