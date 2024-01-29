import csv
from Package import *

class PackageMap:
    def __init__(self, address_object):
        self.map = [None for _ in range(0, 40)]
        with open("WGUPS Package Table.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader, None) # Skipping header
            for entry in reader:
                package = Package(int(entry[0]), entry[1], entry [2], entry [3], entry [4], entry [5], entry [6], entry[7], "4001 South 700 East", address_object)

                if (int(entry[0]) in [6, 25, 28, 32, 9]): # Setting packages that haven't arrived
                    package.status = "AWAITING_ARRIVAL"

                self.set_package(package)


    def hash_function(self, key):
        return key % 40


    def set_package(self, package_object):
        self.map[self.hash_function(package_object.id)] = package_object


    def get_package(self, package_id):
        return self.map[self.hash_function(package_id)]
    
    def print_packages(self):
        for entry in self.map:
            print(f"ID: {entry.id}, Address: {entry.address}, City: {entry.city}, State: {entry.state}, Zip: {entry.zip}, Deadline: {entry.deadline}, Weight: {entry.weight}, Notes: {entry.notes}, Distance From Current Address: {entry.distance_from_current_address}, Status: {entry.status}")
