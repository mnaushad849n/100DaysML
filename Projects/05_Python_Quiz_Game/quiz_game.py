QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def",
    },
    {
        "question": "Which data type stores True or False values?",
        "options": ["string", "integer", "boolean", "list"],
        "answer": "boolean",
    },
    {
        "question": "Which symbol starts a comment in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#",
    },
    {
        "question": "Which built-in function shows output on the screen?",
        "options": ["input", "print", "show", "display"],
        "answer": "print",
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": ["list", "tuple", "dictionary", "set"],
        "answer": "dictionary",
    },
]


def ask_question(question_number, question_data):
    print(f"\nQuestion {question_number}: {question_data['question']}")

    for index, option in enumerate(question_data["options"], start=1):
        print(f"{index}. {option}")

    while True:
        choice = input("Your answer (1-4): ").strip()

        if choice in {"1", "2", "3", "4"}:
            selected = question_data["options"][int(choice) - 1]
            break

        print("Please enter a number from 1 to 4.")

    if selected == question_data["answer"]:
        print("Correct!")
        return 1

    print(f"Wrong. Correct answer: {question_data['answer']}")
    return 0


def show_result(score, total_questions):
    percentage = (score / total_questions) * 100

    print("\nQuiz Complete")
    print("-" * 30)
    print(f"Score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.0f}%")

    if percentage == 100:
        print("Excellent work.")
    elif percentage >= 60:
        print("Good progress. Keep practicing.")
    else:
        print("Review the basics and try again.")


def main():
    print("Python Basics Quiz")
    print("Choose the correct option for each question.")

    score = 0

    for question_number, question_data in enumerate(QUESTIONS, start=1):
        score += ask_question(question_number, question_data)

    show_result(score, len(QUESTIONS))


if __name__ == "__main__":
    main()
