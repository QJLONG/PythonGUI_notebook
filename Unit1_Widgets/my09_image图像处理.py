from tkinter import *
from PIL import Image, ImageTk
# 注意：image属性和bitmap属性不能共存，设置了image参数，则bitmap参数自动失效

root = Tk()
root.title("Image Test")

# # 先生成一个PhotoImage对象
# image_gif = PhotoImage(file="..\\images\\test.gif")
# label = Label(root, image=image_gif)
# label.pack()

# # 如果想在标签内显示jpg文件，需要借助PIL模块的Image和ImageTk模块
# # .\python.exe -m pip install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
# image = Image.open("..\\images\\test.jpg")
# test_image = ImageTk.PhotoImage(image)
# label = Label(root, image=test_image)
# label.pack()

# 如果想让图片与文字共存，需要使用compound参数设置图像的位置, justify参数可以设置文字的对其方式
test_gif = PhotoImage(file="..\\images\\test.gif")
test_text = "如果想让图片与文字共存，\n需要使用compound参数设置图像的位置"
label = Label(text=test_text, image=test_gif, compound="left", justify=LEFT)
label.pack()


root.mainloop()