import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 # 25
SHORT_BREAK_MIN = 5 # 5
LONG_BREAK_MIN = 20 # 20
reps = 0
timer = None
start_is_clicked = False
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global start_is_clicked
    
    reps = 0
    start_is_clicked = False
    
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="", fg=GREEN)
    check_label.config(text="")
    
   
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():    
    window.attributes('-topmost',1)
    window.bell()
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="RELAX", fg=RED)
        window.attributes('-topmost',0)

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text="BREAK", fg=PINK)
        window.attributes('-topmost',0) 
    else:
        count_down(WORK_MIN * 60)
        label.config(text="WORK", fg=GREEN)
        window.attributes('-topmost',0)

        
def button_clicked():
    global start_is_clicked
    if not start_is_clicked:
        start_is_clicked = True
        start_timer() 
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    canvas.itemconfig(timer_text, text=f"{min:02d}:{sec:02d}")
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        session = math.floor(reps / 2)
        for _ in range(session):
            marks += "✔"
            check_label.config(text=marks)
            
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(f"Pomodoro                        Work {WORK_MIN} min - Break {SHORT_BREAK_MIN} min - Relax {LONG_BREAK_MIN} min")
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(0, 0)
window.iconbitmap("favicon.ico")
# Canvas
canvas =Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image= tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
session_done = canvas.create_text(100, 235, text="Sessions Done", fill=PINK,  font=(FONT_NAME, 15, "bold"), )
canvas.grid(column=1, row=1)


# Window Components

start_button = Button(text="Start", highlightthickness=0, bg=GREEN, width=8, height=4, borderwidth=3, font=(FONT_NAME, 10, "bold"), command=button_clicked)
reset_button = Button(text="Reset", highlightthickness=0, bg=RED, width=8, height=4, borderwidth=3, font=(FONT_NAME, 10, "bold"), command=reset_timer)
label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
label.grid(column=1, row=0)
check_label.grid(column=1, row=2)



window.mainloop()
