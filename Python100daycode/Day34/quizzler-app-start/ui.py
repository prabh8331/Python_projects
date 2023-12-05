from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz= quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.title("The Quizzler?")


        self.right_button_img = PhotoImage(file="Python100daycode/Day34/quizzler-app-start/images/true.png")
        self.right_button = Button(image=self.right_button_img,
                                   command=self.right_button_fun,
                                   highlightthickness=0,
                                   relief="groove")
        
        self.wrong_button_img = PhotoImage(file="Python100daycode/Day34/quizzler-app-start/images/false.png")
        self.wrong_button = Button(image=self.wrong_button_img,
                                   command=self.wrong_button_fun,
                                   highlightthickness=0,
                                   relief="groove")
        
        self.right_button.grid(row=2,column=1,padx=10,pady=10)
        self.wrong_button.grid(row=2,column=2,padx=10,pady=10)

        self.canvas = Canvas(width=300, height=250,highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, 
                                                     width= 280,
                                                     text="Some Question text",
                                                     font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=1,columnspan=2,padx=10,pady=30)


        self.score = Label(text="Score: 0/0",background=THEME_COLOR,fg="white",font=("Arial",13))
        self.score.grid(row=0,column=2,padx=20,pady=20)

        self.get_next_question()

        self.window.mainloop()
     

    def right_button_fun(self):
        # print("clicked")
        if self.quiz.check_answer("True"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)



    def wrong_button_fun(self):
        # print("clicked")
        if self.quiz.check_answer("True"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(2000, self.get_next_question)


    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= f"You've reached the end of the quiz. Final score is {self.quiz.score}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")