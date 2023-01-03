"""
设置控件填满所分配容器区间的方式,如果是fill=X表示控件可以填满所分配空间的X轴不留白,
如果是fill=Y表示控件可以填满所分配空间的Y轴不留白,
如果是fill=BOTH表示控件可以填满所分配空间的X轴和Y轴。
fill默认值是NONE,表示保持原大小。
"""
from tkinter import *


win = Tk()
win.title("Pack方法的使用")

# side参数，可以垂直或水平配置控件
lab1 = Label(text="lab1", bg="blue")
lab2 = Label(text="lab2", bg="blue")
lab3 = Label(text="lab3", bg="blue")
lab1.pack(side=LEFT, fill=Y)
lab2.pack(side=TOP, fill=BOTH, expand=True)
lab3.pack(side=TOP, fill=BOTH)

win.mainloop()
