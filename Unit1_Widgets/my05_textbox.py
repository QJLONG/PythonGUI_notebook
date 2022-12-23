import tkinter.ttk
from tkinter import *

win = Tk()
win.title('Text Box')


def click_me():
    btn.configure(text="Hello,"+name.get())


def chose_a_number():
    btn2.configure(text="Your number is:" + number.get())


name = StringVar()  # 用具接收文本框中的内容
number = StringVar() # 用于接收combobox中的数字
lab = Label(text="Enter a name:", width=15, justify=LEFT)
lab.grid(column=0, row=0)
btn = Button(text="Clikc Me!", command=click_me)
btn.grid(column=1, row=1)
# 将name绑定在文本框中
name_entered = Entry(win, width=15, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()    # Place cursor into name Entry

lab2 = Label(text="Select a Numbner:")
lab2.grid(row=2, column=0)
# 添加一个组合框（combobox）
btn2 = Button(text="Click Me!", command=chose_a_number)
btn2.grid(row=3, column=1)
number_chosen = tkinter.ttk.Combobox(win, width=12, textvariable=number)
number_chosen.configure(values=(1, 2, 3, 4))
number_chosen.grid(row=3,column=0)
# 为组合框设置一个默认值, 参数为默认值所在元组的index
number_chosen.current(0)

win.mainloop()