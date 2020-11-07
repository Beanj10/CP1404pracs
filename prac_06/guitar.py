class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 0
        self.vintage = False

    def __str__(self):
        return "{} ({}): ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        self.age = 2020 - self.year
        return self.age

    def is_vintage(self):
        if self.age >= 50:
            self.vintage = True
        else:
            self.vintage = False
        return self.vintage