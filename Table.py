class Employee:
    name = "Employee"
    __date = "12.02.2018"
    def __init__(self, name):
        self.name = name
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        #if isinstance(date,(int, float)) and date >= "01.01.2018" and age <= "12.12.2018":
        self.__date = date



    def startWork(self):
        print(f"я{self.name}, я устроился на работу")

    def __str__(self):
        return f"name: {self.name}, date: {self.date}" + """
            |\_/|        D\___/\
            (0_0)         (0_o)
           ==(Y)==         (V)
----------(u)---(u)----oOo--U--oOo---
__|_______|_______|_______|_______|___
        """

if __name__ == "__main__":
    employee1 = Employee("Boris")
    employee1.date = "15.05.2018"


    print(employee1)
    employee2 = Employee("Olga")
    employee2.date = "01.10.2018"
    print(employee2)

    def __str__(self):
        return f"name: {self.name}, date: {self.date}" + """
            |\_/|        D\___/\
            (0_0)         (0_o)
           ==(Y)==         (V)
----------(u)---(u)----oOo--U--oOo---
__|_______|_______|_______|_______|___