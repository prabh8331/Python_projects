from tkinter import *

window = Tk()

#Window setup 
window.title("Mile to Km Converter")
# window.minsize(width=350, height=150)
window.config(padx=38,pady=25)

# All text setup
text_eq = Label(text="is equal to", font=("Arial", 15))
text_eq.grid(column=1,row=2)

text_mile = Label(text="Miles", font=("Arial", 15))
text_mile.grid(column=3,row=1)

text_km = Label(text="Km", font=("Arial", 15))
text_km.grid(column=3,row=2)

result = 0
text_result = Label(text=f"{result}", font=("Arial", 15))
text_result.grid(column=2,row=2)

def calculate():
    result = round(float(user_input.get())*1.609344,2)
    text_result.config(text=f"{result}")


# Button setup
button = Button(text="Calculate",font=("Arial",15),command=calculate)
button.grid(row=3,column=2)

# Entry
user_input = Entry(width=6,font=("Arial",15))
user_input.grid(row=1,column=2)


window.mainloop()