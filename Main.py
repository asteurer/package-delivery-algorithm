# Student ID: 0101313524
from PackageMap import PackageMap
from Truck import Truck
from AddressList import AddressList
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
    def safe_datetime(deadline):
        if deadline != "EOD":
            return datetime.strptime(deadline, "%H:%M:%S %p").time()
        return time.max  # Return a high value for "EOD" so it's considered the least urgent
    
    def calculate_travel_duration(distance):
        # Calculate total hours
        total_hours = distance / 18
        # Convert to timedelta
        return timedelta(hours=total_hours)
    
    def add_time_and_distance(address1, address2):
        distance = addresses.calculate_distance(address1, address2)
        print(f"Address1: {address1}, Address2: {address2}, Distance: {distance}")

        try:
            travel_duration = calculate_travel_duration(distance)

            # Convert truck.time to a datetime object
            current_datetime = datetime.combine(datetime.today(), truck.time)

            # Add the travel duration
            new_datetime = current_datetime + travel_duration

            # Update truck.time with the new time
            truck.time = new_datetime.time()

            # Adding the mileage on the truck
            truck.mileage += distance 
        except ValueError:
            print(f"Invalid distance value: {distance}")
            
    
    

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
                address1 = hash_map.get_value(entry, "address")
                address2 = truck.address
                distance = addresses.calculate_distance(address1, address2)

                if distance is not None and distance < min_distance:
                    min_package_id = entry

        
        # Marking the package as delivered
        hash_map.set_value(min_package_id, "DELIVERED", "status")
        truck.packages.remove(min_package_id)

        # Adding travel distance and setting new current address
        new_address = hash_map.get_value(min_package_id, "address")

        print(min_package_id)
        add_time_and_distance(new_address, truck.address)
        print(f"Current time: {truck.time}")
        truck.address = new_address

    
    # Adding the final trip to the hub
    add_time_and_distance("4001 South 700 East", truck.address)
    truck.address = "4001 South 700 East"

    print("HUB")
    print(f"\n\nStats for Truck {truck.id}: Time: {truck.time}, Miles: {truck.mileage}\n\n")

def get_total_mileage(user_input):
    print("function: total mileage")


def get_delivery_status(user_input):
    print("function: delivery status")
    """
    Status:
    Truck:
    """

def main():
    # Initializing data structures
    address_list = AddressList()
    package_map = PackageMap(address_list)

    

    # # Creating trucks
    # truck1 = Truck(1)
    # truck2 = Truck(2)
    # truck3 = Truck(3) # Load this one last. Once the other two are finished, return the closest one and send out truck3.

    # truck1.load([15, 16, 34, 40, 4, 14, 13, 39, 19])
    # truck2.load([5, 37, 38, ])
    # truck3.load([31, 32, ]) # delayed on flight + other non-priority deliveries.

    """
    Order of priorities:
    1. The deadline is soon
    2. The package is delivered to the same house
    3. The destination is closer
    """
    


    # deliver_packages(truck1, package_map, addresses)
    # deliver_packages(truck2, package_map, addresses)


    
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