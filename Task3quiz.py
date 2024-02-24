# Quiz questions and answers
quiz_questions = {
    "What is the process by which plants make their food?": ["A. Photosynthesis", "B. Respiration", "C. Transpiration", "D. Photophosphorylation"],
    "What is the outermost layer of a plant cell called?": ["A. Cell Membrane", "B. Cell Wall", "C. Both A&B", "D. None of the above"],
    "Which part of a plant absorbs water and minerals from the soil?": ["A. Stem", "B. Leaf", "C. Roots", "D. All of the above"],
    "Who wrote 'Romeo and Juliet'?": ["A. Charles Dickens", "B. Jane Austen", "C. William Shakespeare", "D. Mark Twain"],
    "What is the male reproductive organ of a flower?": ["A. Sepals", "B. Anther", "C. Stigma", "D. Stamen"]
}

# Function to present quiz questions
def present_quiz():
    score = 0
    for question, choices in quiz_questions.items():
        print(question)
        for choice in choices:
            print(choice)
        user_answer = input("Your Answer: ").strip().upper()
        correct_answer = "A"
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is: " + choices[0][3:])
    return score

# Function to play the quiz game
def play_quiz():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")
    print("-------------------------------")
    score = present_quiz()
    print("-------------------------------")
    print(f"Your Final Score: {score}/{len(quiz_questions)}")
    print("Thanks for playing!")

# Function to ask if the user wants to play again
def play_again():
    while True:
        again = input("Do you want to play again? (yes/no): ").lower()
        if again == "yes":
            return True
        elif again == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Main function to run the quiz game
def main():
    play_quiz()
    while play_again():
        play_quiz()
    print("Goodbye!")

if __name__ == "__main__":
    main()
