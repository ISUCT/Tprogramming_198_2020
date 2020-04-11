class Pig:
    
    def __init__(self, name):
        self.name = name
        self.__weight = 0
        print("Создание объекта")
    
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if isinstance(weight,(int, float))and weight >= 0 and weight <= 10:
            self.__weight = weight
        else:
            print("Не правильно указано колличество")
    
    def increase_weight(self):
        self.__weight = self.__weight + 1

    def run(self):
        print(f"я {self.name}, я бегу, чтобы мня не убили")

    def __str__(self):
        return f"name: {self.name}, weight: {self.__weight}" + """
           _
         <`--'\>______
         /. .  `'     \.
        (`')  ,        @
         `-._,        /
            )-)_/--( >  jv
           ''''  ''''"""
    


if __name__ == "__main__":
    pig1 = Pig("Rita")
    pig1.weight = 10
    pig1.increase_weight()
    print(pig1.name, pig1.weight)
    pig1.run()

    pig2 = Pig("Rata")
    pig2.weight = 2.3
    pig2.increase_weight()
    print(pig2.name, pig2.weight)
    pig2.run()
    
    print(pig2)