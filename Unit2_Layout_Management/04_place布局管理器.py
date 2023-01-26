"""
选项：
x,y         组件左上角的坐标(相对于窗口)
relx,rely   组件左上角的坐标(相对于父容器)
width,height        单位是像素
relwidth,relheight  0~1之间的数
"""

from tkinter import *
from threading import Thread

class Application(Thread):
    def __init__(self, master=None):
        Thread.__init__(self)
        self.master = master
        self.createWidget()
        
    def createWidget(self):
        f1 = Frame(master=self.master, bg="green")
        f1.place(relx=0.2, y=50, relwidth=0.5, relheight=0.5)


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x400")
    app = Application(root)
    root.mainloop()
