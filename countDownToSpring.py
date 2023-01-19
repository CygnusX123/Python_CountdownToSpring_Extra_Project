import time
from datetime import datetime
#import datetime

#x = datetime.datetime.now()
#print(x)

# Set the target date and time for the countdown to Spring 2023
targetDate = "03-20-2023 00:00:00"

# Convert the target date and time into a datetime object
targetDateTime = datetime.strptime(targetDate, "%m-%d-%Y %H:%M:%S")

# Get the current date and time
current_datetime = datetime.now()

# Calculate the difference between the target date and time and the current date and time
difference = targetDateTime - current_datetime

# Print the countdown message
print("Countdown to Spring", targetDate)

# Run the countdown loop
while difference.total_seconds() > 0:
    # Calculate the difference between the target date and time and the current date and time
    difference = targetDateTime - datetime.now()
    
    # Extract the number of days, hours, minutes, and seconds from the difference
    days, hours, minutes, seconds = difference.days, difference.seconds // 3600, difference.seconds // 60 % 60, difference.seconds % 60
    
    # Print the countdown message
    print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds remaining")
    
    # Sleep for 1 second
    time.sleep(1)

# Print the "countdown complete" message
print("Welcome Spring!")