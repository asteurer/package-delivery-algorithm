class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes, current_address, address_object):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.distance_from_current_address = self.new_current_address(address_object, self.address, current_address)
        self.status = "HUB" # HUB, IN_TRANSIT, DELIVERED

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.notes, self.distance_from_current_address)
    
    def new_current_address(self, address_object, current_address):
        self.distance_from_current_address = address_object.calculate_distance(self.address, current_address)
