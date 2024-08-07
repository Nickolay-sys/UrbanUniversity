def single_root_words(root_word, *other_words):         # функция с непроизвольным и произвольными параметрами
    same_words = []         # пустой список в который будет возвращаться значения
    for word in other_words:        # цикл для перебора слов
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():          # условия на соответствие однокоренных слов
            same_words.append(word)         # добавляет подходящие слова в список
    return same_words           # возвращает значения
            
        


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)