class Truck:
    def __init__(self, packages, depart_time):
        self.capacity = 16
        self.speed = 18
        self.packages = packages
        self.mileage = 0
        self.address = """
        Western Governors University
        4001 South 700 East,
        Salt Lake City, UT 84107"""
        self.depart_time = depart_time
        self.time = depart_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages, self.mileage, self.address, self.depart_time)
    
    def load(self, packages):
        if self.capacity +  len(packages) > 16 or not isinstance(packages, list):
            return False
        else:
            self.packages.append(packages)