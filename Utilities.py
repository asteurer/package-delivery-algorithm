import re
from datetime import datetime

def get_time_input():
    # This is the only place the convert_to_military_time function is used, so I nested it
    def convert_to_military_time(input_time):
        if not re.match(r'^\d{1,2}:\d{2} [apAP][mM]$', input_time): # Regular expression to match the format 'hour:minute am/pm'
            return False
        
        try:
            parsed_time = datetime.strptime(input_time, '%I:%M %p') # Parse the time in 12-hour format and convert to 24-hour format
            return parsed_time.strftime('%H:%M')
        except ValueError: # If parsing fails, the time is invalid
            return False
    

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
