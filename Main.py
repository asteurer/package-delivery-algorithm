# Student ID: 0101313524

import re
import csv
from datetime import datetime
from HashMap import HashMap
from Package import Package


def deliver_packages():
    print("function: deliver packages")


def get_total_mileage(start_end_time_list):
    print("function: total mileage")


def get_delivery_status(start_end_time_list):
    print("function: delivery status")


def convert_to_military_time(input_time):
    # Regular expression to match the format 'hour:minute am/pm'
    if not re.match(r'^\d{1,2}:\d{2} [apAP][mM]$', input_time):
        return False
    
    try:
        # Parse the time in 12-hour format and convert to 24-hour format
        parsed_time = datetime.strptime(input_time, '%I:%M %p')
        return parsed_time.strftime('%H:%M')
    except ValueError:
        # If parsing fails, the time is invalid
        return False
    

def get_time_input():
    print("Please enter a start time in the format '03:00 pm' or '3:00 pm'")
    start_time = None
    while True:
        start_time = convert_to_military_time(input("Start time: "))
        if start_time:
            break
        else:
            print("Please enter a valid start time.")

    print("Please enter an end time in the format '03:00 pm' or '3:00 pm'")
    end_time = None
    while True:
        end_time = convert_to_military_time(input("End time: "))
        if end_time:
            break
        else:
            print("Please enter a valid end time.")

    return [start_time, end_time]


def calculate_distance(address1, address2):
    print("This is the distance that will be calculated")


def main():

    # Loading package data
    package_map= HashMap()
    with open("WGUPS Package Table.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader, None) # Skipping header
        for entry in reader:
            package_map.set_value(int(entry[0]), [entry[1], entry[5], entry[2], entry[4], entry[6], "HUB"])

    """
    TODO: The data as it's stored in the CSV doesn't seem right, so I think we should edit the data so it's more readable.
    """
    # Loading address data
    address_row = []
    address_col = []
    with open("WGUPS Distance Table.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for i, row in enumerate(reader):
            edited_row = [cell.replace("\n", "") for cell in row]
            if i == 0:
                address_row = edited_row[2:]
            else:
                address_col.append(edited_row[0])


    print(address_row)
    print(address_col)
    
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
            deliver_packages(get_time_input())
        elif function_to_run == "2":
            get_total_mileage(get_time_input())
        elif function_to_run == "3":
            deliver_packages()
            

main()