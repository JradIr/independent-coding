trivia = {"What color is the sky?": "blue", "What is 2+2?": "4", "What color is the grass? " : "green"}

score = 0

for question, correct_answer in trivia.items():
    answer = input(f"{question}")
    if answer in correct_answer:
        score += 1
        print("you got it right")
    else:
        print("you got it wrong")

print(score)