import csv

class HashMap:
    def __init__(self):
        self.map = [[None for _ in range(6)] for _ in range(40)]
        with open("WGUPS Package Table.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader, None) # Skipping header
            for entry in reader:
                self.set_value(int(entry[0]), [entry[1], entry[5], entry[2], entry[4], entry[6], "HUB"])

    def hash_function(self, key, type=None):
        return key % 40

    def set_value(self, key, value, type=None):
        index = self.hash_function(key)
       
        if type == None:
            if isinstance(value, list) and len(value) == 6:
                self.map[index] = value
            else:
                print("If type is set to None, the value needs to be a list type of length 6.")
        if type == "address":
            self.map[index][0] = value
        if type == "deadline":
            self.map[index][1] = value
        if type == "city":
            self.map[index][2] = value
        if type == "zip":
            self.map[index][3] = value
        if type == "weight":
            self.map[index][4] = value
        if type == "status":
            self.map[index][5] = value # HUB, IN_TRANSIT, DELIVERED

        

    def get_value(self, key, type=None):
        index = self.hash_function(key)
        
        if type == None: 
            return self.map[index]
        else:
            if type == "address":
                return self.map[index][0]
            if type == "deadline":
                return self.map[index][1]
            if type == "city":
                return self.map[index][2]
            if type == "zip":
                return self.map[index][3]
            if type == "weight":
                return self.map[index][4]
            if type == "status":
                return self.map[index][5]

