"""Quick quiz on Python functions. Run with: python functions_quiz.py"""


def ask(question, correct_answers):
    answer = input(question + " ").strip().lower()
    if answer in correct_answers:
        print("Correct!\n")
        return 1
    print(f"Not quite. Expected: {correct_answers[0]}\n")
    return 0


def run_quiz():
    score = 0
    total = 5

    print("=== Functions Quiz ===\n")

    score += ask(
        "1. What keyword sends a value back from a function?",
        ["return"],
    )

    score += ask(
        "2. What do we call the values inside the parentheses when calling a function? (one word)",
        ["arguments", "argument", "args"],
    )

    score += ask(
        "3. True or false: a function can both print and return a value.",
        ["true", "t"],
    )

    score += ask(
        "4. What is the default value of last_name in get_formal_greeting(first_name, last_name=\"\")?",
        ["empty string", '""', "blank", "nothing", ""],
    )

    score += ask(
        "5. Which function from functions.py checks if a name is not empty?",
        ["is_valid_name", "is valid name"],
    )

    print(f"Your score: {score}/{total}")
    if score == total:
        print("Great job! You understand functions well.")
    elif score >= 3:
        print("Good start. Review functions.py and try again.")
    else:
        print("Keep practicing. Re-read functions.py and your other challenge files.")


if __name__ == "__main__":
    run_quiz()
