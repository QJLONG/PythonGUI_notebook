from tkinter import *


def click_confirm():
    selection = []
    for i in checkBox.keys():
        if checkBox[i].get() == True:
            selection.append(myDict[i])
    print("Your selection is: ", " ".join(selection))


win = Tk()
win.title("Check Button Test")
win.geometry("400x200+600+300")
# 创建一个提示标签
lab = Label(text="请选择你喜欢的运动！")
lab.grid(row=0, column=0)
# 创建复选框
myDict = {0: "Basketball", 1: "Baseball", 2: "badminton", 3: "Ping Pang", 4: "Volleyball"}
checkBox = {}
for i in range(len(myDict)):
    checkBox[i] = BooleanVar()
    check_btn = Checkbutton(text=myDict[i], variable=checkBox[i])
    check_btn.grid(row=i+1, column=0, sticky=W)
# 添加一个确认按钮，点击输出选择的值
btn_confirm = Button(text="确认", command=click_confirm)
btn_confirm.grid(row=len(myDict) + 1, column=0, sticky=W)
win.mainloop()