# Import the datetime module
import datetime

# Get the current date
current_date = datetime.date.today()

# Set the target date (Christmas Day)
target_date = datetime.date(current_date.year, 12, 25)

# If the current date is after Christmas Day, set the target date to next year's Christmas Day
if current_date > target_date:
    target_date = datetime.date(current_date.year + 1, 12, 25)

# Calculate the number of days until Christmas Day
days_until_christmas = (target_date - current_date).days

# Print the number of days until Christmas Day
print(f"There are {days_until_christmas} days until Christmas!")
