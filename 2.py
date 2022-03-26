#!/usr/bin/python3

# wxPython 图形界面测试

import wx

def load(event):
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    file = open(filename.GetValue(), 'w')
    file.write(contents.GetValue())
    file.close()

app = wx.App()

# 窗口设定
win = wx.Frame(None, title = 'Simple Editor', size = (410, 335))
bkg = wx.Panel(win)

# 按钮
# btn = wx.Button(win)
# load_button = wx.Button(win, label = 'Open', pos = (225, 5), size = (80, 25))
load_button = wx.Button(bkg, label = 'open')
load_button.Bind(wx.EVT_BUTTON, load)
# save_button = wx.Button(win, label = 'Save', pos = (315, 5), size = (80, 25))
save_button = wx.Button(bkg, label = 'save')
save_button.Bind(wx.EVT_BUTTON, save)

# 文本框
# filename = wx.TextCtrl(win, pos = (5, 5), size = (210, 25))
filename = wx.TextCtrl(bkg)
# contents = wx.TextCtrl(win, pos = (5, 35), size = (390, 260), style = wx.TE_MULTILINE | wx.HSCROLL)
contents = wx.TextCtrl(bkg, style = wx.TE_MULTILINE | wx.HSCROLL)

# 使用尺寸器
hbox = wx.BoxSizer()
hbox.Add(filename, proportion = 1, flag = wx.EXPAND)
hbox.Add(load_button, proportion = 0, flag = wx.LEFT, border = 5)
hbox.Add(save_button, proportion = 0, flag = wx.LEFT | wx.RIGHT, border = 5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
vbox.Add(contents, proportion = 1, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border = 5)

bkg.SetSizer(vbox)

win.Show()
app.MainLoop()