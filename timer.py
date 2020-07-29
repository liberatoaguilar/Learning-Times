import tkinter as tk
from tkinter import *
import os
root = tk.Tk()
root.title("Timer")
c = tk.Canvas(root,bg="black",borderwidth=0,highlightthickness=0,width=300,height=200)
time = tk.Label(root,bg="black",fg="white",font=(" ",50),text="")
enter = tk.Entry(root)
c.create_window(150,100,window=enter)
def done():
    for x in range(5):
        os.system("echo -e '\a'")
def timer(x):
    time.config(text=x)
    if time.cget("text") > 0:
        root.after(60000,timer,x-1)
        time.config(text=x)
    else:
        root.after(1,done)
        root.after(3000,root.destroy)
def start():
    num = enter.get()
    b.destroy()
    enter.destroy()
    if int(num) > 0:
        c.create_window(150,100,window=time)
        timer(int(num))
b = tk.Button(root,text="Start Timer",command=start)
c.create_window(150,150,window=b)
c.pack()
root.mainloop()
