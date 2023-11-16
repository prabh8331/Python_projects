import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label

my_lable = tkinter.Label(text = "I Am a Label", font=("Arial", 24, "bold"))  # create a component 
my_lable.pack(side="left")   #how that component is going to laid out on windows, packer is geometry-management mechanism 
## in pack we see kw** and no other paratemter we can set 
## it is because tkinter is imported from antoher language and they used **kwargs, because it was most efficient way to do so



#either we mention the properties in tkinter in above style in time of initialization or 
## by taping into the parameter :
my_lable["text"] = "New Text"
my_lable.config(font=("Arial",30))


# def button_clicked():
#     print("I got clicked")
#     my_lable.config(text="I got clicked")
#     my_lable.pack(side="top")

# button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()



def button_clicked():
    text=input.get()
    print(text)
    my_lable.config(text=f"{text}")
    my_lable.pack(side="top")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


#Entry

input = tkinter.Entry(width=10)
input.pack()


window.mainloop()
# inside this mainloop similar to following is happening 
# while True:
#     listening

