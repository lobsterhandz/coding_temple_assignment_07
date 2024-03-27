# Implement Task 2 Quiz User
def take_quiz(questions):
    score = 0  # Keep track of the correct answers
    for question, correct_answer in questions:
        # Ask the question
        user_answer = input(question + " ")
        # Check if the answer is correct
        if user_answer.lower().strip() == correct_answer.lower().strip():
            print("Correct!")
            score += 1  # Increment the score for a correct answer
        else:
            print("Wrong. The correct answer is:", correct_answer)
    return score  # Return the final score after all questions have been asked

def run_quiz_game():
    # Our predefined list of quiz questions and answers
    quiz_questions = [
        ("Who created the Python programming language?", "Guido van Rossum"),
        ("What was the ship called in Star Trek?", "Enterprise"),
        ("What year was Python released?", "1991")
    ]
    
    # Take the quiz and get the score
    total_questions = len(quiz_questions)
    score = take_quiz(quiz_questions)
    
    # Provide feedback based on the score
    print(f"\nQuiz completed! You got {score} out of {total_questions} questions right.")
    if score == total_questions:
        print("Perfect score! Well done.")
    elif score >= total_questions / 2:
        print("Good job! You've got most of them right.")
    else:
        print("Nice try! Review and try again to improve.")

# Run the quiz game
run_quiz_game()
