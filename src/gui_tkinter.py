# -*- coding:utf-8 -*-
import sys
import tkinter

root = tkinter.Tk()
root.title('さかなび - 知らない魚を写真に撮ったら教えてくれるアプリ')
root.geometry('375x480')

# txt01
txt01 = tkinter.Label(text = '１）魚の写真を撮る')
txt01.place(x = 100, y = 100)
txt01.pack()

# button01
btn01 = tkinter.Button(text = '写真を撮る', width = 30)
btn01.place(x = 100, y = 150)
btn01.pack()

# txt02
txt02 = tkinter.Label(text = '２）調べる')
txt02.place(x = 100, y = 100)
txt02.pack()

# button02
btn02 = tkinter.Button(text = '調べる', width = 30)
btn02.place(x = 100, y = 150)
btn02.pack()

root.mainloop()

