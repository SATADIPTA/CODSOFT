#Program to make a simple calculator

from tkinter import*
expression=""
#the variable expression is used to store the expression provided by the user

def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
#This function is used to append the pressed button value to the expression variable

def equalpress():
    try:
        global expression
        total=str(eval(expression))

        equation.set(total)
        expression=""

    except:

        equation.set("error")
        expression=""
#This function evaluates the expression stored in expression variable

def clear():
    global expression
    expression=""
    equation.set("")
#It clears the expression variable and resets the display

if __name__=="__main__":
    root=Tk()
    #Creating the main window

    root.configure(background="light yellow")
    #setting the background colour as light yellow

    root.title("CALCULATOR")
    #Keeping the title

    root.geometry("295x300")
    #setting the dimension as per the programmar's choice

    root.minsize(295,300)
    #setting the minsize so that it cant get compressed

    root.maxsize(295,300)
    #setting the maxsize so that it cant get maximised

    equation=StringVar()
    #tkinter StringVar associated with Entry widget

    expression_field=Entry(root,textvariable=equation)
    #Creating Entry widget

    expression_field.grid(columnspan=4, ipadx=70)
    #grig option places the button in the window application
    #ipadx is the padding in the X direction

    #Now creating the buttons
    b1=Button(root,text='1',fg='white',bg='orange',command=lambda:press(1),height=3,width=9)
    b1.grid(row=2,column=0)

    b2=Button(root,text='2',fg='white',bg='orange',command=lambda:press(2),height=3,width=9)
    b2.grid(row=2,column=1)

    b3=Button(root,text='3',fg='white',bg='orange',command=lambda:press(3),height=3,width=9)
    b3.grid(row=2,column=2)

    b4=Button(root,text='4',fg='white',bg='orange',command=lambda:press(4),height=3,width=9)
    b4.grid(row=3,column=0)

    b5=Button(root,text='5',fg='white',bg='orange',command=lambda:press(5),height=3,width=9)
    b5.grid(row=3,column=1)

    b6=Button(root,text='6',fg='white',bg='orange',command=lambda:press(6),height=3,width=9)
    b6.grid(row=3,column=2)

    b7=Button(root,text='7',fg='white',bg='orange',command=lambda:press(7),height=3,width=9)
    b7.grid(row=4,column=0)

    b8=Button(root,text='8',fg='white',bg='orange',command=lambda:press(8),height=3,width=9)
    b8.grid(row=4,column=1)

    b9=Button(root,text='9',fg='white',bg='orange',command=lambda:press(9),height=3,width=9)
    b9.grid(row=4,column=2)

    b0=Button(root,text='0',fg='white',bg='orange',command=lambda:press(0),height=3,width=9)
    b0.grid(row=5,column=0)

    plus=Button(root,text='+',fg='white',bg='orange',command=lambda:press("+"),height=3,width=9)
    plus.grid(row=2,column=3)

    minus=Button(root,text='-',fg='white',bg='orange',command=lambda:press("-"),height=3,width=9)
    minus.grid(row=3,column=3)

    multiply=Button(root,text='*',fg='white',bg='orange',command=lambda:press("*"),height=3,width=9)
    multiply.grid(row=4,column=3)

    divide=Button(root,text='/',fg='white',bg='orange',command=lambda:press("/"),height=3,width=9)
    divide.grid(row=5,column=3)

    decimal=Button(root,text='.',fg='white',bg='orange',command=lambda:press("."),height=3,width=9)
    decimal.grid(row=6,column=0)

    equal=Button(root,text='=',fg='white',bg='orange',command=equalpress,height=3,width=9)
    equal.grid(row=5,column=1)

    clear=Button(root,text='Clear',fg='white',bg='orange',command=clear,height=3,width=9)
    clear.grid(row=5,column=2)

   
    root.mainloop()
    
