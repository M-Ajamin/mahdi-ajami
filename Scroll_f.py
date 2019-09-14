import tkinter as tk
from DBmanagment import *

dbm = DBmanage("mahdi.db")

class ScrollFrame(tk.Frame):
    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def __init__(self , parent):
        super().__init__(parent)

        self.canvas = tk.Canvas(self, borderwidth = 0 , background = "#FFFFFF")
        self.viewPort = tk.Frame(self.canvas,background = "#FFFFFF" )
        self.vsb = tk.Scrollbar(self,orient = "vertical" , command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.vsb.set )

        self.vsb.pack(side="right" , fill="y")
        self.canvas.pack(side = "left" , fill = "both" , expand = True)
        self.canvas.create_window((4,4),window=self.viewPort,anchor="nw",tags="self.viewPort")

        self.viewPort.bind("<Configure>",self.onFrameConfigure)


class SBIND(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self)
        self.me = []

        SListn = dbm.selectstudentsname()
        Slistf = dbm.selectstudentsfamily()


        for row in range(len(SListn)):
            tk.Label(self.scrollFrame.viewPort, text=str(SListn[row][0])).grid(row=row, column=0 , padx = 20)
        for i in range(len(Slistf)):
            tk.Label(self.scrollFrame.viewPort, text=str(Slistf[i][0])).grid(row=i, column=1, padx=20)
            MS = tk.Entry(self.scrollFrame.viewPort)
            MS.grid(row=i, column=2, padx=20)
            self.me.append(MS)
        self.scrollFrame.pack(side="top", fill="both", expand=True)



