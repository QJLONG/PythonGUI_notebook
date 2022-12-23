from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("我的第一个GUI程序")
root.geometry("500x300+400+200")

btn = Button(root)
btn['text'] = "点我就送花"
btn.pack()


def songhua(e):
    messagebox.showinfo("message", "送你一朵玫瑰花")


btn.bind("<Button-1>", songhua)

root.mainloop()
