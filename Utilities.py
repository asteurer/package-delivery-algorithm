import re
from datetime import datetime

def get_user_input():
    def convert_time(time_to_stop):
        if not re.match(r'^\d{1,2}:\d{2} [apAP][mM]$', time_to_stop): # Regular expression to match the format 'hour:minute am/pm'
            return False
        
        try:
            return datetime.strptime(time_to_stop, '%I:%M %p').time()
        except ValueError: # If parsing fails, the time is invalid
            return False
    
    id = None
    while True:
        id = input("Please enter the package ID: ")
        if int(id) not in range(1, 41):
            print(f"The package ID must be between 1 and 40.")
        else:
            break

    time = None
    while True:
        time = convert_time(input("Please enter a time in the format '03:00 pm' or '3:00 pm': "))
        if time:
            break
        else:
            print("Invalid time.")

    # IMPROVEMENT: I would create a class for user_input to make this return value more readable
    return [time, int(id)]