class Dog:

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
  __      _
o'')}____//
 `_/      )
 (_(_/-(_/
        """

if __name__ == "__main__":
    dog1 = Dog("Leo")
    dog1.age = 10
    dog1.increase_age()
    print(dog1.name, dog1.age)

    dog2 = Dog("Yuuki")
    dog2.age = 2.3
    dog2.increase_age()
    print(dog2.name, dog2.age)

    dog2.age = 13
    dog2.age = "Test"

    print(dog2)


