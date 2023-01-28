"""
格式：lambda 输入：输出
例如：lambda x,y: x+y
      lambda *args: sum(args)
      lambda **kwargs: 1
"""

# 在GUI编程中通常于command属性配合使用
# command绑定事件不涉及到event对象的使用，适用于简单的事件绑定

"""
对一类组件进行事件绑定：widget.bind_class
"""

from tkinter import * 

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.pack()
        self.createWidgets()

    def mouseTest(self, a, b):
        print("moustTest" + str(a) + str(b))

    def createWidgets(self):
        b1 = Button(self.master, text="Mouse测试1")
        b1.pack()
        b2 = Button(self.master, text="Mouse测试2")
        b2.pack()
        b1.bind_class("Button", "<ButtonPress-1>", lambda event: self.mouseTest(1,2))


if __name__ == '__main__' :
    root = Tk()
    root.geometry("200x200")
    app = Application(root)
    root.mainloop()
