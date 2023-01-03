'''
Description: 
Language: UTF-8
Author: hummer
Date: 2023-01-03 23:42:52
'''
from tkinter import *
import webbrowser

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()


    def createWidget(self):
        self.w1 = Text(self, width=40, height=12, bg="gray")
        self.w1.pack()
        # insert方法第一个参数1.0表示在第一行第0列插入字符，注意：行从1开始，但列从0开始
        self.w1.insert(1.0, "0123456789\nnafdera")
        self.w1.insert(2.4, "hummer")

        Button(self, text="插入字符", command=self.insertText).pack(side="left")
        Button(self, text="输出字符", command=self.returnText).pack(side="left")
        Button(self, text="插入图片", command=self.addImage).pack(side="left")
        Button(self, text="添加组件", command=self.addWidget).pack(side="left")
        Button(self, text="tag", command=self.testTag).pack(side="left")


    # 插入字符方法
    def insertText(self):
        # INSERT索引表示在光标处插入
        self.w1.insert(INSERT, "hummer")
        # END索引表示在最后插入
        self.w1.insert(END, "ending...")


    # 返回文本
    def returnText(self):
        # get方法获取文本框中的内容
        print("content: \n", self.w1.get(1.0, END))


    # 添加图片
    def addImage(self):
        self.photo = PhotoImage(file="..\\images\\test.gif")
        self.w1.image_create(END, image=self.photo)


    # 添加组件
    def addWidget(self):
        b1 = Button(self.w1, text="hummer_test")
        self.w1.window_create(INSERT, window=b1)


    # 通过tag精确控制文本
    def testTag(self):
        self.w1.delete(1.0, END)
        self.w1.insert(INSERT, "good good study, day day up!\nhummer\nGoogle")
        self.w1.tag_add("name1", 1.0, 1.9)
        self.w1.tag_config("name1", background="blue", foreground="red")
        self.w1.tag_add("name2", 2.0, 2.5)
        self.w1.tag_config("name2", underline=True)
        self.w1.tag_add("google", 3.0, 3.5)
        self.w1.tag_config("google", underline=True)
        self.w1.tag_bind("google", "<Button-1>", self.webshow)

    def webshow(self, event):
        webbrowser.open("http://www.google.com")


if __name__ == '__main__':
    win = Tk()
    win.geometry("400x200+400+200")
    app = Application(win)
    win.mainloop()