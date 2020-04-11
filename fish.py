class Country:

    def __init__(self, city):
        self.city = city
        self.__population = 0
        print("Создание объекта")

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        if isinstance(population,(int, float)) and population >= 0 and population <= 10000000:
            self.__population = population
        else:
            print("Не правильно указано население")

    def increase_population(self):
        self.__population = self.__population + 1

    def __str__(self):
        return f"city: {self.city}, population: {self.__population}" + """
     ^
                _______ ^^^
               | Ххххххй | _ ^^^^^ _
               | Ххххххй | | [] [] |
            ______ ххххх | | [] [] [] |
           | ++++++ | хххх | | [] [] [] | МЕТРОПОЛИС
           | ++++++ | хххх | | [] [] [] |
           | ++++++ | _________ [] [] |
           | ++++++ | = | = | = | = | = | [] |
           | ++++++ | = | = | = | = | = | [] [] |
___________ | ++ HH ++ | _HHHH__ | _________ _________ _________
         _______________ ______________ ______________
__________________ ___________ __________________ ____________

if __name__ == "__main__":
    city1 = Country("Toronto")
    # city1.population = 200000
    city1.increase_population()
    print(City1.city, city1.population)

    city2 = Country("Moskow")
    # city2.population = 300000
    city2.increase_population()
    print(city2.city, city2.population)

    city2.population = 300000
    city2.population = "Test"

    print("city2")