# GUI_create_button_change_property.py
from tkinter import *

win = Tk()
win.title("Python GUI")

a_label = Label(win, text="A Label")
a_label.grid(column=0, row=0)


def click_me():
    btn.configure(text="** I have been Clicked! **")
    a_label.configure(fg="red")
    a_label.configure(text="** I have been red! **")


btn = Button(text="Clink Me!", command=click_me)
btn.grid(column=1, row=0)

win.mainloop()