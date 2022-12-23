# 练习Label组件的使用
"""
Label(parent, options)
options:
1.anchor: 如果空间大于所需，控制标签的位置，默认是CENTER（居中）
2.bg/background: 背景颜色
3.fg/foreground: 前景色
4.relief：标签的边框类型，默认是FLAT
5.bd/borderwidth: 标签边界宽度，默认是1
6.cursor：光标在标签上方时的外形
7.underline：可以设置第几个字符有下划线，从0开始，默认是-1，表示无下划线
8.font: 字形，字形样式或大小
9.height: 标签高度，单位是字符
10.width:标签宽度，单位是字符
11.warplength：本文到多少宽度后换行，单位是px
12.image：标签以图像的方式呈现
13.justify：多行文本的最后一行的对齐方式，（LEFT/CENTER/RIGHT）默认是CENTER
14.padx/pady: 标签文字与标签区间的间距，单位是px
15.text:标签内容
16.textvariable：设置标签以变量的方式显示
17.btmap：使用默认图标当做标签内容
18.compound：可以设置标签内含图像文字时，彼此的位置关系
"""
from tkinter import *


class Application(Frame):
    # 创建初始化方法
    def __init__(self, master=None):
        super().__init__(master=master)
        # 将Application对象pack处理
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text="Hummer的GUI", width=15, height=2, font=("黑体", 20),
                             bg="green", fg="white")
        self.label01.pack()

        # 添加图片标签
        self.photo = PhotoImage(file="../images/test.gif")
        self.label02 = Label(self, image=self.photo, borderwidth=5, relief="solid")
        self.label02.pack()

        # 添加右对齐的文本框
        self.label03 = Label(self, text="我是一个粉刷匠\n粉刷本领强", width=15, font=("黑体", 20), justify=CENTER)
        self.label03.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x600+400+200")
    app = Application(root)

    root.mainloop()