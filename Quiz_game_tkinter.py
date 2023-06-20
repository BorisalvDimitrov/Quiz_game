import tkinter as tk
from quiz import quiz_questions
import random

score = 0
used_questions = []
rounds = 11


def end_game():
    if score == 100:
        question_label.config(text=f"Congrats!\n You are the absolute winner.\nYour result is {score:.2f}%")
    elif 50 <= score < 100:
        question_label.config(text=f"Good try!\n Your result is {score:.2f}%")
    else:
        question_label.config(text=f"You have to read more!\nYour result is {score:.2f}%")

    for buton in option_buttons:
        buton.destroy()

    root.after(10000, root.destroy)
    return


def check_answer(user_input, correct_answer, question_lab):
    global score
    if user_input == correct_answer:
        score += 10

    used_questions.append(question_lab.cget("text"))
    next_question()


def next_question():
    global rounds

    rounds -= 1
    if rounds == 0:
        end_game()
        return

    question_data = random.choice(quiz_questions)
    question, correct_answer, answer_options = question_data[0][0], question_data[1][0], question_data[2]

    if question not in used_questions:
        question_data = random.choice(quiz_questions)
        question, correct_answer, answer_options = question_data[0][0], question_data[1][0], question_data[2]

    question_label.config(text=question)
    result_label.config(text="")

    for x in range(len(answer_options)):
        option_buttons[x].config(text=answer_options[x])

    for i in range(4):
        option_buttons[i].config(
            command=lambda i=i: check_answer(option_buttons[i].cget("text"), correct_answer, question_label))


root = tk.Tk()
root.title("Quiz")
root.geometry("600x400")

question_label = tk.Label(root, text="Question", font=("Arial", 20))
question_label.pack(pady=10)

options_frame = tk.Frame(root, bg="black")
options_frame.pack(pady=10)

option_buttons = []
for _ in range(4):
    button = tk.Button(options_frame, font=("Arial", 12), width=30, bg="gray")
    button.pack(pady=0, ipady=4, fill=tk.BOTH)
    option_buttons.append(button)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="black")
result_label.pack(pady=10)

next_question()

root.configure(bg="black")
root.mainloop()

