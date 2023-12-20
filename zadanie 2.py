# Создаем исходный словарь
original_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

# Применяем метод items() для получения объекта dict_items
items_object = original_dict.items()

# Создаем новый словарь, "обратный" исходному
reversed_dict = {value: key for key, value in items_object}

# Выводим результат
print("Исходный словарь:", original_dict)
print("Новый словарь (обратный):", reversed_dict)
