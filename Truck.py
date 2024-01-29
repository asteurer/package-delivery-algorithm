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
    
    # TODO: When a package is loaded, change the status to IN_TRANSIT
    def load(self, packages):
        if len(self.packages) > 16:
            raise Exception("You cannot have more than 16 packages")
        else:
            self.packages.append(packages)
    
    def deliver_packages(self, address_object, package_map):
        while len(self.packages) > 0:
            next_package = None

            # This determines the next best package to deliver
            for package in self.packages:
                if next_package == None:
                    next_package = package

                # TODO: This logic probably needs to incorporate calculate address.
                elif next_package.deadline == "EOD" and package.deadline == "EOD":
                    if next_package.distance_from_current_address > package.distance_from_current_address:
                        next_package = package

                elif next_package.deadline == "EOD" and package.deadline != "EOD":
                    next_package = package

                elif next_package.deadline != "EOD" and package.deadline != "EOD":
                    if next_package.deadline > package.deadline:
                        next_package = package
            
            # Checking to be sure that no other packages have the same address
            same_address_list = [next_package]
            for package in self.packages:
                if next_package.address == package.address:
                    same_address_list.append(package)

            # delivering the packages
            for package in same_address_list.reverse():
                package_map


