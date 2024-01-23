from HashMap import HashMap
from Package import Package
import re
from datetime import datetime

def deliver_packages():
    print("function: deliver packages")

def get_total_mileage():
    print("function: total mileage")

def get_delivery_status(start_time, end_time):
    print("function: delivery status")

import re
from datetime import datetime

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



def main():
    print(
        """
        Please enter the number of the function you want to run:
        1. View the delivery status of a package
        2. Total mileage driven by all trucks
        3. Deliver packages
        """
        )
    
    function_to_run= input("Please enter 1, 2, 3, or any other key to cancel: ")

    if function_to_run in ["1", "2", "3"]:
        if function_to_run == "1":
            print("Please enter a start time in the format '12:00 pm'")
            start_time = None
            while True:
                start_time = convert_to_military_time(input("Start time: "))
                if start_time:
                    break
                else:
                    print("Please enter a valid start time.")

            print("Please enter an end time in the format '12:00 pm'")
            end_time = None
            while True:
                end_time = convert_to_military_time(input("End time: "))
                if end_time:
                    break
                else:
                    print("Please enter a valid end time.")

main()