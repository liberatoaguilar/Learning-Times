import time
import tkinter as tk
import os
root = tk.Tk()
root.wm_title("Pomodoro")
c = tk.Canvas(root,borderwidth=0,highlightthickness=0,bg="#800000",height=100,width=200)
c.pack()
t = tk.Label(root,text="25",bg="#800000",fg="#ffffff",font=(" ",28,"bold"))
task = tk.Label(root,text=" ",bg="gray",width=1,height=1)
task2 = tk.Label(root,text=" ",bg="gray",width=1,height=1)
task3 = tk.Label(root,text=" ",bg="gray",width=1,height=1)
task4 = tk.Label(root,text=" ",bg="gray",width=1,height=1)
c.create_window(20,20,window=task)
c.create_window(40,20,window=task2)
c.create_window(60,20,window=task3)
c.create_window(80,20,window=task4)
def stp():
    global credit
    credit = 0
    credit += 10
    if credit >= 10:
        credit -= 10
        timer(25)
num = 1
def comp():
    global num
    num += 1
    task.configure(bg="green")
    c.create_window(20,20,window=task)
    b.destroy()
    c.create_window(49,75,window=longb)
    c.create_window(148,75,window=shortb)
b = tk.Button(root,text="Complete",command=comp)
def comp2():
    global num
    num += 1
    task2.configure(bg="green")
    b2.destroy()
    c.create_window(49,75,window=longb2)
    c.create_window(148,75,window=shortb2)
def comp3():
    global num
    num += 1
    task3.configure(bg="green")
    b3.destroy()
    c.create_window(49,75,window=longb3)
    c.create_window(148,75,window=shortb3)
def comp4():
    global num
    num += 1
    task4.configure(bg="green")
    b4.destroy()
    t.destroy()
    done = tk.Label(root,text="Done!",bg="#800000",fg="#ffffff",font=(" ",28,"bold"))
    c.create_window(100,52,window=done)
def timer(x):
    if x != 0:
        t.configure(text=x)
        root.after(60000, timer, x-1)
    else:
        t.configure(text=0)
        if num == 1:
            c.create_window(100,75,window=b)
        elif num == 2:
            c.create_window(100,75,window=b2)
        elif num == 3:
            c.create_window(100,75,window=b3)
        elif num == 4:
            c.create_window(100,75,window=b4)
        for x in range(1):
            os.system('afplay Desktop/solemn.mp3')
def lbc():
    global credit
    credit = 0
    credit += 10
    if credit >= 10:
        credit -= 10
        longbreak(5)
        longb.destroy()
        shortb.destroy()
def sbc():
    global credit
    credit = 0
    credit += 10
    if credit >= 10:
        credit -=10
        shortbreak(5)
        shortb.destroy()
        longb.destroy()
def lbc2():
    global credit
    credit = 0
    credit += 10
    if credit >= 10:
        credit -= 10
        longbreak2(10)
        shortb2.destroy()
        longb2.destroy()
def lbc3():
    global credit
    credit = 0
    credit += 10
    if credit >= 10:
        credit -= 10
        longbreak3(10)
        shortb3.destroy()
        longb3.destroy()
def sbc2():
    global credit
    credit = 0
    credit += 10
    if credit >= 10:
        credit -= 10
        shortbreak2(5)
        shortb2.destroy()
        longb2.destroy()
def sbc3():
    global credit
    credit = 0
    credit += 10
    if credit >= 10:
        credit -= 10
        shortbreak3(5)
        shortb3.destroy()
        longb3.destroy()
def longbreak(x):
    if x != 0:
        t.configure(text=x)
        root.after(60000,longbreak,x-1)
    else:
        t.configure(text=0)
        os.system("say Break Finished")
        c.create_window(100,75,window=st2)
def longbreak2(x):
    if x != 0:
        t.configure(text=x)
        root.after(60000,longbreak2,x-1)
    else:
        t.configure(text=0)
        os.system("say Break Finished")
        c.create_window(100,75,window=st3)
def longbreak3(x):
    if x != 0:
        t.configure(text=x)
        root.after(60000,longbreak3,x-1)
    else:
        t.configure(text=0)
        os.system("say Break Finished")
        c.create_window(100,75,window=st4)
def shortbreak(x):
    if x != 0:
        t.configure(text=x)
        root.after(60000,shortbreak,x-1)
    else:
        t.configure(text=0)
        os.system("say Break Finished")
        c.create_window(100,75,window = st2)
def shortbreak2(x):
    if x != 0:
        t.configure(text=x)
        root.after(60000,shortbreak2,x-1)
    else:
        t.configure(text=0)
        os.system("say Break Finished")
        c.create_window(100,75,window = st3)
def shortbreak3(x):
    if x != 0:
        t.configure(text=x)
        root.after(60000,shortbreak3,x-1)
    else:
        t.configure(text=0)
        os.system("say Break Finished")
        c.create_window(100,75,window = st4)
def stp1():
    stp()
    st.destroy()
def stp2():
    global b2
    b2 = tk.Button(root,text="Complete",command=comp2)
    stp()
    st2.destroy()
def stp3():
    global b3
    b3 = tk.Button(root,text="Complete",command=comp3)
    stp()
    st3.destroy()
def stp4():
    global b4
    b4 = tk.Button(root,text="Complete",command=comp4)
    stp()
    st4.destroy()
longb = tk.Button(root,text="Long Break",command=lbc)
shortb = tk.Button(root,text="Short Break",command=sbc)
st2 = tk.Button(root,text="Start",command=stp2)
st = tk.Button(root,text="Start",command=stp1)
st3 = tk.Button(root,text="Start",command=stp3)
st4 = tk.Button(root,text="Start",command=stp4)
longb2 = tk.Button(root,text = "Long Break",command=lbc2)
shortb2 = tk.Button(root,text="Short Break",command=sbc2)
shortb3 = tk.Button(root,text="Short Break",command=sbc3)
longb3 = tk.Button(root,text="Long Break", command=lbc3)
st.pack()
t.pack()
c.create_window(100,75,window=st)
c.create_window(140,35,window=t)
root.mainloop()
