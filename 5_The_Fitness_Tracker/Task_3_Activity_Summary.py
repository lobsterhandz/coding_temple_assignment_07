activities_log = [] 

def log_activity(activity_name, duration):
    activities_log.append((activity_name, duration))
    print(f"Logged: {activity_name} for {duration} minutes.")

def estimate_calories_burned():
    total_calories = 0
    for activity, duration in activities_log:
        calories = duration * 3.5
        print(f"{activity}: {calories} calories burned.")
        total_calories += calories
    return total_calories

def show_daily_summary():
    if not activities_log:
        print("No activities logged today.")
        return
    
    print("\nToday's Activity Summary:")
    total_calories_burned = estimate_calories_burned()
    print(f"Total calories burned today: {total_calories_burned}")
    
# Now, let's log some activities and show the summary.
log_activity('Dancing', 10)
log_activity('Swimming', 20)
log_activity('Biking', 15)

# Display the summary of all activities and total calories burned
show_daily_summary()
