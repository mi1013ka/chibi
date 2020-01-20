#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import Tkinter


root = Tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

#ボタン
Button = Tkinter.Button(text=u'ボタンです', width=50)
Button.pack()

root.mainloop()