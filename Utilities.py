import re
from datetime import datetime

def get_time_input(id_type):
    # This is the only place the convert_to_military_time function is used, so I nested it
    def convert_to_military_time(input_time):
        if not re.match(r'^\d{1,2}:\d{2} [apAP][mM]$', input_time): # Regular expression to match the format 'hour:minute am/pm'
            return False
        
        try:
            parsed_time = datetime.strptime(input_time, '%I:%M %p') # Parse the time in 12-hour format and convert to 24-hour format
            return parsed_time.strftime('%H:%M')
        except ValueError: # If parsing fails, the time is invalid
            return False
    
    
    print(f"Please enter the {id_type} ID: ")
    id = None
    while True:
        id = input(f"{id_type} ID: ")
        if id < 1 or (id_type == "truck" and id > 3) or (id_type == "package" and id > 40):
            print(f"Invalid {id_type} ID")
        else:
            break

    print("Please enter a time in the format '03:00 pm' or '3:00 pm'")
    time = None
    while True:
        time = convert_to_military_time(input("End time: "))
        if time:
            break
        else:
            print("Please enter a valid time.")

    return [time, id]


