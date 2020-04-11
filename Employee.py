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
        
    def increase_date(self):
        self.__date = self.__date + 1

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
    #employee1.date = "15.05.2018"
    employee1.increase_date()
    print(employee1.name, employee1.date)

    employee2 = Employee("Olga")
    employee2.increase_date()

    print(employee2.name, employee2.date)
    print(employee2)