list_data = [5, '9', 4, None, '5', {}] # Массив для проверки

def get_max_multiplication_two_number(list_numbers): 
    # локальный массив
    format_list = []
    # записываем в локальный массив только числа
    for item in list_numbers:
        if isinstance(item, (int, float, complex)):
            format_list.append(item)
    # если элементов массива меньше 2 то None
    if len(format_list) < 2:
        return None
    # убираем повторяющиеся элементы массива
    format_list = list(set(format_list))
    # сортируем
    format_list.sort()
    # берем два последних элемента
    first_number = format_list[-1]
    two_number = format_list[-2]
    return first_number, two_number

print(get_max_multiplication_two_number(list_data))