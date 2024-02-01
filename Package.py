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
        self.status = "HUB________________________"
        self.truck_id = 0
        self.distance_from_current_address = 0

        if deadline == "EOD":
            self.deadline = time.max.strftime("%H:%M:%S")
        else:
            self.deadline =  datetime.strptime(deadline, "%H:%M:%S %p").time()

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.notes, self.status)

