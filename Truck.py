from datetime import datetime, timedelta, time

class Truck:
    def __init__(self, id):
        self.id = id
        self.packages = []
        self.mileage = 0
        self.address = "4001 South 700 East" # Instantiating truck address with the HUB address.
        self.time = time(8)

    
    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.id, self.packages, self.mileage, self.address, self.time)
    

    def load(self, package_id_list, package_map):
        isList = isinstance(package_id_list, list)
        if isList:
            if len(self.packages) > 16:
                raise Exception("You cannot have more than 16 packages")
        elif not isList:
            raise Exception("You can only pass a list of integers into this function")
        
        for package_id in package_id_list:
                package = package_map.get_package(package_id)
                package.status = "IN_TRANSIT"
                package.truck_id = self.id
                self.packages.append(package)

            
    
    def deliver_packages(self, address_list, package_map, time_to_stop=None, package_lookup_id=None):
        """
        Greedy Algorithm:
        1. The deadline is soon
        2. The package is delivered to the same house
        3. The destination is closer
        """
        def get_option_one_string(package_lookup_id):
            package = package_map.get_package(package_lookup_id)
            transit_string = ""

            if package.status == "IN_TRANSIT":
                transit_string = f"It is currently on truck {package.truck_id}."

            return f"Package {package_lookup_id} is in status {package.status}. {transit_string}"


        def calculate_travel_duration(distance):
            # Calculate total hours
            total_hours = distance / 18
            # Convert to timedelta
            return timedelta(hours=total_hours)
        
        
        def add_time_and_distance(distance):
            try:
                travel_duration = calculate_travel_duration(distance)

                # Convert truck.time to a datetime object
                current_datetime = datetime.combine(datetime.today(), self.time)

                # Add the travel duration
                new_datetime = current_datetime + travel_duration

                # Update truck.time with the new time
                self.time = new_datetime.time()
        
                """
                Stragglers Pseudo Code
                if the time is after 0905 and late packages are in AWAITING_ARRIVAL, set status to HUB
                if the time is after 1020 and the wrong address package is in AWAITING_INFORMATION_UPDATE, update address and set status to HUB
                if time_to_stop != None and package is in truck and self.time >= time_to_stop
                """
                
                if (self.time >= time(9, 5) and self.time < time(9, 35)) or time_to_stop >= time(9, 5):
                    late_arrivals = [6, 25, 28, 32]
                    for package_id in late_arrivals:
                        package = package_map.get_package(package_id)
                        if package.status == "AWAITING_ARRIVAL":
                            package.status = "HUB"
                        else:
                            break
                    
                if (self.time >= time(10, 20) and self.time < time(10,50)) or time_to_stop >= time(10, 20):
                    package = package_map.get_package(9)
                    if package.status == "AWAITING_INFORMATION_UPDATE":
                        package.address = "410 S. State St."
                        package.city = "Salt Lake City"
                        package.state = "UT"
                        package.zip = 84111
                        package.status = "HUB"

                if time_to_stop != None:
                    if time_to_stop >= self.time:
                        # TODO: Have better error handling
                        return get_option_one_string(package_lookup_id)


                # Adding the mileage on the truck
                self.mileage += distance 
            except ValueError:
                print(f"Invalid distance value: {distance}")


        isNotReturned = True # Prevents the rest of the code from running once true
        while len(self.packages) > 0:
            next_package = None

            # This determines the next best package to deliver
            for package in self.packages:
                if next_package == None:
                    next_package = package

                elif next_package.deadline == "EOD" and package.deadline == "EOD":
                    if next_package.distance_from_current_address > package.distance_from_current_address:
                        next_package = package

                elif next_package.deadline == "EOD" and package.deadline != "EOD":
                    next_package = package

                elif next_package.deadline != "EOD" and package.deadline != "EOD":
                    if next_package.deadline > package.deadline:
                        next_package = package
            
            # Checking to be sure that no other packages have the same address
            same_delivery_address_list = [next_package]
            for package in self.packages:
                if next_package.address == package.address and next_package != package:
                    same_delivery_address_list.append(package)

            # delivering the packages
            for package in same_delivery_address_list:
                package_map.get_package(package.id).status = "DELIVERED"
                self.packages.remove(package)
            
            # This breaks if we are running option one and the proper time has passed
            output = add_time_and_distance(next_package.distance_from_current_address)
            
            if output != None:
                isNotReturned = False
                return output # Returns False if error, else returning the output string.
            
            package_map.set_new_current_address(address_list, next_package.address)
            self.address = next_package.address

        # Return to the HUB
        if isNotReturned:
            distance = address_list.calculate_distance(self.address, "4001 South 700 East")
            add_time_and_distance(distance)
            self.address = "4001 South 700 East"
    



