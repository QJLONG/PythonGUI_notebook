
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    

    def createWidget(self):
    # 创建主菜单栏
        menubar = Menu(root) 

        # 创建菜单
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)

        # 将菜单加入主菜单栏
        menubar.add_cascade(label="文件(F)", menu=menuFile)
        menubar.add_cascade(label="编辑(E)", menu=menuEdit)
        menubar.add_cascade(label="帮助(H)", menu=menuHelp)
        
        # 添加菜单项
        menuFile.add_command(label="新建", accelerator="ctrl+n")
        menuFile.add_command(label="打开", accelerator="ctrl+o")
        menuFile.add_command(label="保存", accelerator="ctrl+s")
        menuFile.add_separator() # 添加分割线
        menuFile.add_command(label="退出", accelerator="ctrl+q")
        
        # 将主菜单栏添加到根窗口
        self.master["menu"] = menubar

        # 文本编辑区
        self.textpad = Text(root, height=30)
        self.textpad.pack()

        # 创建上下文菜单
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label="背景颜色")

        # 为鼠标右键绑定事件
        # self.master.bind("<Button-3>", self.createContextMenu)
        self.master.bind("<Button-3>", lambda event:self.contextMenu.post(event.x_root, event.y_root))

     
    # def createContextMenu(self, event):
    #     self.contextMenu.post(event.x_root, event.y_root)


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x400")
    app = Application(root)
    root.mainloop()

