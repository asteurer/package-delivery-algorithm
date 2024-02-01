from datetime import datetime, timedelta, time
import copy

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
        if not isList:
            raise Exception("You can only pass a list of integers into this function")
        
        for package_id in package_id_list:
            if len(self.packages) > 16:
                raise Exception("You cannot have more than 16 packages")
            else:
                package = package_map.get_package(package_id)
                package.status = "IN_TRANSIT_________________"
                package.truck_id = self.id
                self.packages.append(package)

            
    
    def deliver_packages(self, address_list, package_map, time_to_stop=None, package_lookup_id=None, result=None):
        # This is a function that updates a snapshot of the package_map that is unaltered past the time_to_stopS
        def update_result_map():
            if time_to_stop != None and self.time <= time_to_stop:
                for id in range(1, 41):
                    current_map = package_map.get_package(id)
                    outdated_map = result[1].get_package(id)

                    outdated_map.status = current_map.status
                    outdated_map.address = current_map.address
                    outdated_map.truck_id = current_map.truck_id

        # This creates the snapshot of the package_map and returns the status of the desired package
        def get_option_one_string(package_lookup_id, package):
            if len(result) == 0:
                package = package_map.get_package(package_lookup_id)
                transit_string = ""

                if package.status == "IN_TRANSIT_________________":
                    transit_string = f"It is currently on truck {package.truck_id}."
                
                output_string = f"Package {package_lookup_id} is in status {package.status}. {transit_string}"
                output_map = copy.deepcopy(package_map)
                result.append(output_string)
                result.append(output_map)
                


        def calculate_travel_duration(distance):
            # Calculate total hours
            total_hours = distance / 18
            # Convert to timedelta
            return timedelta(hours=total_hours)
        
        
        def add_time_and_distance(next_package, returnToHub=False):
            try:
                travel_duration = None
                distance = None

                # If the truck is not returning to the hub...
                if not returnToHub:
                    distance = next_package.distance_from_current_address
                    travel_duration = calculate_travel_duration(next_package.distance_from_current_address)
                else:
                    distance = next_package
                    travel_duration = calculate_travel_duration(distance)

                # Convert truck.time to a datetime object
                current_datetime = datetime.combine(datetime.today(), self.time)

                # Add the travel duration
                new_datetime = current_datetime + travel_duration

                # Update truck.time with the new time
                self.time = new_datetime.time()
      
                # Updates the status of the arriving packages once the time elapses past 09:05
                if self.time >= time(9, 5) or (time_to_stop != None and time_to_stop >= time(9, 5)):
                    late_arrivals = [6, 25, 28, 32]
                    for package_id in late_arrivals:
                        package = package_map.get_package(package_id)
                        if package.status == "AWAITING_ARRIVAL___________":
                            package.status = "HUB________________________"
                        else:
                            break
                    
                # Updates the status of the wrong-address package once the time elapses past 10:20
                if self.time >= time(10, 20) or (time_to_stop != None and time_to_stop >= time(10, 20)):
                    package = package_map.get_package(9)
                    if package.status == "AWAITING_INFORMATION_UPDATE":
                        package.address = "410 S. State St."
                        package.city = "Salt Lake City"
                        package.state = "UT"
                        package.zip = 84111
                        package.status = "HUB________________________"

                # If there is a need for a snapshot, and the time has elapsed past the time specified...
                if time_to_stop != None and not returnToHub:
                    if time_to_stop >= self.time:
                        get_option_one_string(package_lookup_id, next_package)
                
                # Updating the snapshot
                update_result_map()


                # Adding the mileage on the truck
                self.mileage += distance 
            except ValueError:
                print(f"Invalid distance value: {distance}")


        while len(self.packages) > 0:
            next_package = None

            # This determines the next best package to deliver
            for package in self.packages:
                if next_package == None:
                    next_package = package

                elif next_package.distance_from_current_address > package.distance_from_current_address:
                        next_package = package
            
            # Checking to be sure that no other packages have the same address
            same_delivery_address_list = [next_package]
            for package in self.packages:
                if next_package.address == package.address and next_package != package:
                    same_delivery_address_list.append(package)

            
            add_time_and_distance(next_package)

            # delivering the packages
            for package in same_delivery_address_list:
                package_map.get_package(package.id).status = f"DELIVERED_{self.time}_________"
                self.packages.remove(package)
            
            package_map.set_new_current_address(address_list, next_package.address)
            self.address = next_package.address

        # Return to the HUB
        distance = address_list.calculate_distance(self.address, "4001 South 700 East")
        add_time_and_distance(distance, True)
        self.address = "4001 South 700 East"
    



