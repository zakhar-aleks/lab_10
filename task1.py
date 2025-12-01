def solve_task(B):
    negative_numbers = [x for x in B if x < 0]
    
    if not negative_numbers:
        print("У списку немає від'ємних чисел.")
        return B

    max_negative = max(negative_numbers)
    
    target_index = B.index(max_negative)
    
    print(f"Найбільший від'ємний елемент: {max_negative}")
    print(f"Індекс цього елемента: {target_index}")

    new_B = []
    for i in range(len(B)):
        if i < target_index:
            new_B.append(B[i] ** 2)
        else:
            new_B.append(B[i])
            
    return new_B

original_list = [2, 3, -10, 4, -2, 5, -8]

print("Початковий список:", original_list)
result_list = solve_task(original_list)
print("Результат:", result_list)