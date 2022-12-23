import tkinter
from tkinter import *
from tkinter import ttk


def click_me():
    btn.configure(text="Your number is: " + number.get())


win = Tk()
win.title("Check Button Test")
lab1 = Label(win, text="Enter a name:")
lab1.grid(row=0, column=0)
lab2 = Label(win, text="Choose a number:")
lab2.grid(row=0, column=1)

# Adding a Button
btn = Button(text="Click Me!", command=click_me)
btn.grid(row=1, column=2)

# Adding two comboboxs
name = StringVar()
number = StringVar()
name_entred = Entry(win, width=12, textvariable=name)
name_entred.grid(row=1, column=0)
number_chosen = ttk.Combobox(win, width=12, textvariable=number, values=(12, 20, 40, 42), state="readonly") # readonly可以设置不可以自定义选项
number_chosen.grid(row=1, column=1)
number_chosen.current(0)

# Adding three chack buttons
chVarDis = IntVar()
check1 = Checkbutton(win, text='Disabled', variable=chVarDis, state="disabled")
# select the button mark
check1.select()
check1.grid(row=3, column=0, sticky=W)
'''
    sticky:默认的控件在窗口中的对齐方式是居中。
    可以使用sticky选项去指定对齐方式，可以选择的值有：N/S/E/W，分别代表上对齐/下对齐/左对齐/右对齐，
    可以单独使用N/S/E/W，也可以上下和左右组合使用，达到不同的对齐效果，
'''

chVarUn = IntVar()
check2 = Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(row=3, column=1, sticky=W)
chvarEn = IntVar()
check3 = Checkbutton(win, text="Enabled", variable=chvarEn)
check3.select()
check3.grid(row=3, column=2, sticky=W)




win.mainloop()