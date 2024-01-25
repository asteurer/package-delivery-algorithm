class Truck:
    def __init__(self):
        self.driver = False
        self.capacity = 16
        self.speed = 18
        self.packages = []
        self.mileage = 0
        self.address = "4001 South 700 East" # Instantiating truck address with the HUB address.
        self.depart_time = -1
        self.time = -1

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages, self.mileage, self.address, self.depart_time)
    
    def load(self, packages):
        if self.capacity +  len(packages) > 16 or not isinstance(packages, list):
            return False
        else:
            self.packages.append(packages)