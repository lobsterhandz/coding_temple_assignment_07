# Define a list of questions and answers
quiz_questions = [
    ("Who created the Python programming language?", "Guido van Rossum"),
    ("What was the ship called in Star Trek?", "Enterprise"),
    ("What year was Python released?", "1991")
]
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

