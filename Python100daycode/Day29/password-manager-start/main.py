import os
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT_NAME = "Courier"

BLUE = "#22092C"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project from day 5
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    # print(f"Your password is: {password}")
    pass_entry.delete('0','end')
    pass_entry.insert(END, string=f"{password}")
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    
    website = website_entry.get()
    user = user_entry.get()
    pass_code = pass_entry.get()
    if len(website)<1 or len(user)<1 or len(pass_code)<0:
        messagebox.showinfo(title="Empty fields",message="Please don't leave any fields empty!")
        is_ok=False
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail: {user}" 
                            f"\nPassword: {pass_code} \n\nIs this ok to save?")
    
    if is_ok:
        with open("Python100daycode/Day29/password-manager-start/data.csv",mode="a") as file:            
            file.write(f"\n{website}, {user}, {pass_code}")
            website_entry.delete('0','end')
            pass_entry.delete('0','end')
    
    

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
                    command=generate_password,
                    fg=BLUE,font=(FONT_NAME,9,"bold"),bg="#FFFFDD", highlightthickness=0, relief="groove")
pass_button.grid(row=4, column=3, sticky="e")

add_button = Button(text="Add", width=47,
                    command=save_password,
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