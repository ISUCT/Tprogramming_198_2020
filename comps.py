class Comp:

    def __init__(self, name):
        self.name = name
        self.__hdd = 0
        print("Создание объекта")

    @property
    def hdd(self):
        return self.__hdd

    @hdd.setter
    def hdd(self, hdd):
        if isinstance(hdd,(int, float)) and hdd >= 32 and hdd <= 100:
            self.__hdd = hdd
        else:
            print("Не правильно указан объем жесткого диска")

    def increase_hdd(self):
        self.hdd = self.hdd + 1

    def __str__(self):
        return f"name: {self.name}, hdd: {self.hdd}" + """
         _______
        |.-----.|
        ||x . x||
        ||_.-._||
        `--)-(--`
       __[=== o]___
      |:::::::::::|
      `-=========-`()
"""
if __name__ == "__main__":
    comp1 = Comp("Laptop")
    comp1.hdd = 42
    comp1.increase_hdd()
    print(comp1.name, comp1.hdd)

    comp2 = Comp("PC")
    comp2.hdd = 99
    comp2.increase_hdd()
    print(comp2.name, comp2.hdd)

    comp2.hdd = 101
    comp2.hdd = "Test"

    print(comp2)