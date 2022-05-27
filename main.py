from tkinter import *

timer = None

def countdown(count):
    global timer
    if count > 3 :
        timer = window.after(1000, countdown, count - 1)
    elif count > 2 :
        text.config(fg="#FCD2D1")
        timer = window.after(1000, countdown, count - 1)
    elif count > 1 :
        text.config(fg="#FE8F8F")
        timer = window.after(1000, countdown, count - 1)
    elif count > 0 :
        text.config(fg="#FF5C58")
        timer = window.after(1000, countdown, count - 1)
    else:
        text.delete("1.0","end")
        
def detectkey(e):
    window.after_cancel(timer)
    text.config(fg="#F7ECDE")
    countdown(5)

window = Tk()
window.title("Dissapearing Text")
window.minsize(700,500)
window.config(padx=100, bg="gray")

title_lbl = Label(text="Keep Typing!",bg="gray", fg="#F7ECDE",font=("Supermercado Regular", 30))
title_lbl.grid(column=0,row=0, pady=50)

text = Text(borderwidth=0, width=50, height=20, bg="gray",
            fg="#F7ECDE", font=("Supermercado Regular", 18))
text.focus()
text.grid(column=0, row=1)

countdown(5)
window.bind("<Key>", detectkey)

window.mainloop()