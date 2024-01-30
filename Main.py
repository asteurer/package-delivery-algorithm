# Student ID: 0101313524
from PackageMap import PackageMap
from Truck import Truck
from AddressList import AddressList
from Utilities import *

def get_delivery_status(time_to_stop=None, package_lookup_id=None):
    # Initializing data structures
    address_list = AddressList()
    package_map = PackageMap(address_list)

    # Creating trucks
    truck1 = Truck(1)
    truck2 = Truck(2)

    truck1.load([1, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 27, 34, 35, 39], package_map)
    truck2.load([4, 5, 7, 24, 29, 37, 38, 40], package_map)

    truck1_output = truck1.deliver_packages(address_list, package_map, time_to_stop, package_lookup_id)
    truck2_output = truck2.deliver_packages(address_list, package_map, time_to_stop, package_lookup_id)

    if truck1_output != None and time_to_stop != None:
        return truck1_output
    elif truck2_output != None and time_to_stop != None:
        return truck2_output
    
    truck2.load([2, 3, 6, 8, 18, 22, 23, 25, 26, 28, 30, 31, 32, 33, 36], package_map)
    
    truck2_output = truck2.deliver_packages(address_list, package_map, time_to_stop, package_lookup_id)
    
    truck1.load([9], package_map)

    truck1.output = truck1.deliver_packages(address_list, package_map, time_to_stop, package_lookup_id)

    if truck2_output != None and time_to_stop != None:
        return truck2_output
    if truck1_output != None and time_to_stop != None:
        return truck1_output
    

    total_mileage = truck1.mileage + truck2.mileage
    max_time = 0

    if truck1.time > truck2.time:
        max_time = truck1.time
    else:
        max_time = truck2.time

    print(f"The trucks finished at {max_time} with a total distance of {total_mileage} miles traveled.")

def main():
    # Requesting user interaction
    print("""
Please enter the number of the function you want to run:
1. View the delivery status of a package
2. View the total mileage of the trucks driven
""")
    
    function_to_run= input("Please enter 1, 2 or any other key to cancel: ")

    if function_to_run in ["1", "2"]:
        if function_to_run == "1":
            user_input = get_user_input()
            print(get_delivery_status(user_input[0], user_input[1]))
        elif function_to_run == "2":
            get_delivery_status()

main()