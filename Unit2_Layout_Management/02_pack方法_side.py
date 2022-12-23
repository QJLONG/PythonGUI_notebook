'''
    pack是最常用的空间配置管理方法，他是用相对位置的概念处理控件的配置
    使用方法如: pack(options, ...)
    options参数可以是: side, fill, padx/pady, ipadx/ipady, anchor
'''

from tkinter import *


win = Tk()
win.title("Pack方法的使用")

# side参数，可以垂直或水平配置控件
lab1 = Label(text="lab1", bg="lightyellow")
lab2 = Label(text="lab2", bg="lightyellow")
lab3 = Label(text="lab3", bg="lightyellow")
# lab1.pack()
# lab2.pack()
# lab3.pack()
'''
    TOP：这是默认值，由上往下排列。
    BOTTOM：由下往上排列。
    LEFT：由左往右排列。
    RIGHT：由右往左排列。
'''
# lab1.pack(side=BOTTOM)
# lab2.pack(side=BOTTOM)
# lab3.pack(side=BOTTOM)

# 还可以混合使用：
# lab1.pack()
# lab2.pack(side=RIGHT)
# lab3.pack(side=LEFT)

# 使用side参数，列出所有relief和bitmap
reliefs = ["flat", "groove", "raised", "ridge", "solid", "sunken"]
for Relief in reliefs:
    Label(win, text=Relief, relief=Relief, fg="blue", font="Times 20 bold").pack(side=LEFT, padx=5)

bitMaps = ["error", "hourglass", "info", "questhead", "question",
           "warning", "gray12", "gray25", "gray50", "gray75"]
for bitMap in bitMaps:
    Label(win, bitmap=bitMap).pack(side=LEFT, padx=5)




win.mainloop()
