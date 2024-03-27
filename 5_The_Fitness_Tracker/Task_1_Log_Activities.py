# Initialize a list to keep track of activities and their durations
activities_log = []

def log_activity(activity_name, duration):
    activities_log.append((activity_name, duration))
    print(f"Logged: {activity_name} for {duration} minutes.")

# Example of logging some activities
log_activity('Dancing', 10)
log_activity('Swimming', 20)
log_activity('Biking', 15)
