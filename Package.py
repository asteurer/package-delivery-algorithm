class Package:
    def __init__(self, weight, status, deadline, address, city, zip):
        self.weight = weight; 
        self.status = status; 
        self.deadline = deadline; 
        self.address = address; 
        self.city = city; 
        self.zip = zip; 

    def __str__(self): 
        return "%s, %s, %s, %s, %s, %s" % (self.weight, self.status, self.deadline, self.address, self.city, self.zip)
    
    def map_array(self):
        return [self.address, self.deadline, self.city, self.zip, self.weight, self.status]