from tkinter import *



top=Tk()
def addnumber():
    number1=float( numberbox.get())

    number2=float(numberbox2.get())
    results= number1+number2
    resultslabel=Label(text="output = "+str(results))
    resultslabel.pack()

top.title("calulator")
top.minsize(300,300)

numberlabel=Label(text="first number")
numberlabel.pack()

numberbox=Entry()
numberbox.pack()

numberlabel2=Label(text="second number")
numberlabel2.pack()
numberbox2=Entry()
numberbox2.pack()

B =Button( text ="add",command=addnumber)
B.pack()









top.mainloop()