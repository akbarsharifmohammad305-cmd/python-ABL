#Case Study 4: Smart Parking Fee Management
#1. Problem Statement
'''Calculate parking charges using entry and exit times, vehicle categories, overnight parking, daily limits and penalty conditions while validating time inputs.'''
#2. Objectives
'''	Validate time entries and determine parking duration.
	Apply category-based hourly rates and daily caps.
	Add a penalty when the vehicle remains beyond the allowed duration.'''
#3. Assumptions
'''	Time format is 24-hour HH:MM on the same or following day.
	If exit time is earlier than entry time, exit is assumed to be on the next day.
	Rates and caps are illustrative and can be changed.'''


#4. Algorithm
'''Step 1: Read entry time, exit time and vehicle category.
Step 2: Validate time format and category.
Step 3: Calculate duration in minutes, accounting for overnight parking.
Step 4: Calculate hours charged, category rate and daily cap.
Step 5: Add any applicable penalty and display the bill.'''


#5. Flowchart
'''Start -> Read and validate input -> Process calculations and conditions -> Display results -> Stop'''


#6. Pseudocode
'''BEGIN
  READ entry, exit, vehicle category
  VALIDATE time values
  duration <- exit minutes - entry minutes
  IF duration < 0 THEN duration <- duration + 1440
  hours <- ceiling(duration / 60)
  fee <- min(hours * rate, daily cap)
  IF duration > allowed duration THEN fee <- fee + penalty
  PRINT duration and fee
END'''


#7. Python Source Code
from math import ceil
 
rates = {"CAR": 30, "BIKE": 15, "VAN": 50}
daily_caps = {"CAR": 250, "BIKE": 120, "VAN": 400}
allowed_hours = 24
penalty = 200
 
def to_minutes(value):
    parts = value.split(":")
    if len(parts) != 2:
        raise ValueError
    hour, minute = int(parts[0]), int(parts[1])
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        raise ValueError
    return hour * 60 + minute
 
try:
    entry = to_minutes(input("Entry time (HH:MM): "))
    exit_time = to_minutes(input("Exit time (HH:MM): "))
    vehicle = input("Vehicle type (CAR/BIKE/VAN): ").upper()
 
    if vehicle not in rates:
        print("Invalid vehicle cate")
    else:
        duration = exit_time - entry
        if duration < 0:
            duration += 24 * 60  # overnight parking
        hours = ceil(duration / 60)
        base_fee = min(hours * rates[vehicle], daily_caps[vehicle])
        extra_penalty = penalty if duration > allowed_hours * 60 else 0
        total = base_fee + extra_penalty
        print(f"Parking duration: {duration // 60} hours "
              f"{duration % 60} minutes")
        print("Hourly charge before cap: Rs", hours * rates[vehicle])
        print("Daily cap: Rs", daily_caps[vehicle])
        print("Penalty: Rs", extra_penalty)
        print(f"Total parking fee: Rs {total:.2f}")
except (ValueError, IndexError):
    print("Invalid time. Use 24-hour HH:MM format.")


#8. Test Case and Expected Output
'''Example: entry 22:30, 
            exit 01:15, 
            vehicle BIKE. 
            Duration = 2 hours 45 minutes; 
            3 billable hours x rupees 15 = rupees 45.'''

        
#9. Conclusion
'''The fee manager validates time input, supports overnight stays and applies vehicle-specific rates and daily caps before calculating the final charge.'''





 



