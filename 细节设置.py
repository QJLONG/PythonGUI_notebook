'''
Font 构造器具有以下选项：

family - 字体系列，如 Arial，Courier。
size - 字体大小（以 points 为单位）
weight - 粗细，normal 或 bold
slant - 字体倾斜：roman 或 italic
underline - 字体的下划线，False 或 True
overstrike - 字体删除线，False 或 True
'''

import tkinter.font as tkFont

fontExample = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
fontExample.configure(weight='normal')


'''
设置文本对齐
'''

self.lab.pack(side=TOP, anchor=W)