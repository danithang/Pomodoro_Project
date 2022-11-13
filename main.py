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
REPS = 0
# having the Timer variable do nothing to start off
TIMER = NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # stopping the timer when hit the button reset
    window.after_cancel(TIMER)
    # resetting the canvas timer_text to 0 when the reset button is pressed
    canvas.itemconfig(timer_text, text="00:00")
    # resetting the tomato_label to words Timer when the reset button is pressed
    tomato_label.config(text="Timer")
    # resetting the label_check to an empty string so nothing will show up when reset
    label_check.config(text="")
    # calling global Reps to reset it to 0
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    # establishing global reps from above to pass in +=1
    global REPS
    REPS += 1

    # giving the global variables a variable to multiply each by 60
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if reps have no remainder then change the timer...8 is the last rep which is the long break
    if REPS % 8 == 0:
        # change label text and color when certain reps happen
        tomato_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # any reps with 2 with no remainder will get the short break
    elif REPS % 2 == 0:
        tomato_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    # anything else will have work_sec
    else:
        tomato_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # math.floor returns the largest whole number that is less than or equal to that certain number
    count_min = math.floor(count / 60)
    # getting the number of seconds that remains
    count_sec = count % 60
    # getting the sec to have 00 and 09 and below when counting down instead of 1 digit...uses dynamic type basically
    # changing int into str
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # taking the count and configuring variable timer_text(canvas.create_text) and saying if count is greater than 0
    # then use window.after to wait a certain time then call a function you tell it to call
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        # first arg is to wait 1 sec(1000ms), then pass in function, then pass in positional argument which in this
        # case is the count - 1 which means countdown by 1
        # placing it in a global variable Timer to stop the count in reset function
        TIMER = window.after(1000, count_down, count - 1)
    # calling start timer function so it can be in loop
    else:
        start_timer()
        marks = ""
        # looping through reps/2 and using math.floor to get the nearest whole number
        for _ in range(math.floor(REPS / 2)):
            # giving mark variable a checkmark for everytime user finishes a work rep
            marks += "✔"
            label_check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# getting Tk() class from tkinter and adding title and size
window = Tk()
window.title("Pomodoro Project")
# fixes the padding, so it can be more in middle of screen and giving a background color
window.config(padx=100, pady=100, bg=YELLOW)

# transferring the tomato picture as background of program...canvas width and height is the same as the tomato pic
# giving background color of canvas to match window color and taking highlight around the canvas off
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# retrieving the file and placing it on the background
tomato_img = PhotoImage(file="tomato.png")
# placing image on background and making width and height half of the original canvas to get pic to fit...adjust the
# measurements to not cut off tomato image
canvas.create_image(100, 112, image=tomato_img)
# creating text within the tomato photo
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# determining how canvas will go on screen
canvas.grid(column=1, row=1)

# creating a label/title for the program
tomato_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
tomato_label.grid(column=1, row=0)

# creating buttons for start and restart
# calling the function start timer for the button
button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

# calling the function reset timer for the button
button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)

label_check = Label(fg=GREEN, bg=YELLOW)
label_check.grid(column=1, row=3)

window.mainloop()
