calls = 0

def count_calls():      # фунция подсчитывающая вызовы остальных функций
    global calls        # принимает глобальную переменную
    calls = calls + 1       # прибавляет 1
    #print(calls)     

def string_info(string):        # функция выводящаяч указанную информацию о строке
    print((len(string), string.upper(), string.lower()))
    count_calls()       # вызов фунции подсчёта
    
    
def is_contains(string, list_to_search):        # фунция проверяющая наличме строки в списке
    list_lowercase = [word.lower() for word in list_to_search]      # перевод списка в нижний регистр
    string_lowercase = string.lower()       # перевод строки в нижний регистр
    #print(string_lowercase)
    #print(list_lowercase)
    if string_lowercase in list_lowercase:      # условие - если строка в списке
            print(True)     # вывести True
    else:       #       условие - иначе
            print(False)        # вывести False
    count_calls()       # вызов функции подсчёта
    
string_info("Capybara")
string_info("Armageddon")
string_info("Назаваль")
string_info("Супрастин")
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
is_contains('Сон', ['Сомнабула', 'снотрворное', 'сОн'])
is_contains('Сова', ['Сотворение', 'СоВунЬя'])
print(calls)