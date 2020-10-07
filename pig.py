class Table:
    name = "Table"
    age = 5
    def __init__(self, name):
        self.__age = 0
        print("Создание объекта")

    @property
    def age(self):
        return self.__age

    def increase_age(self):
        self.__age += 1

    @age.setter
    def age(self, age):
        if isinstance(age, (int, float)) and age in range(0,10):
            self.__age = age
        else:
            print("не правильно установлен размер")
    def increase_age(self):
        self.__age = self.__age +1

    def swim(self):
        print(f"я {self.name}, стоит")
    def __str__(self):
        return f"name:{self.name}, age: {self.__age}" + """
        
                     ,%;,
                     ,%%,
        ______________)(______________
       /             (__)             \
      /________________________________\
      [________________________________]
         \ \  / /            \ \  / /
          \ \/ /              \ \/ /
          _\/ /________________\ \/_
         [_/o/__________________\o\_]
          / /\ \              / /\ \
         lc/  \_\            /_/  \_\
"""
if __name__=="__main__":
    table1 = Table("Rita")
    # table1.age - 10
    table1.increase_age()
    print(table1.name, table1.age)

    table2 = Table("Rata")
    # table2.age = 2
    table2.increase_age()
    print(table2.name, table2.age)