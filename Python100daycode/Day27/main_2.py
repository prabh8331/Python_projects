from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) #this will add padding into edge of the entire window

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()   #always start from top and keeps adding new items below, but we can specify the top, left, right or bottom
my_label.grid(column=1, row=1)

# my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)  # this will add padding to just this widget



#Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
# button.place(x=100,y=200)  #give the precise location, but because it is too specific that we have to work on the coordinate
button.grid(column=2, row=2)




# new button
new_button = Button(text="New Button")
new_button.grid(column=4, row=3)




#Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=1)  #it imagine the window as grid and then place as per that, we can not use pack and grid in one program




window.mainloop()