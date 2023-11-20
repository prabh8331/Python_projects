import os
from tkinter import *
FONT_NAME = "Courier"

BLUE = "#22092C"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Personal Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200 , height= 200 )

# logo_img = PhotoImage(file="Python100daycode/Day29/password-manager-start/logo.png")

logo_img = PhotoImage(file="C:/Users/prabh/OneDrive/Desktop/Python_projects/Python100daycode/Day29/password-manager-start/logo.png")

canvas.create_image(135,100, image=logo_img)

canvas.grid(row=1,column=2,sticky="e")


website_text = Label(text="Website:",fg=BLUE,font=(FONT_NAME,9,"bold"))
website_text.grid(row=2,column=1)

user_text = Label(text="Email/Username:",fg=BLUE,font=(FONT_NAME,9,"bold"))
user_text.grid(row=3,column=1)

pass_text = Label(text="Password:",fg=BLUE,font=(FONT_NAME,9,"bold"))
pass_text.grid(row=4,column=1)


pass_button= Button(text="Generate Password",
                    #  command=reset_timer,
                    fg=BLUE,font=(FONT_NAME,9,"bold"),bg="#FFFFDD", highlightthickness=0, relief="groove")
pass_button.grid(row=4, column=3, sticky="e")

add_button = Button(text="Add", width=47,
                    #  command=reset_timer,
                    fg=BLUE,font=(FONT_NAME,9,"bold"),bg="#FFFFDD", highlightthickness=0, relief="groove")
add_button.grid(row=5, column=2,columnspan=2,sticky="w")


#Website Entries
website_entry = Entry(width=47,fg=BLUE,font=(FONT_NAME,9,"bold"),bg="#FFFFDD")
#beginning text
website_entry.insert(END, string="www.example.com")
#Gets text in entry
# print(entry.get())
website_entry.grid(row=2,column=2 , columnspan= 2, sticky="w")
website_entry.focus()


#Email/Username Entries
user_entry = Entry(width=47,fg=BLUE,font=(FONT_NAME,9,"bold"),bg="#FFFFDD")
#beginning text
user_entry.insert(END, string="prabh8331@gmail.com")
#Gets text in entry
# print(entry.get())
user_entry.grid(row=3,column=2, columnspan=2, sticky="w")


#Password Entries
pass_entry = Entry(width=28,fg=BLUE,font=(FONT_NAME,9,"bold"),bg="#FFFFDD")
#beginning text
pass_entry.insert(END, string="Enter you Password")
#Gets text in entry
# print(entry.get())
pass_entry.grid(row=4,column=2, sticky="w")


window.mainloop()