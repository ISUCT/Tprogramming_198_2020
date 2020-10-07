class Address:

    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = int(zipcode)

    def get_street(self):
        return self.street

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zipcode(self):
        return self.zipcode

    def str(self):
        print('Улица: {}, Город: {}, Область: {}, Индекс: {}'.format(self.street, self.city, self.state, self.zipcode))

address = Address('Смольная', 'Иваново', 'Ивановская', 156025)
address2 = Address('Революции', 'Кинешма', 'Ивановская', 155806)
address.str()
address2.str()
