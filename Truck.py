class Truck:
    def __init__(self):
        self.id = 0
        self.packages = []
        self.mileage = 0
        self.address = "4001 South 700 East" # Instantiating truck address with the HUB address.
        self.time = -1
        self.distance = 0

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages, self.mileage, self.address, self.depart_time)
    
    def load(self, packages):
        if len(self.packages) > 16:
            raise Exception("You cannot have more than 16 packages")
        else:
            self.packages.append(packages)