class Car:

    def start(self, start):
        self.start = 10 
        print(start, "Поехали")
        
    def stop(self, stop):
        self.stop = 12 
        print(stop, "Приехали")

    def drive(self, howlong):
        distance = howlong*60
        return(distance)

    

new_car = Car()
new_start= Car()
new_stop= Car()


print(new_start.start(1))
print(new_car.drive(50))
print(new_stop.stop(2)) 


    

        