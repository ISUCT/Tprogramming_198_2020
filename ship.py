class Ship:
    
    def __init__(self, name):
        self.name = name
        self.__length = 0
        print("Создание объекта")
    
    @property
    def length(self):
        return self.__length
        
    @length.setter
    def length(self, length):
        if isinstance(length,(int, float))and length >= 0 and length <= 10:
            self.__length = length
        else:
            print("Не правильно указана длинна")
    
    def increase_length(self):
        self.__length = self.__length + 1

    def run(self):
        print(f"Корабль: {self.name}")

    def __str__(self):
        return f"name: {self.name}, length: {self.__length}" + """
        ░░██████░░░░░░░░░░░░░░░░
░░░░░░░░████░░██░░░░░░░░░░░░░░░░
░░░░░░░░██░░░░██░░░░
░░░░░░░░██░░░░██░░░░░░░░░░░░░░░░
░░░░░░░░████████░░░░░░░░░░░░░░░░
░░░░░░░░░░░░████░░░░░░░░░░░░░░░░
████████████████████████████░░░░
░░██░░░░░░░░░░░░░░░░░░░░██░░░░░░
░░░░██░░░░░░░░░░░░░░░░██░░░░░░░░
░░░░░░████████████████░░░░░░░░░░
           ''''  ''''"""
    
if __name__ == "__main__":
    ship1 = Ship("Авианосец")
    ship1.length = 9
    ship1.increase_length()
    print(ship1.name, ship1.length)
    ship1.run()

    print(ship1)

    ship2 = Ship("Лодочка")
    ship2.length = 3.4
    ship2.increase_length()
    print(ship2.name, ship2.length)
    ship2.run()

    print(ship2)
