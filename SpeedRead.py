import tkinter as tk
import time
root = tk.Tk()
root.wm_title('SpeedRead')
def s1():
    eentry.destroy()
    ebutton.destroy()
    s2()
def s2():
    path = evar.get()
    with open(path) as f:
        global content
        content = f.read()
    s35()
def s35():
    global lst
    lst = []
    for x in content.split():
        lst.append(x)
    s3()
def s3():
    time = 200
    offset = 0
    lett = lst[0]
    if len(lst[0]) % 2 == 0:
        #print(2)
        l = len(lst[0])/2
        lett = lst[0][int(l)]
        for x in lst[0]:
            if x == lett:
                #lst[0] = lst[0].replace(x, " ")
                break
        offset = 18
    else:
        lett = lst[0][int((len(lst[0])+0.5) /2)]
        for x in lst[0]:
            if x == lett:
                #lst[0] = lst[0].replace(x," ")
                break
        offset = 0
    if lst[0][-1] == ".":
        time = 350
    for child in root.winfo_children():
        if child != c:
            child.destroy()
    words = tk.Label(root,text=lst[0],font=("","45",""),bg="#1d1d1d",fg="#454545")
    #letter = tk.Label(root,text=lett,font=("","45",""),bg='#1d1d1d',fg="#a20404",bd=0)
    c.create_window(640-offset,800/3,window=words)
    #c.create_window(1280/2,800/3,window=letter)
    del lst[0]
    if len(lst) > 0:
        root.after(time,s3)
c = tk.Canvas(root,borderwidth=0,highlightthickness=0,width=1280,height=800,bg='#1d1d1d')
evar = tk.StringVar()
eentry = tk.Entry(root,textvariable=evar,width=35,justify='center')
evar.set('Enter File Path')
c.create_window(1280/2,800/3,window=eentry)
ebutton = tk.Button(root,text='Enter',command=s1)
c.create_window(1280/2,800/2,window=ebutton)
c.pack()
root.mainloop()
