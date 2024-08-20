def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
test_function()
# inner_function - вне фунции имя не определенно из-за чего терминал выдаёт ошибку