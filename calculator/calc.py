from tkinter import *
window=Tk()

window.title("CALCULATOR")
window.configure(bg="white")
window.attributes("-topmost",1)
window.resizable(False,False)
window.geometry("570x500")

equation=" "
def show(value):
    global equation
    equation+=value
    label.configure(text=equation) 
def clear():
    global equation
    equation=" "
    label.configure(text=equation)
def calculate():
    global equation
    result=" "
    if equation!=" ":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=" "
    label.configure(text=result) 

label=Label(window,width=25,height=2,text="",font=("arial",30))
label.pack()

button1=Button(window,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda: show("1") ).place(x=10,y=100)
button2=Button(window,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda: show("2") ).place(x=150,y=100)
button3=Button(window,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda: show("3") ).place(x=290,y=100)
button4=Button(window,text="c",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="green",command=lambda: clear()).place(x=430,y=100)

button5=Button(window,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda: show("4")  ).place(x=10,y=200)
button2=Button(window,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda: show("5") ).place(x=150,y=200)
button3=Button(window,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda: show("6") ).place(x=290,y=200)
button4=Button(window,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda: show("+")).place(x=430,y=200)

button1=Button(window,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda: show("7")  ).place(x=10,y=300)
button2=Button(window,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda: show("8") ).place(x=150,y=300)
button3=Button(window,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda: show("9") ).place(x=290,y=300)
button4=Button(window,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda: show("-")).place(x=430,y=300)

button1=Button(window,text="0",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda: show("0") ).place(x=10,y=400)
button2=Button(window,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda: show("*")).place(x=150,y=400)
button3=Button(window,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey" ,command=lambda:show("/")).place(x=290,y=400)
button4=Button(window,text="=",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="blue",bg="grey",command=lambda:calculate()).place(x=430,y=400)

window.mainloop()
       




