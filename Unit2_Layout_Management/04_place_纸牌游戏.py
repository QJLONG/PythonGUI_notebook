'''
Description: 
Language: UTF-8
Author: hummer
Date: 2023-01-27 13:57:48
'''
"""
Description:    用Place布局管理器实现纸牌点击的上下移动效果
Auther: hummer
CreateDate: 2023-01-27
"""

from tkinter import *
from PIL import Image, ImageTk

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.images_switch = [Image.open("/home/hummer/Documents/pycode/pythonGUI/images/pukes/2"+str(i)+".JPG").\
                resize((200,300), Image.ANTIALIAS) for i in range(10)]
        self.images = [ImageTk.PhotoImage(self.images_switch[i]) for i in range(10)]
        self.pukes = [Label(self.master, image=self.images[i]) for i in range(10)]
        for i in range(10):
            self.pukes[i].place(x=10+i*65, y=50)
            self.pukes[i].bind_class("Label", "<Button-1>", self.chupai)             
    
    def chupai(self, event):
        if event.widget.winfo_y() == 50:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)
        



if __name__ == '__main__':
    root = Tk()
    root.geometry("1000x400")
    app = Application(root)
    root.mainloop()

