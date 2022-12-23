from tkinter import *


counter = 0


def run_counter(dight):
    def counting():
        global counter
        counter += 1
        dight.config(text=str(counter))     # 更新组件中的文本信息
        dight.after(1000, counting)     # 每隔一秒运行一次函数
    counting()


root = Tk()
root.title("Counter")

counter_label = Label(root, bg="yellow", fg="blue", height=3, width=10, font="Helvetic 20 bold")
counter_label.pack()
run_counter(counter_label)

root.mainloop()
