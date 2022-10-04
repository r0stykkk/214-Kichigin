from tkinter import *
import tkinter
from math import *
import math

Equcheck = 0

bcolor = "#edeceb" #хекс цвет фона
tcolor = "#21201f" #хекс цвет текста

class Main(Frame):
    def __init__(self, root):
        self.img = tkinter.PhotoImage(file="sf.png") 
        super(Main, self).__init__(root)
        self.build()

    def build(self): 
        self.formula = "0"
        self.lbl2 = Label(text="", font=("Georgia Bold", 22, "bold"), bg=bcolor, foreground=tcolor)
        self.lbl2.place(x=40, y=50)
        self.lbl = Label(text=self.formula, font=("Georgia Bold", 33, "bold"), bg=bcolor, foreground=tcolor)
        self.lbl.place(x=40, y=50)

        btns = [

            "C", "DEL", "Equ", "/",
            "1", "2", "3", "*",
            "4", "5", "6", "-",
            "7", "8", "9", "+",
            "ᅠ", "0", "", "="
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg=bcolor, relief="flat",
            foreground=tcolor, font=("Georgia Bold", 15),
            command=com).place(x=x, y=y,
                        width=90,
                        height=70)
            x += 117
            if x > 400:
                x = 10
                y += 81


    
    def logicalc(self, operation):
        global frstint, scndint, thrdint, Equcheck
        if operation == "C":
            self.lbl.place(x=40, y=50)
            self.lbl2.place(x=30, y=50)
            self.formula = ""
            Equcheck = 0
            root.title("CALC")
            self.lbl2.configure(text=" ")
            self.lbl.configure(bg=bcolor, image="")
            self.lbl.configure(font=("Georgia Bold", 33, "bold"))

        elif operation == "Equ":  #квадратное уравнение
            self.lbl2.configure(text="Первое число: ")
            Equcheck += 1
            self.lbl2.place(x=40, y=50)
            self.lbl.place(x=260, y=50)

            if Equcheck == 2:
                frstint = self.formula
                self.formula = "0"
                self.lbl2.configure(text="Второе число:")
                
            elif Equcheck == 3:
                scndint = self.formula
                self.formula = "0"
                self.lbl2.configure(text="Третье число:")

            elif Equcheck == 4:
                thrdint = self.formula
                self.formula = "0"
                frstint = float(frstint)
                scndint = float(scndint)
                thrdint = float(thrdint)
                D = (scndint ** 2) - (4 * frstint * thrdint)
                if D > 0:
                    x1 = (-scndint + sqrt(D)) / (2 * frstint)
                    x2 = (-scndint - sqrt(D)) / (2 * frstint)
                self.lbl2.configure(text="Ответ: " + "xᵃ= " + str(x1) + " xᵇ= " + str(x2), font=("Georgia Bold", 26, "bold"))
                self.lbl.configure(font=("Georgia Bold", 1, "bold"))


       
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "=":
            self.formula = str(eval(self.formula))
        elif operation == "ᅠ":
            if self.formula == "1000-7": #пасхалка
                root.title("ZXC MODE")
                self.lbl.configure(bg="#FFF", image=self.img)

        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = bcolor
    root.geometry("462x542")
    root.title("CALC")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()