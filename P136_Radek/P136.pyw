from tkinter import *  
from random import *

Num1 = int(0)
Num2 = int(0)
Num3 = int(0)
b = int(0)

def initiation():
    root.geometry("400x500")        

def render():
    global LNum1
    global LNum2
    global LNum3
    global Space
    
    Space = Label(height=2, text="pro vyhru se musi soucet tvych cisel rovnat sedmi")
    Space.grid(row=0, column=0, columnspan= 3)
    
    LNum1= Label(bg= "white", height = 8, width = 15, text = 7)
    LNum1.grid(row = 1, column = 0, padx = 10)
    
    LNum2= Label(bg= "white", height = 8, width = 15, text = 7)
    LNum2.grid(row = 1, column = 1, padx = 10)

    LNum3= Label(bg= "white", height = 8, width = 15, text = 7)
    LNum3.grid(row = 1, column = 2, padx = 10)

    Butn1= Button(bg="yellow", height = 1, width = 15, text = "roztoc", command = Spin)
    Butn1.grid(row = 2, column = 1, pady = 20)
    
    Butn1= Button(bg="yellow", height = 1, width = 15, text = "konec", command = exit)
    Butn1.grid(row = 3, column = 1, pady = 20)    
    
def Vyhra():
        PhotoLabel = Label(image=Photo).grid(row = 4, column=0, columnspan=3)
        Space.config(text=str("VYHRAL JSI! zabralo ti to "+str(b)+" pokusu"))
    
def Spin():
    global Num1
    global Num2
    global Num3
    global b
    
    Num1 = randint(0,99)
    Num2 = randint(0,99)
    Num3 = randint(0,99)
    
    LNum1.config(text=Num1)
    LNum2.config(text=Num2)
    LNum3.config(text=Num3)
    
    if (Num1 + Num2 + Num3 )== 7:
        Vyhra()
    else:
        b += 1
        
def SpinBind(Event):
    Spin()
def SpinBindDebug(Event):
    a=True
    global b
    while a:
        Spin()
        if (Num1 + Num2 + Num3 )== 7:
            a=False
        else:
            pass
    print(b)
def exit():
    root.destroy()
root = Tk()
initiation()
render()
root.bind("<space>", SpinBind)
root.bind("f", SpinBindDebug)
Photo = PhotoImage(file="Win.png")
mainloop()