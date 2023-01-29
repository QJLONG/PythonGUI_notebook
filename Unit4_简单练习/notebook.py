'''
Description: 
Language: UTF-8
Author: hummer
Date: 2023-01-29 16:48:36
'''

from tkinter.filedialog import *
from tkinter import *
from tkinter.colorchooser import *

 
class Application(Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createMenuBar()
        self.createTextPad()
        self.createContextMenu()

    
    # 创建菜单栏
    def createMenuBar(self):
        menubar = Menu(self.master)
        
        # 创建菜单
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)

        # 将菜单添加到菜单栏中
        menubar.add_cascade(label="文件(F)", menu=menuFile)
        menubar.add_cascade(label="编辑(E)", menu=menuEdit)
        menubar.add_cascade(label="帮助(H)", menu=menuHelp)

        # 创建菜单项
        menuFile.add_command(label="新建", accelerator="ctrl+n", command=self.newFile)
        menuFile.add_command(label="打开", accelerator="ctrl+o", command=self.openFile)
        menuFile.add_command(label="保存", accelerator="ctrl+s", command=self.saveFile) 
        menuFile.add_separator()
        menuFile.add_command(label="退出", accelerator="ctrl+q", command=self.exitFile)


        # 将菜单栏添加到root中
        self.master.configure(menu=menubar)
    
    
    # 创建上下文菜单
    def createContextMenu(self):
        self.contextMenu = Menu(self.master)
        self.contextMenu.add_command(label="背景颜色", command=self.changeBackGround)
        self.master.bind("<Button-3>", lambda event: self.contextMenu.post(event.x_root, event.y_root))


    # 创建文本编辑区
    def createTextPad(self):
        self.textpad = Text(self.master, width=90, height=300)
        self.textpad.pack()


    def changeBackGround(self):
        color = askcolor(title="背景颜色")
        self.textpad.configure(bg=color[1])


    def newFile(self):
        self.textpad.delete(1.0, END)
        self.filename = asksaveasfilename(title="另存为", initialfile="新建文件.txt", 
                            filetypes=[("文本文档", "*.txt")], 
                            defaultextension=".txt")
        self.saveFile()


    def openFile(self):
        self.textpad.delete(1.0, END)
        with askopenfile(title="打开文件") as f:
            self.filename = f.name
            self.textpad.insert(1.0, f.read())

    
    def saveFile(self):
        with open(self.filename, "w") as f:
            f.write(self.textpad.get(1.0, END))
    

    def exitFile(self):
        self.master.quit()



if __name__ == "__main__":
    root = Tk()
    root.title("记事本测试项目")
    root.geometry("600x400")
    app = Application(root)
    root.mainloop()

