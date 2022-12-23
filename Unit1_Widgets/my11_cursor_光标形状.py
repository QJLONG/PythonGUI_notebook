from tkinter import *

win = Tk()
win.title("Cursor")

label = Label(win, text="rasied", relief="raised", bg="lightyellow", padx=5, pady=10, cursor="heart")
label.pack()

win.mainloop()