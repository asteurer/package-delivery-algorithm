# Student ID: 0101313524
from HashMap import HashMap
from Truck import Truck
from Addresses import Addresses
from Utilities import *
from datetime import datetime, time, timedelta
import math


def deliver_packages(truck, hash_map, addresses):
    """
    Greedy Params:
    1. Deadline
    2. PackageWithSameAddress
    3. Distance
    """ 
    def safe_float_conversion(input_string):
        try:
            if input_string == '':
                raise ValueError("Input string is empty")
            return float(input_string)
        except ValueError as e:
            print(f"Error converting '{input_string}' to float: {e}")
            return None  # Or return math.inf as appropriate for your logic


    def safe_datetime(deadline):
        if deadline != "EOD":
            return datetime.strptime(deadline, "%H:%M:%S %p").time()
        return time.max  # Return a high value for "EOD" so it's considered the least urgent
    
    def calculate_travel_duration(distance):
        # Calculate total hours
        total_hours = distance / 18
        # Convert to timedelta
        return timedelta(hours=total_hours)
    
    def add_time(address1, address2):
        distance_str = addresses.calculate_distance(address1, address2)
        print(f"distance: {distance_str}")

        try:
            distance = float(distance_str)
            travel_duration = calculate_travel_duration(distance)

            # Convert truck.time to a datetime object
            current_datetime = datetime.combine(datetime.today(), truck.time)

            # Add the travel duration
            new_datetime = current_datetime + travel_duration

            # Update truck.time with the new time
            truck.time = new_datetime.time()
        except ValueError:
            print(f"Invalid distance value: {distance_str}")
            
    
    

    has_deadlines = True

    while len(truck.packages) > 0:
        min_package_id = -1
        min_deadline_package_time = time.max

        if has_deadlines: # If there are packages with deadlines NOT EOD...
            for entry in truck.packages:
                deadline = safe_datetime(hash_map.get_value(entry, "deadline"))
                if deadline < min_deadline_package_time:
                    min_package_id = entry
                    min_deadline_package_time = deadline
                
            
            if min_package_id == -1:
                has_deadlines = False
                min_package_id = truck.packages[len(truck.packages) - 1]
        else:
            min_distance  = math.inf
            for entry in truck.packages:
                distance = safe_float_conversion(addresses.calculate_distance(hash_map.get_value(entry, "address"), truck.address))
                if distance == None:
                    distance = safe_float_conversion(addresses.calculate_distance(truck.address, hash_map.get_value(entry, "address")))
                if distance is not None and distance < min_distance:
                    min_package_id = entry

        
        # Marking the package as delivered
        hash_map.set_value(min_package_id, "DELIVERED", "status")
        truck.packages.remove(min_package_id)

        # Adding travel distance and setting new current address
        new_address = hash_map.get_value(min_package_id, "address")

        add_time(new_address, truck.address)
        truck.address = new_address

    
    # Adding the final trip to the hub
    add_time("4001 South 700 East", truck.address)
    truck.address = "4001 South 700 East"

    print(f"final time: {truck.time}")
        
        
    


        
        


def get_total_mileage(user_input):
    print("function: total mileage")


def get_delivery_status(user_input):
    print("function: delivery status")
    """
    Status:
    Truck:
    """

def main():
    # Loading package data
    package_map = HashMap()

    # Loading address data
    addresses = Addresses()

    # Instantiating trucks
    truck1 = Truck()
    truck2 = Truck()
    truck1.id = 1
    truck2.id = 2
    truck1.time = time(8)
    truck2.time = time(8)

    # Segregating packages by note type
    packages_with_deadlines = [1, 29, 30, 31, 34, 37, 40]
    packages_with_no_notes = [2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39]
    delivered_together = [13, 14, 15, 16, 19, 20] # Effective deadline is 9:00
    only_truck_two = [3, 18, 36, 38]
    flight_delay = [6, 25, 28, 32] # Arrives at 09:05
    wrong_address = [9] # Arrives at 10:20


    
    # Loading truck 1
    for entry in delivered_together:
        truck1.load(entry)
    
    for entry in packages_with_no_notes:
        if package_map.get_value(entry, "deadline") != "EOD":
            truck1.load(entry)
    
    for entry in packages_with_deadlines:
        truck1.load(entry)

    for entry in reversed(packages_with_no_notes):
        if len(truck1.packages) < 16:
            truck1.load(entry)
            packages_with_no_notes.remove(entry)
        else:
            break

    # Loading truck 2
    for entry in only_truck_two:
        truck2.load(entry)

    for entry in reversed(packages_with_no_notes):
        if len(truck2.packages) < 16:
            truck2.load(entry)
            packages_with_no_notes.remove(entry)
        else:
            break

    

    deliver_packages(truck1, package_map, addresses)
    # deliver_packages(truck2)


    
#     # Requesting user interaction
#     print("""
# Please enter the number of the function you want to run:
# 1. View the delivery status of a package
# 2. Total mileage driven by all trucks
# 3. Deliver packages
# """)
    
#     function_to_run= input("Please enter 1, 2, 3, or any other key to cancel: ")

#     if function_to_run in ["1", "2", "3"]:
#         if function_to_run == "1":
#             get_delivery_status(get_time_input("package"))
#         elif function_to_run == "2":
#             get_total_mileage(get_time_input("truck"))
#         elif function_to_run == "3":
#             deliver_packages()
            

main()