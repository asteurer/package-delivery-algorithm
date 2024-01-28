from datetime import time

class Truck:
    def __init__(self, id):
        self.id = id
        self.packages = []
        self.mileage = 0
        self.address = "4001 South 700 East" # Instantiating truck address with the HUB address.
        self.time = time(8)

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.id, self.packages, self.mileage, self.address, self.time)
    
    def load(self, packages):
        if len(self.packages) > 16:
            raise Exception("You cannot have more than 16 packages")
        else:
            self.packages.append(packages)