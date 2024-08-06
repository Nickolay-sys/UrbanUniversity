def print_params(a = 1, b = 'string', c = True):        # функция с установлеными по умолчанию параметрами
    print(a,b,c)        # вывод указаных параметров
print_params()      # вызов функции без аргументов
print_params(2)     # вызов функции с одним аргументом
print_params(3, 4)      # вызов функции с двумя аргументами
print_params(5, 6, 7)       # вызов функции с тремя аргументами
print_params(b = 25)        # вызов функции именного 
print_params(c = [1,2,3])       # вызов функции именного       


values_list = [2, 'строка', False]      # список элементов разных типов 
values_dict = {'a':2, 'b':'строка', 'c': False}     # словарь элементов разных типов
print_params(*values_list)      # распаковка списка
print_params(**values_dict)     # распаковка словаря


values_list_2 = [3, 'megastring']       
print_params(*values_list_2)        # распаковка списка
print_params(*values_list_2, 42)        # распаковка списка с заменой позиционного параметра