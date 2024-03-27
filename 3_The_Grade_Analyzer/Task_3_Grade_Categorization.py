def categorize_grades(grades):
    # Check if the list isn't empty
    if not grades:
        print("No grades to categorize.")
        return
    
    for grade in grades:
        if grade >= 90:
            letter = 'A'
        elif grade >= 80:
            letter = 'B'
        elif grade >= 70:
            letter = 'C'
        elif grade >= 60:
            letter = 'D'
        else:
            letter = 'F'
        print(f"A score of {grade} is a letter grade {letter}.")

def calculate_average_grades():
    grades = []
    print("Enter your test scores one at a time. Press enter X2 to finish.")

    while True:
        grade_input = input("Enter a test score: ")
        if grade_input == "":
            break  # User finished entering grades
        else:
            try:
                grade = float(grade_input)  # Convert input to a number
                grades.append(grade)
            except ValueError:
                print("Please enter a number or just press enter to finish.")

    if grades: 
        average = sum(grades) / len(grades)
        print(f"The average score is: {average}")
      
        find_highest_and_lowest(grades)
        # Now also categorize and print each grade
        categorize_grades(grades)
    else:
        print("No grades were entered.")

# Including the function find_highest_and_lowest
def find_highest_and_lowest(grades):
    if grades:
        highest = max(grades)
        lowest = min(grades)
        print(f"The highest score is: {highest}")
        print(f"The lowest score is: {lowest}")

# Run the function
calculate_average_grades()
