import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label

my_lable = tkinter.Label(text = "I Am a Label", font=("Arial", 24, "bold"))  # create a component 
my_lable.pack(side="left")   #how that component is going to laid out on windows, packer is geometry-management mechanism 
## in pack we see kw** and no other paratemter we can set 
## it is because tkinter is imported from antoher language and they used **kwargs, because it was most efficient way to do so





window.mainloop()
# inside this mainloop similar to following is happening 
# while True:
#     listening

