# Student ID: 0101313524
from HashMap import HashMap
from Package import Package
from Addresses import Addresses
from Utilities import *


def deliver_packages():
    print("function: deliver packages")


def get_total_mileage(start_end_time_list):
    print("function: total mileage")


def get_delivery_status(start_end_time_list):
    print("function: delivery status")    

def main():
    # Loading package data
    package_map = HashMap()

    # Loading address data
    addresses = Addresses()
    
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
#             deliver_packages(get_time_input())
#         elif function_to_run == "2":
#             get_total_mileage(get_time_input())
#         elif function_to_run == "3":
#             deliver_packages()
            

main()