import tkinter as tk
from tkinter import *
from Stocks import *
stock = Stock("amzn")
stock.Name()
stock.Value()
stock.Change(True)
root = Tk()
root.title("Stocks")
c = Canvas(root,height=300,width=300,borderwidth=0,highlightthickness=0,bg="#050a52")
stock.tklabel(150,150,c,"#8b8b8b",48)
c.pack()
root.mainloop()
