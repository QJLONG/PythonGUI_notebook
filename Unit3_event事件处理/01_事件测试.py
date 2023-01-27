from tkinter import *

root = Tk()
root.geometry("500x300")

c1 = Canvas(root, width=200, height=200, bg="green")
c1.pack()

def mouseClick(event):
    print("相对于父容器x=%d" % event.x)
    print("相对于父容器y=%d" % event.y)

def mouseDrag(event):
    c1.create_oval(event.x, event.y, event.x+1, event.y+1)

def pressA(event):
    print("You have pressed " + event.keysym)


c1.bind("<ButtonPress-1>", mouseClick)
c1.bind("<B1-Motion>", mouseDrag)

root.bind("<KeyPress-a>", pressA)


root.mainloop()
