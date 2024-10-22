numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Вычисление среднего арифметического, исключая None
valid_numbers = list(filter(lambda x: x is not None, numbers))
average = sum(valid_numbers) / (len(valid_numbers) + 1)  # +1 для пропущенного элемента

# Замена None на среднее арифметическое
modified_numbers = list(map(lambda x: average if x is None else x, numbers))

print("Измененный список:", modified_numbers)
