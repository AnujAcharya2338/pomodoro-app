from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timeer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timeer)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN *60
    short_sec = SHORT_BREAK_MIN *60
    long_sec = LONG_BREAK_MIN *60
    
    
    if reps % 8 == 0:
        timer.config(text="Long Break mode", fg=PINK)
        
        count_down(long_sec)
    elif reps %2 ==0:
        timer.config(text="Short Break mode", fg=GREEN)
        count_down(short_sec)
    else:
        timer.config(text="Work mode" , fg=RED)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec= count % 60
   
    if count_sec < 10:
        count_sec =(f"0{count_sec}")
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timeer
        timeer=window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        checkmark.config(text=mark)     
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100, bg=YELLOW)

timer=Label(text="Timer",font=(FONT_NAME,35,"bold"), fg=GREEN , bg=YELLOW)
timer.grid(row=0, column=1)


canvas=Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(150,150, image=photo)
timer_text= canvas.create_text(150,170, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

start=Button(text="start", bg=YELLOW , command=start_timer) 
start.grid(row=3,column=0)


reset=Button(text="reset", bg=YELLOW, command=reset_timer)
reset.grid(row=3,column=3)

checkmark=Label(font=(FONT_NAME,40 ,"bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1,row=3)
window.mainloop()