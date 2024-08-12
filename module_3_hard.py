data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]

def calculate_structure_sum(structure):
    counter = 0
    for item in structure:      # функция для перебора элементов
        # print(item, type(item))
        if isinstance(item, list|tuple|set):        # условие - если элемент принадлежит к одному из указаных классов то выполнить след строку 
            counter += calculate_structure_sum(item)        # прибавить к переменой counter результат функции с перебираемым параметром
        if isinstance(item, dict):      # условие - если элемент класса словарь то 
            for i in item:      # перебрать ключи 
                counter += len(i)       # и добавть длину каждого к переменной counter
            counter += sum(item.values())       # добавить сумму значенний словаря к переменой counter
        if isinstance(item , int):      # если элемент число 
            counter += item     # добавить к переменой counter
        if isinstance(item, str):       # если элемент строка
            counter += len(item)        # добавить длину строки к переменой counter
    return counter      # вернуть переменую
    

result = calculate_structure_sum(data_structure)
print(result)