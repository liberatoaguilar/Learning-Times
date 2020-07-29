from bs4 import BeautifulSoup
from urllib.request import urlopen
#url = urlopen("http://www.motivationalquotes101.com/")
#soup = BeautifulSoup(url, "html.parser")
#got = soup.find("strong").text
got = "Do or do not. There is no try. - Master Yoda"
print(got.upper().split())
got = got.upper().split()
got5 = got[21:]
got4 = got[17:21]
got3 = got[13:17]
got2 = got[9:13]
got1 = got[5:9]
got = got[:5]
import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("Motivational Quotes")
c = tk.Canvas(root,bg="black",borderwidth=0,highlightthickness=0,height=300,width=300)
c.create_text(150,90,text=got,fill="white",justify=CENTER,font=(" ",15,"bold"))
c.create_text(150,120,text=got1,fill="white",justify=CENTER,font=(" ",15,"bold"))
c.create_text(150,150,text=got2,fill="white",justify=CENTER,font=(" ",15,"bold"))
c.create_text(150,180,text=got3,fill="white",justify=CENTER,font=(" ",15,"bold"))
c.create_text(150,210,text=got4,fill="white",justify=CENTER,font=(" ",15,"bold"))
c.create_text(150,240,text=got5,fill="white",justify=CENTER,font=(" ",15,"bold"))
c.pack(expand=YES,fill=BOTH)
root.mainloop()
