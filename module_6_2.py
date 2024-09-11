class Vehicle:
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        self.COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
        
class Sedan(Vehicle):
    
    def get_model(self):
        return f'Модель: {self._Vehicle__model}'
    
    def get_horsepower(self):
        return f'Мощность двигателя: {self._Vehicle__engine_power}'
    
    def get_color(self):
        return f'Цвет: {self._Vehicle__color}'
    
    def print_info(self):
        print(f'Модель: {self._Vehicle__model}')
        print(f'Мощность двигателя: {self._Vehicle__engine_power}')
        print(f'Цвет: {self._Vehicle__color}')
        print(f'Владелец: {self.owner}')
        
    def set_color(self, new_color):
        if new_color.lower() in self.COLOR_VARIANTS:
            self._Vehicle__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')
        

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()