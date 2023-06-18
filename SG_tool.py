# import 하기
from tkinter import *
import os
import time

# GUI 초기화 및 세팅
tk = Tk()
tk.title("SG_tool(v.1)")
tk.geometry("640x150")
tk.resizable(False, False)

# 버튼 클릭했을때, 함수
def btncmd():
    pat1 = txt.get("1.0", END)
    path_ = pat1.strip("\n")
    print(path_)
    if os.path.isdir(path_):
        os.rmdir(path_)
    else:
        os.remove(path_)

def btncmd1():
    pat1 = txt.get("1.0", END)
    path_ = pat1.strip("\n")
    os.mkdir(path_)

def btncmd2():
    pat1 = txt.get("1.0", END)
    path_ = pat1.strip("\n")
    if os.path.isfile(path_):
        f = open(path_, 'w')
    else:
        f = open(path_, 'a')

def btncmd3():
    pat1 = txt.get("1.0", END)
    path_ = pat1.strip("\n")
    f = open(path_, 'r')
    label1.config(text="info:{}".format(f))
    f.close()

# 텍스트 초기화 및 생성
txt = Text(tk, width=90, height=3)
txt.pack()

# 버튼 초기화 및 생성
btn1 = Button(tk, text="remove", width=12, command=btncmd)
btn1.place(x=150, y=44)

btn2 = Button(tk, text="mkdir", width=12, command=btncmd1)
btn2.place(x=245, y=44)

btn3 = Button(tk, text="mkfile", width=12, command=btncmd2)
btn3.place(x=340, y=44)

btn4 = Button(tk, text="info", width=12, command=btncmd3)
btn4.place(x=435, y=44)

label1 = Label(tk, text="info:")
label1.place(x=150, y=75)

# 라벨들 초기화 및 생성
label1e = Label(tk, text="(info can only read files, no medicine.)")
label1e.place(x=250, y=90)

label2 = Label(tk, text="😀dev:Sgoodgen", width=30)
label2.place(x=230, y=120)

# 종료
tk.mainloop()
