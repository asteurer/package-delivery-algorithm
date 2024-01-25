# Student ID: 0101313524
from HashMap import HashMap
from Truck import Truck
from Addresses import Addresses
from Utilities import *


def deliver_packages():
    print("function: deliver packages")


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
    truck3 = Truck()

    # Segregating packages by note type
    packages_with_no_notes = [1, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 29, 30, 31, 33, 34, 35, 37, 39, 40]
    delivered_together = [13, 14, 15, 16, 19, 20] # Effective deadline is 9:00
    only_truck_two = [3, 18, 36, 38]
    flight_delay = [6, 25, 28, 32] # Arrives at 09:05
    wrong_address = [9] # Arrives at 10:20
    
    # Requesting user interaction
    print("""
Please enter the number of the function you want to run:
1. View the delivery status of a package
2. Total mileage driven by all trucks
3. Deliver packages
""")
    
    function_to_run= input("Please enter 1, 2, 3, or any other key to cancel: ")

    if function_to_run in ["1", "2", "3"]:
        if function_to_run == "1":
            get_delivery_status(get_time_input("package"))
        elif function_to_run == "2":
            get_total_mileage(get_time_input("truck"))
        elif function_to_run == "3":
            deliver_packages()
            

main()