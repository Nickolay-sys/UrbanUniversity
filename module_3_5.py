def get_multiplied_digits(number):      # функция подсчёта произведения цифр указанног числа
    str_number = str(number)        # преобразование значения параметра в строку
    # print(type(str_number))
    first = int(str_number[0])      # преобразование первого символа строки в число
    # print(str_number[0])
    # print(type(first))
    if int(len(str_number)) > 1:        # условие - если полученая цифра больше 1 то выполняется след строка
        return first * get_multiplied_digits(int(str_number[1:]))       # возвращение указаного значения с вызовом функции с указаными параметрами . Рекурсия
    if int(len(str_number)) <= 1:       # услов если цифра first меньше или равно 1 то выполняется след строка
        return first        # возврашение этой цифры
    
result = get_multiplied_digits(40203)
print(result)