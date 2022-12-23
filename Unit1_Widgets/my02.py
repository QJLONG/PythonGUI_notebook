"""测试一个经典的GUI程序的写法，使用面向对象的方式"""
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """一个经典的GUI程序的写法"""
    def __init__(self, master=None):
        super().__init__(master)
        self.btn01 = None
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.btn01 = Button(self)
        self.btn01['text'] = "点我就送花"
        self.btn01['command'] = self.songhua
        self.btn01.pack()

        # 创建一个退出按钮
        self.btnQuit = Button(master=self, text="Quit", command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("message", "送你一朵小红花")


root = Tk()
root.title("My first GUI")
root.geometry("400x200+400+200")

app = Application(root)

root.mainloop()


