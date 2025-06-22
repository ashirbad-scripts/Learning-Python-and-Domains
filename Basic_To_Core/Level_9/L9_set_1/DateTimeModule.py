# Use the datetime module to print today’s date in 
# YYYY-MM-DD format.
import datetime

today = datetime.date.today()
print("Today's date is: ", today)
print("Today's date is: ", today.strftime("%d-%m-%y"))

# Another format
# Get only date
from datetime import date
today = date.today()
print("Today : ", today)



# Get current date and time
from datetime import datetime

now = datetime.now()
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print(now)
print(formatted)


# Get only time
from datetime import datetime
now = datetime.now()
currentTime = now.time()
print("Current time: ", currentTime)


# Create a specific date 
from datetime import date

specific_date = date(2022, 12, 25)
print("Specific date:", specific_date)


# Get a weekday of a date
from datetime import date
d = date.today()
print("Weekday (0=monday, 6=sunday): ", d.weekday()) # day of week


# Difference between two days
from datetime import date
d1 = date(2025, 5, 3)
d2 = date(2024, 4, 3)
diff = d1 - d2
print(diff)



# Add or subtract days from a date
from datetime import date, timedelta
today = date.today()
future = today + timedelta(days=10)
past = today - timedelta(days=10)

print("10 days in future: ", future)
print("10 days in past: ", past)


#  Build a Python timer that waits for X seconds and rings
import time
def startTimer(seconds):
    print(f"Timer started for {seconds} seconds")
    time.sleep(seconds)
    print("Time's up")

startTimer(5)