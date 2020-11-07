from random import randint

drive_number = randint(0, 100)


class Car:

    def __init__(self, name="", fuel=0):

        self.name = name
        self.fuel = fuel
        self.odo = 0

    def __str__(self):
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel,
                                                 self.odo)

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odo += distance
        return distance


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=0):
        Car.__init__(self, name, fuel)
        self.reliability = reliability
        self.drive = False

    def drive(self, distance):
        if drive_number < self.reliability:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odo += distance
        return distance
