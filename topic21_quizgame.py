from topic21_quizgame_questions import Question

question_prompts = [
    "\nWhat is the capital of Japan?\n(a) Seoul\n(b) Tokyo\n(c) Beijing\n\n",
    "\nWhich planet is known as the Red Planet?\n(a) Venus\n(b) Mars\n(c) Jupiter\n\n",
    "\nWhat programming language is known for its use in machine learning?\n(a) Python\n(b) JavaScript\n(c) Ruby\n\n"
]

questions= [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a" )
]

def run_quiz(questions):
    score=0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer.lower():
            score += 1
    print(f"\nYou got {score} out of {len(questions)} questions right!")        

run_quiz(questions)