def find_highest_and_lowest(grades):
    # Check if the list isn't empty
    if not grades:
        print("No grades to analyze for highest and lowest scores.")
        return

    # Find the highest and lowest grades
    highest = max(grades)
    lowest = min(grades)

    print(f"The highest score is: {highest}")
    print(f"The lowest score is: {lowest}")

def calculate_average_grades():
    grades = []
    print("Enter your scores one at a time. Press enter to finish.")

    while True:
        grade_input = input("Enter a test score: ")
        if grade_input == "":
            break  # User finished entering grades
        else:
            try:
                grade = float(grade_input)  # Convert input to number
                grades.append(grade)
            except ValueError:
                print("Please enter a number or just press enter to finish.")

    if grades:  # If the list isn't empty
        average = sum(grades) / len(grades)
        print(f"The average score is: {average}")
        # Now also find and print the highest and lowest grades
        find_highest_and_lowest(grades)
    else:
        print("No grades were entered.")

# Run the function
calculate_average_grades()