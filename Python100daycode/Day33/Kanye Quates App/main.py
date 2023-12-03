from tkinter import *
import requests

def get_quote():
    #Write your code here.
    response = requests.get(url="https://api.kanye.rest/")
    # print(response)
    response.status_code
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text,text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="Python100daycode/Day33/Kanye Quates App/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Python100daycode/Day33/Kanye Quates App/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()