def calculate_average_grades():
    grades = []
    print("Enter your test scores one at a time. Press enter to finish.")

    while True:
        grade_input = input("Enter a test score: ")
        if grade_input == "":
            break  # User finished entering grades
        else:
            try:
                grade = float(grade_input)  # Convert input to a number
                grades.append(grade)
            except ValueError:
                print("Please enter a valid number or just press enter to finish.")

    if grades:  # If the list isn't empty
        average = sum(grades) / len(grades)
        print(f"The average score is: {average}")
    else:
        print("No grades were entered.")

# Run the function
calculate_average_grades()
