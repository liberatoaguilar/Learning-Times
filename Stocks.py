import tkinter as tk
from tkinter import *
import urllib.request
from bs4 import BeautifulSoup
class Stock(object):
    def __init__(self,url):
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
        url_req = urllib.request.Request("http://www.marketwatch.com/investing/stock/" + url, headers=headers)
        self.url = urllib.request.urlopen(url_req)
        self.stockname = url.upper()
        self.soup = BeautifulSoup(self.url,"html.parser")
        self.worth = str(self.soup.find("p","data bgLast"))
        self.color = ""
        self.uod = str(self.soup.find("span","bgChange"))
        self.uodp = str(self.soup.find("span", "bgPercentChange"))
        if self.uod[0] == "-":
            self.color = "red"
        else:
            self.color = "green"
    def Name(self):
        print(self.stockname)
    def Value(self):
        print(self.worth)
    def Change(self, x):
        print(self.uod)
        if x == True:
            print(self.uodp)
    def tklabel(self,p1,p2,root,color,size):
        root.create_text(p1,p2,text=self.worth,fill=color,font=(" ",size))
        root.create_text(p1-40,p2+40,text=self.uod,fill=self.color,font=(" ",size-30))
        root.create_text(p1+40,p2+40,text=self.uodp,fill=self.color,font=(" ",size-30))
        root.create_text(p1-13,p2-40,text=self.stockname,fill=color,font=(" ",size-18))
