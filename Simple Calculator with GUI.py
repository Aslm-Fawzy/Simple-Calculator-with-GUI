#!/usr/bin/env python
# coding: utf-8

# # Calculator with GUI
#  Python offers multiple options for developing a GUI (Graphical User Interface). Out of all the GUI methods, Tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with Tkinter outputs the fastest and easiest way to create GUI applications. Creating a GUI using Tkinter is an easy task.
#  
# ### **Resources :** 
#  1. https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/
#  
#  2. https://www.geeksforgeeks.org/python-gui-tkinter/
#                  
#  3. https://www.analyticsvidhya.com/blog/2022/01/gui-calculator-using-tkinter-python/




import tkinter
from tkinter import *
from tkinter import messagebox
import math

# setting up the tkinter window
root = tkinter.Tk()
root.geometry("250x400+300+300")
#root.resizable(0,0)
root.title("Calculator")

val = ""
A = 0
operator = ""


# function for numerical button clicked

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)


# functions for the operator button click
def btn_plus_clicked():
    global A
    global operator,val
    A = float(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_clicked():
    global A
    global operator,val
    A = float(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mult_clicked():
    global A
    global operator,val
    A = float(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator,val
    A = float(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_c_pressed():
    global A,operator,val
    val = ""
    A = 0
    operator = ""
    data.set(val)

def FACT():
    global A,operator,val
    A = float(val)
    A=math.factorial(A)
    operator="!"
    data.set(A)

def MOD():
    global A,operator,val,b
    A = float(val)
    operator="%"
    val=val + "%"
    data.set(val)

def sqrtt():
    global A,operator,val
    A = float(val)
    A=math.sqrt(A)
    operator="SQRT"
    data.set(A)

def expp():
    global A,operator,val
    A = float(val)
    A=math.exp(A)
    operator="EXP"
    data.set(A)    
    
    

# function to find the result
def result():
    global A,operator,val
    val2 = val
    if operator == "+":
        x = float((val2.split("+")[1]))
        C = A + x
        val = str(C)
        data.set(val)
    if operator == "-":
        x = float((val2.split("-")[1]))
        C = A - x
        val = str(C)
        data.set(val)
    if operator == "*":
        x = float((val2.split("*")[1]))
        C = A * x
        val = str(C)
        data.set(val)
    if operator == "/":
        x = float((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            val = ""
            data.set(val)
        else: 
          C = float(A / x)
          data.set(C)
    
    if operator == "!" :
        x= float(val2) 
        val = str(x)
        data.set(val)  
        #data.set(val.math.factorial)
        
    if operator == "%":
        x= float((val2.split("%")[1])) 
        C = A % x
        val = str(C)
        data.set(val)
        
    if operator == "SQRT": 
        x= float(val2)
        val = str(x)
        data.set(val)
        #data.set(val.math.sqrt)
        
    if operator == "EXP":
        x= float(val2)
        val = str(x)
        data.set(val)
        #data.set(val.math.exp)

  # the label that shows the result
data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand = True, fill = "both")

# the frames section
btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")

btnrow5 = Frame(root)
btnrow5.pack(expand = True, fill = "both")

# The buttons section
btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_1_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_2_isclicked,
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_3_isclicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command =  btn_plus_clicked,
)
btnplus.pack(side = LEFT, expand = True, fill = "both",)

# buttons for frame 2

btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_4_isclicked,
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_5_isclicked,
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_6_isclicked,
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_minus_clicked,
)
btnminus.pack(side = LEFT, expand = True, fill = "both",)

# button for frame 3

btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_7_isclicked,
)
btn7.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_8_isclicked,
)
btn8.pack(side = LEFT, expand = True, fill = "both",)

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_9_isclicked,
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btnmult = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_mult_clicked,
)
btnmult.pack(side = LEFT, expand = True, fill = "both",)

# button for frame4


btnc = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_c_pressed,
)
btnc.pack(side = LEFT, expand = True, fill = "both",)

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_0_isclicked,
)
btn0.pack(side = LEFT, expand = True, fill = "both",)

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = result,
)
btnequal.pack(side = LEFT, expand = True, fill = "both",)

btndiv = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_div_clicked,
)
btndiv.pack(side = LEFT, expand = True, fill = "both",)

# button for frame5

btnFACT = Button(
    btnrow5,
    text = "FACT",
    font = ("Verdana", 12),
    relief = GROOVE,
    border = 0,
    command = FACT,
)
btnFACT.pack(side = LEFT, expand = True, fill = "both",)

btnexp = Button(
    btnrow5,
    text = "EXP",
    font = ("Verdana", 12),
    relief = GROOVE,
    border = 0,
    command = expp,
)
btnexp.pack(side = LEFT, expand = True, fill = "both",)

btnMOD = Button(
    btnrow5,
    text = "MOD",
    font = ("Verdana", 12),
    relief = GROOVE,
    border = 0,
    command =MOD ,
)
btnMOD.pack(side = LEFT, expand = True, fill = "both",)

btnsqrt = Button(
    btnrow5,
    text = "SQRT",
    font = ("Verdana", 12),
    relief = GROOVE,
    border = 0,
    command = sqrtt,
)
btnsqrt.pack(side = LEFT, expand = True, fill = "both",)

root.mainloop()


# In[ ]:




