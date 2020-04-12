class TV:
    def __init__(self, name):
        self. name = name
        self.__chanel = 0
        print("Создание объекта")

    @property
    def chanel(self):
        return self.__chanel

    @chanel.setter
    def chanel(self, chanel):
        if isinstance(chanel,(int, float)) and chanel >= 0 and chanel <= 100:
            self.__chanel = chanel
        else:
            print("Не правильно указано количество каналов")    

    def increase_chanel(self):
        self.__chanel = self.__chanel + 1
    
    def swim(self):
        print(f"я {self.name}, я показываю")

    def __str__(self):
        return f"name: {self.name}, chanel: {self.__chanel}" + """
      ______________
     |.------------.|
     ||  88::%%##  ||
     ||  88::%%##  ||
     ||  88::%%##  ||
 __  ||  88::%%##  ||
|==| ||____________||
|88| |[##] oo O [##]|
|88| |==sharp=======|
|__| |______________|
        """ 

if __name__ == "__main__":
    TV1 = TV("samsung")
    TV1.chanel = 99
    TV1.increase_chanel()
    print(TV1.name, TV1.chanel)
    TV1.swim()

    TV2 = TV("ld")
    TV2.chanel = 10
    TV2.increase_chanel()
    print(TV2.name, TV2.chanel)
    TV2.swim()

    TV2.chanel = 103
    TV2.chanel = "Test"

    print(TV2)