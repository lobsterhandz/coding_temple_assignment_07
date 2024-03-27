# Initialize a list to keep track of activities and their durations
activities_log = [] 

def estimate_calories_burned():
    total_calories = 0
    for activity, duration in activities_log:
        calories = duration * 3.5
        print(f"{activity}: {calories} calories burned.")
        total_calories += calories
    return total_calories
