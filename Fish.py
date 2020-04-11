class Fish:
    
    def __init__(self, name):
        self.name = name
        self.__age = 0
        print("Создание объекта")
    
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age,(int, float)) and age >= 0 and age <= 10:
            self.__age = age
        else:
            print("Не правильно указан возраст")

    def increase_age(self):
        self.__age = self.__age + 1

    def __str__(self):
        return f"name: {self.name}, age: {self.__age}" + """
      /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\´´\¸.·´
        """

if __name__ == "__main__":
    fish1 = Fish("Nemo")
    fish1.age = 10
    fish1.increase_age()
    print(fish1.name, fish1.age)

    fish2 = Fish("Dori")
    fish2.age = 2.3
    fish2.increase_age()
    print(fish2.name, fish2.age)

    fish2.age = 13
    fish2.age = "Test"

    print(fish2)
