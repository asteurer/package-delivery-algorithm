# Student ID: 0101313524
from PackageMap import PackageMap
from Truck import Truck
from AddressList import AddressList
from datetime import time
from Utilities import *

def get_delivery_status(time_to_stop=None, package_lookup_id=None):
    # Initializing data structures
    address_list = AddressList()
    package_map = PackageMap(address_list)

    # Creating trucks
    truck1 = Truck(1)
    truck2 = Truck(2)

    #You are using nearest neighbor Greedy is not an algorithm, say djyskstras or brute force

    # Creating a snapshot object that stores the data from the time of the indicated snapshot across all truck deliveries
    time_param_result = []

    truck1.load([1, 2, 7, 8, 13, 14, 15, 16, 19, 20, 21, 29, 30, 33, 34, 39], package_map)
    truck1.deliver_packages(address_list, package_map, time_to_stop, package_lookup_id, time_param_result)

    truck2.time = time(9, 5)
    truck2.load([3, 4, 5, 6, 11, 17, 18, 25, 26, 28, 31, 32, 36, 37, 38, 40], package_map)
    truck2.deliver_packages(address_list, package_map, time_to_stop, package_lookup_id, time_param_result)

    truck1.time = time(10, 20)
    truck1.load([9], package_map)
    truck1.deliver_packages(address_list, package_map, time_to_stop, package_lookup_id, time_param_result)

    truck1.load([10, 12, 19, 22, 23, 24, 27, 35], package_map)
    truck1.deliver_packages(address_list, package_map, time_to_stop, package_lookup_id, time_param_result)

    if time_to_stop != None:
        print("\n" + time_param_result[0])
        print(f"\nStatus of all packages at time {time_to_stop}")
        time_param_result[1].print_packages()
        print("\n")
    

    total_mileage = truck1.mileage + truck2.mileage
    max_time = 0

    if truck1.time > truck2.time:
        max_time = truck1.time
    else:
        max_time = truck2.time

    print(f"\nThe trucks finished at {max_time} with a total distance of {total_mileage} miles traveled.")
    print(f"\nStatus of all packages as of {max_time}:")
    package_map.print_packages()

def main():
    # Requesting user interaction
    print("""
Please enter the number of the function you want to run:
1. View the delivery status of a package (all package data)
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