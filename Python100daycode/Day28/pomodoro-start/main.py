from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9ADE7B"
GREEN_tick = "#508D69"
YELLOW = "#EEF296"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
tick = ""
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global rep
    window.after_cancel(timer)
    rep=0
    canvas.itemconfig(timer_text, text="00:00")
    lable_text.config(text="Timer",fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global rep
    WORK_sec = WORK_MIN*60
    SHORT_BREAK_sec = SHORT_BREAK_MIN*60
    LONG_BREAK_sec = LONG_BREAK_MIN*60
    
    rep += 1
    print(rep)

    if rep%8 == 0:
        count_down(LONG_BREAK_sec)
        lable_text.config(text="Break",fg=RED)
    elif rep%2 == 0:
        count_down(SHORT_BREAK_sec)
        lable_text.config(text="Break",fg=PINK)
    else:
        count_down(WORK_sec)
        lable_text.config(text="Work",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# the time module and time.sleep will not work because we are working in graphical user interface not in command line program
# command line program will only do something when we instruct it
# but in graphical user interface it keep refreshing itself to keep listening for events for every fraction of second
# this GUI type of GUI program is called EVENT DRIVEN and it is driven through our mainloop()


# tkinert has window.after (after) funtion for timing mechanism, it execute a command after a time delay


def count_down(count):
    global tick
    count_min = count//60
    count_sec = count%60
    if count_sec <=9:
        count_sec = "0"+str(count_sec)  # here we are dynamically changing the datatype of the variable count_sec from int to string this is called "Dynamic Typing"
    if count_min <=9:
        count_min = "0"+str(count_min)

    # but python is also strongly typed in the sense if a function is expected to have a integer then only it will take integer not string, and python holds on to the datatype if not explicit converted

    #Python is strongly, dynamically typed.
    #   Strong typing means that the type of a value doesn't change in unexpected ways. A string containing only digits doesn't magically become a number, as may happen in Perl. Every change of type requires an explicit conversion.
    #    Dynamic typing means that runtime objects (values) have a type, as opposed to static typing where variables have a type.

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  
    print(count)
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)  ## we can give *args which mean we can give multiple numbers of positional arguments
    else:
        if rep%2 != 0:
            tick += "✔" 
            tick_text.config(text=tick)
        start_timer()





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="Python100daycode/Day28/pomodoro-start/tomato.png")

canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100,130, text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

canvas.grid(row=2,column=2)



# Timer Label
lable_text = Label(text="Timer", font=(FONT_NAME, 30,"bold"),bg=YELLOW,fg=GREEN)
lable_text.grid(row=1,column=2)

# fg means foreground and bg means background

# start Button setup
start_button= Button(text="Start",
                     command=start_timer,
                     fg=GREEN_tick,font=(FONT_NAME,9,"bold"),bg="#FFFFDD", highlightthickness=0, relief="groove")
start_button.grid(row=3, column=1)

# Reset Button setup
reset_button= Button(text="Reset",
                     command=reset_timer,
                     fg=GREEN_tick,font=(FONT_NAME,9,"bold"),bg="#FFFFDD", highlightthickness=0, relief="groove")
reset_button.grid(row=3, column=3)

# tick label
tick_text = Label(#text="✔",
                  bg=YELLOW,fg=GREEN_tick)
tick_text.grid(row=3, column=2)



window.mainloop()