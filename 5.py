# 不可思议的样本
from tkinter import *

win = Tk()


def show():
    str = entry().get()
    print(str)


entry = Entry(win)
entry.grid(row=0)
Button(win, text='显示', command=show).grid(row=0, column=1)


win.mainloop()
