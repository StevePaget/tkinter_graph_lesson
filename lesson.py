import tkinter as tk
from tkinter import font as tkFont

class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1500x800+0+0")
        self.titlefont = tkFont.Font(family="Arial", size=30, slant="italic")

        # ust a title label
        l0 = tk.Label(text="Graph App", bg="#ffaaaa", font=self.titlefont)
        l0.grid(row=0,column=0, columnspan=4, sticky="NSEW")

        # Another little label
        l1 = tk.Label(text="Enter values below:" )
        l1.grid(row=0, column=0)

        # The entry box for typing in numbers
        self.entry = tk.Entry(width=30)
        self.entry.grid(row=0, column=0)

        # A submit button
        b1 =tk.Button(text="Add", command = self.add)
        b1.grid(row=0, column=0)

        # The canvas for drawing the graph
        self.theCanvas = tk.Canvas(self,width=800, height=400, bg="#ddddff")
        self.theCanvas.grid(row=0, column=0)
        
        # A list of numbers to go into the graph
        self.list = tk.Listbox(width=20, height=20)
        self.list.grid(row=0, column=0)

        # Some formatting to make the columns fit
        self.columnconfigure(2,minsize=100)
        self.columnconfigure(3,weight=1)

        self.drawgraph()
        self.mainloop()


    def drawgraph(self):
        self.theCanvas.delete(tk.ALL) # clears the canvas
        self.theCanvas.create_line(700,50,0,350,fill="black") # draws a line from x,y (700,50) to (0,350) 
        self.theCanvas.create_rectangle(10,10,100,50, fill="red") # draws a rectangle from (10,10) to (100,50)



            
    def add(self):
        # this should add the number in the entry box into the listbox
        # it should only accept numerical values

        self.drawgraph()

app = Main()


        
