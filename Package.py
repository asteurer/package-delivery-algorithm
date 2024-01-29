from datetime import datetime, time
class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes, current_address, address_object):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = weight
        self.notes = notes
        self.status = "HUB" # HUB, IN_TRANSIT, DELIVERED, AWAITING_ARRIVAL
        self.new_current_address(address_object, current_address) # creates distance_from_current_address

        if deadline == "EOD":
            self.deadline = time.max
        else:
            self.deadline =  datetime.strptime(deadline, "%H:%M:%S %p").time()

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.notes, self.distance_from_current_address)
    
    def new_current_address(self, address_object, current_address):
        distance = address_object.calculate_distance(self.address, current_address)
        self.distance_from_current_address = distance

