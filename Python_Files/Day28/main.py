import pandas
from tkinter import *

window = Tk()
window.title("AKX WINDOW")
window.config(padx=30, pady=30)
window.minsize(width=400, height=400)
my_label = Label(text="this is label", font=("Roman", 12, "bold"))
my_label.grid(row=0, column=0)
new_label = Label(text="New label", font=("arial", 13, "underline"))
new_label.grid(row=5, column=5)


def button_click():
    my_label["text"] = input.get()
    

input = Entry(width=10)
input.grid(row=2, column=2)
button = Button(text="Click Me", command=button_click)
button.grid(row=1, column=3)


def hit_me():
    new_label["text"] =value.get()


value = Entry(width=25)
value.grid(column=5, row=7)
new_button = Button(text="New_click", command=hit_me)
new_button.grid(row=4, column=4)




window.mainloop()