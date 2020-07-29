import tkinter as tk
global md
class ResizingCanvas(tk.Canvas):
    def __init__(self,parent,**kwargs):
        tk.Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)
md = {"MD":False}
alllabels = []
root = tk.Tk()
root.wm_title("Notes")
frame= tk.Frame(root,width=600,height=600,bg="#1D1F21")
frame.grid(row=0,column=0)
canvas = ResizingCanvas(frame,borderwidth=0,highlightthickness=0,bg="#1D1F21",height=600,width=600)
vbar= tk.Scrollbar(frame,orient="vertical",bg="#1D1F21",activebackground="#1D1F21")
vbar.config(command=canvas.yview)
write = tk.Text(root,width=74,height=37,bg="#1D1F21",fg="white",highlightthickness=0,insertbackground="white",wrap="word")
write.focus()
origY = canvas.yview()[0]
def on_vertical(event):
    canvas.yview_scroll(-1 * event.delta, 'units')
def togglemd(event=None):
    if md["MD"] == False:
        md["MD"] = True
        canvas.bind_all('<MouseWheel>', on_vertical)
        #vbar.pack(side="right",fill='y')
        inputtext = write.get("1.0",'end-1c')
        inputtext2 = inputtext.replace("\n"," \n ").split(" ")
        # The # Headers
        Headers1 = []
        d1 = 0
        for x in range(len(inputtext2)):
            if inputtext2[x] == "#":
                d1 += 1
                Headers1.append([])
                c1 = 1
                while inputtext2[x+c1] != "\n":
                    Headers1[d1-1].append(inputtext2[x+c1])
                    c1 += 1
        # The ## Headers
        Headers2 = []
        d = 0
        for x in range(len(inputtext2)):
            if inputtext2[x] == "##":
                d += 1
                Headers2.append([])
                c = 1
                while inputtext2[x+c] != "\n":
                    Headers2[d-1].append(inputtext2[x+c])
                    c += 1
        # The ### Headers
        Headers3 = []
        d3 = 0
        for x in range(len(inputtext2)):
            if inputtext2[x] == "###":
                d3 += 1
                Headers3.append([])
                c3 = 1
                while inputtext2[x+c3] != "\n":
                    Headers3[d3-1].append(inputtext2[x+c3])
                    c3 += 1
        # Lists with -
        Lists = []
        d4 = 0
        for x in range(len(inputtext2)):
            if inputtext2[x] == "-":
                d4 += 1
                Lists.append([])
                c4 = 1
                while inputtext2[x+c4] != "\n":
                    Lists[d4-1].append(inputtext2[x+c4])
                    c4 += 1
        # Italics
        Italics = []
        d5 = 0
        for x in range(len(inputtext2)):
            try:
                if inputtext2[x][0] == "*" and inputtext2[x][1] != "*":
                    d5 += 1
                    Italics.append([])
                    c5 = 0
                    while inputtext2[x+c5][-1] != "*":
                        Italics[d5-1].append(inputtext2[x+c5])
                        c5 += 1
                    Italics[-1].append(inputtext2[x+c5])
            except:
                pass
        # Bold
        Bold = []
        d6 = 0
        for x in range(len(inputtext2)):
            try:
                if inputtext2[x][0] == "*" and inputtext2[x][1] == "*":
                    d6 += 1
                    Bold.append([])
                    c6 = 0
                    while inputtext2[x+c6][-1] != "*":
                        Bold[d6-1].append(inputtext2[x+c6])
                        c6 += 1
                    Bold[-1].append(inputtext2[x+c6])
            except:
                pass
        #Markdown View
        write.configure(state="normal",fg="#1D1F21",height=0,width=0)
        linelist = []
        count = 0
        for x in range(len(inputtext2)):
            if inputtext2[x] != "\n":
                linelist.append([])
                linelist[count].append(inputtext2[x])
            else:
                count += 1
        for x in range(len(linelist)):
            linelist[x] = str(linelist[x]).replace(']',"").replace('[',"").replace(", "," ").replace(",,",",").replace("'",'')
        onlylist = []
        for y in range(len(linelist)):
            try:
                if linelist[y] != '':
                    onlylist.append(linelist[y])
                elif linelist[y] == '' and linelist[y+1] != '':
                    linelist[y] = "  "
                    onlylist.append(linelist[y])
            except:
                pass
        #The Good Stuff
        g = 0
        scroller1 = 500
        scroller2 = 500
        for z in onlylist:
            canvas.config(yscrollcommand=vbar.set,scrollregion=(0,0,scroller1,scroller2))
            if z[0] == "#" and z.replace("## ","") in str(Headers2).replace(']',"").replace('[',"").replace(",","").replace("'",''):
                for x in Headers2:
                    if z.replace("## ","") == str(x).replace(']',"").replace('[',"").replace(",","").replace("'",''):
                        label = tk.Label(text=str(x).replace(']',"").replace('[',"").replace(",","").replace("'",''),fg='white',bg="#1D1F21",font=("Helvetica",17), anchor="w",width=60)
                        canvas.create_window(318,60+g,window=label)
                        alllabels.append(label)
                        g+=48
                        scroller1 += 56
                        scroller2 += 56
            elif z[0] == "#" and z.replace("# ","") in str(Headers1).replace(']',"").replace('[',"").replace(",","").replace("'",''):
                for x in Headers1:
                    if z.replace("# ","") == str(x).replace(']',"").replace('[',"").replace(",","").replace("'",''):
                        label = tk.Label(text=str(x).replace(']',"").replace('[',"").replace(",","").replace("'",''),fg='white',bg="#1D1F21",font=("Helvetica",24), anchor="w",width=36)
                        canvas.create_window(282,60+g,window=label)
                        alllabels.append(label)
                        g+=42
                        scroller1 += 23
                        scroller2 += 23
            elif z[0] == "#" and z.replace("### ","") in str(Headers3).replace(']',"").replace('[',"").replace(",","").replace("'",''):
                for x in Headers3:
                    if z.replace("### ","") == str(x).replace(']',"").replace('[',"").replace(",","").replace("'",''):
                        label = tk.Label(text=str(x).replace(']',"").replace('[',"").replace(",","").replace("'",''),fg='white',bg="#1D1F21",font=("Helvetica",15), anchor="w",width=60)
                        canvas.create_window(288,60+g,window=label)
                        alllabels.append(label)
                        g+=24
                        scroller1 += 23
                        scroller2 += 23
            elif z[0] == "-" and z.replace("- ","") in str(Lists).replace(']',"").replace('[',"").replace(",","").replace("'",''):
                for x in Lists:
                    if z.replace("- ","") == str(x).replace(']',"").replace('[',"").replace(",","").replace("'",''):
                        label = tk.Label(text=z.replace("-","•"),fg='grey',bg="#1D1F21",font=("Helvetica",13), anchor="w",width=84,justify="left",wraplength=480)
                        canvas.create_window(404,60+g,window=label)
                        alllabels.append(label)
                        g+=24
                        scroller1 += 23
                        scroller2 += 23
            elif z[0] == "*" and z[1] == "*" and z in str(Bold).replace(']',"").replace('[',"").replace(",","").replace("'",''):
                for x in Bold:
                    print(z,x)
                    if z == str(x).replace(']',"").replace('[',"").replace(",","").replace("'",''):
                        label = tk.Label(text=z.replace("**",""),fg='grey',bg="#1D1F21",font=("Helvetica",13,"bold"), anchor="w",width=84,justify="left",wraplength=480)
                        canvas.create_window(384,60+g,window=label)
                        alllabels.append(label)
                        g+=24
                        scroller1 += 23
                        scroller2 += 23
            else:
                label = tk.Label(text=z,fg='grey',bg="#1D1F21",font=("Helvetica",13), anchor="w",width=84,justify="left",wraplength=480)
                canvas.create_window(384,60+g,window=label)
                alllabels.append(label)
                g+=24
                scroller1 += 23
                scroller2 += 23
        canvas.addtag_all("all")
    elif md["MD"] == True:
        canvas.unbind_all('<MouseWheel>')
        md["MD"] = False
        canvas.yview_moveto(origY)
        write.configure(width=74,height=37,bg="#1D1F21",fg="white",highlightthickness=0,insertbackground="white",wrap="word")
        for label in alllabels:
            label.destroy()
        #vbar.pack_forget()
        canvas.config(yscrollcommand=None,scrollregion=None)
canvas.addtag_all("all")
canvas.create_window(294,316,window=write)
frame.pack(expand='yes',fill='both')
canvas.pack(side="left",expand='yes',fill="both")
root.bind("<Command-i>",togglemd)
root.mainloop()
