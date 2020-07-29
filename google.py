import webbrowser
import tkinter as tk
from tkinter import *
root = tk.Tk()
root.wm_title("Google")
la = tk.Entry(bg='white',width=50)
def get():
    search = la.get()
    sp = search.split()
    b = []
    for x in sp:
        b.append(x)
    num = len(b)
    stri = b[:num]
    for x in stri:
        corr = "+".join(stri)
    print(corr)
    sea = "https://www.google.com/#q=",corr
    webbrowser.open("https://www.google.com/#q="+ corr)
bu = tk.Button(text="Search",command=get)
bu.pack(side=BOTTOM)
la.pack()
root.mainloop()
