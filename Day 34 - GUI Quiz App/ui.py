from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window =  Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(bg="white", width=300, height=200)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.question_text = self.canvas.create_text(150, 100, text="Hello!", font=("Arial", 16, "italic"), fill=THEME_COLOR,
                                                     width=280)

        tick = PhotoImage(file=r"Day 34 - GUI Quiz App\images\true.png")
        self.tick_button = Button(image=tick, command=self.check_true)
        self.tick_button.grid(row=2, column=0)

        cross = PhotoImage(file=r"Day 34 - GUI Quiz App\images\false.png")
        self.x_button = Button(image=cross, command=self.check_false)
        self.x_button.grid(row=2, column=1, pady=20)

        self.score = Label(text="Score: ", bg=THEME_COLOR, fg="white", font=("Arial", 11, "bold"))
        self.score.grid(row=0, column=1, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions:
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.tick_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
 


