#!/usr/bin/python3

# tkinter 图形界面测试

import random
from tkinter import *

win = Tk()

win.title('tkinter的初使用——对齐可伸缩渐变色乘法口诀表')

for i in range(1, 10):
    win.rowconfigure(i-1, weight=1)
    win.columnconfigure(i-1,weight=1)
    for j in range(i, 10):
        a = Label(win,
                  text=str(i) + '×' + str(j) + '=' + str(i*j),
                  #   bg='#'+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                  #   bg='#' + str(i) + str(j) + 'F'
                  bg='#' + str(j) + str(i) + 'F'
                  )
        a.grid(row=j-1,
               column=i-1,
            #    padx=10,
            #    pady=10,
               sticky=W+E+N+S
               )

win.mainloop()
