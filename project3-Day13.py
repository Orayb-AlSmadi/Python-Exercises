#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 10:03:19 2019

@author: owner
"""
import sqlite3
conn = sqlite3.connect('OrgDB.db')
from tkinter import *
from tkinter import Tk
from tkinter import scrolledtext
from tkinter import messagebox
import functools
root=Tk()
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
w="500x500+"+str(int((screen_width-500)/2))+"+"+str(int((screen_height-500)/2))
root.geometry(w)


# =============================================================================
# x= conn.cursor()
# x.execute('''CREATE TABLE employee
#            (number int, name text, gender text, nationality text, dateofbirth text,address text,deparment text,salary real)''')
# conn.commit()
# conn.close()
# =============================================================================

def addEmployee():
    def saveEmployee():
        x= conn.cursor()
        x.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?)",(val1.get(),val2.get(),val3.get(),val4.get(),val5.get(),val6.get(),val7.get(),val8.get()))
        conn.commit()

        
    c=Toplevel(root)
    c.title(' window')
    c.geometry('400x400')
    number=Label(c,text="Number").place(x=30,y=50)
    name=Label(c,text="Name").place(x=30,y=90)
    gender=Label(c,text="gender").place(x=30,y=120)
    nationality=Label(c,text="nationality").place(x=30,y=150)
    dateofbirth=Label(c,text="dateofbirth").place(x=30,y=170)
    address=Label(c,text="address").place(x=30,y=200)
    deparment=Label(c,text="deparment").place(x=30,y=220)
    salary=Label(c,text="salary").place(x=30,y=240)
    button=Button(c,text="Save",command=saveEmployee).place(x=150,y=260)
    val1=IntVar()
    val2=StringVar()
    val3=StringVar()
    val4=StringVar()
    val5=StringVar()
    val6=StringVar() 
    val7=StringVar()
    val8=IntVar()
    e1=Entry(c,textvariable=val1).place(x=100,y=60)
    e2=Entry(c,textvariable=val2).place(x=100,y=90)
    e3=Entry(c,textvariable=val3).place(x=100,y=120)
    e4=Entry(c,textvariable=val4).place(x=100,y=150)
    e5=Entry(c,textvariable=val5).place(x=100,y=170)
    e6=Entry(c,textvariable=val6).place(x=100,y=200)
    e7=Entry(c,textvariable=val7).place(x=100,y=220)
    e8=Entry(c,textvariable=val8).place(x=100,y=240)


def viewEmployee():
    x = conn.cursor()
    x.execute("SELECT * FROM employee")
    
    c=Toplevel(root)
    c.title(' window')
    c.geometry('400x250')
    txt = scrolledtext.ScrolledText(c, width=200, height=200, wrap=WORD)
    for row in x:
        txt.insert(END,row)
        txt.insert(END,"\n")
    
    txt.yview(END)
    txt.pack()
    conn.commit() 




top=Menu(root)
root.config(menu=top)
file=Menu(top,tearoff=0)
file.add_command(label='Add employee',command=addEmployee)
file.add_command(label='view employee',command=viewEmployee)
file.add_separator()
file.add_command(label='Quit',command=root.destroy)
top.add_cascade(label='File',menu=file)
root.mainloop()