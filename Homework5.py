immutable_var = 1,2,3,4
print(immutable_var)
#immutable_var[1] = 4       # Кортеж неизменяем для: хранения данных в которых нельзя допускать изменения
                             #                       оптимизации памяти(кортеж занимает меньше памяти чем список)
                                #                    удобства копирования(кортежу можно дать имя и использовать как ссылку)
mutable_list = [1,2,3,4]
mutable_list.append(immutable_var)
print(mutable_list)
mutable_list.extend('abcd')
print(mutable_list)
