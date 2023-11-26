BACKGROUND_COLOR = "#B1DDC6"

from tkinter import * 

import pandas
import random


try:
    data = pandas.read_csv("Python100daycode/Day31/flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("Python100daycode/Day31/flash-card-project-start/data/french_words.csv")
finally:
    df = data.to_dict(orient="records")

###--------------UI SETUP-------------------------#
window = Tk()

window.title("The Flashy: Learn Language Flash Cards")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)

card_front = PhotoImage(file="Python100daycode/Day31/flash-card-project-start/images/card_front.png")
card_back = PhotoImage(file="Python100daycode/Day31/flash-card-project-start/images/card_back.png")
right_button_img = PhotoImage(file="Python100daycode/Day31/flash-card-project-start/images/right.png")
wrong_button_img = PhotoImage(file="Python100daycode/Day31/flash-card-project-start/images/wrong.png")

card = canvas.create_image(400,263, image=card_front)
canvas.grid(row=1,column=1,columnspan=3,rowspan=4)

title_text = canvas.create_text(400,150, text="title",font=("Arial",40,"italic"))
word_text = canvas.create_text(400,263, text="word",font=("Arial",60,"bold"))


def result_word(word):
    canvas.itemconfig(title_text,text="English",fill="white")
    canvas.itemconfig(word_text,text=word,fill="white")
    canvas.itemconfig(card, image=card_back)


def pick_word():
    global timer, french_word, english_word, df, data
    try:
        word = random.choice(df)
    except IndexError:
        data = pandas.read_csv("Python100daycode/Day31/flash-card-project-start/data/french_words.csv")
        df = data.to_dict(orient="records")
        word = random.choice(df)

    french_word=word['French']
    english_word=word['English']
    canvas.itemconfig(title_text,text="French",fill="black")
    canvas.itemconfig(word_text,text=french_word,fill="black")
    canvas.itemconfig(card, image=card_front)
    timer = window.after(3000, result_word, english_word)
    


def right_button_function():
    window.after_cancel(timer)
    global data, df
    data=data[data["French"]!=french_word]
    data.to_csv("Python100daycode/Day31/flash-card-project-start/data/words_to_learn.csv",index=False)
    df = data.to_dict(orient="records")
    pick_word()

def wrong_button_function():
    window.after_cancel(timer)
    pick_word()


right_button= Button(image=right_button_img,
                    command=right_button_function,
                    highlightthickness=0,
                    relief="groove")

right_button.grid(row=5, column=3,sticky="w")

wrong_button= Button(image=wrong_button_img,
                    command=wrong_button_function,
                    highlightthickness=0,
                    relief="groove")

wrong_button.grid(row=5, column=1,sticky="e")


# title_text = Label(text="Title",font=("Ariel",40,"italic"))
# # title_text.place(x=355,y=150)
# title_text.grid(row=2  ,column=2)

# word_text = Label(text="Word",font=("Ariel",60,"bold"))
# # word_text.place(x=308,y=263)
# # word_text.config(background=None)
# word_text.grid(row=3  ,column=2)

pick_word()

window.mainloop()