import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
 
def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['Artist_ID'])
    e2.insert(0,select['Name'])
    e3.insert(0,select['Birth_Place'])
    e4.insert(0,select['Age'])
    e5.insert(0,select['Style'])


 
 
def Add():

    Name = e2.get()
    Birth_Place = e3.get()
    Age = e4.get()
    Style = e5.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="admin",database="Art_Gallery")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "INSERT INTO  Artist ( Name, Birth_Place, Age, Style) VALUES (%s, %s, %s, %s)"
       val = ( Name, Birth_Place, Age, Style)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Artist inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
      
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
 
def update():
    Artist_ID = e1.get()
    Name = e2.get()
    Birth_Place = e3.get()
    Age = e4.get()
    Style = e5.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="admin",database="Art_Gallery")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "Update  Artist set Name= %s, Birth_Place= %s, Age= %s,  Style =%s where Artist_ID= %s"
       val = (Name, Birth_Place, Age, Style, Artist_ID)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updated successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def delete():
    Artist_ID = e1.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="admin",database="Art_Gallery")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "delete from Artist where Artist_ID = %s"
       val = (Artist_ID,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleted successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="admin", database="Art_Gallery")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT Artist_ID, Name, Birth_Place, Age, Style FROM Artist")
        records = mycursor.fetchall()
        print(records)
 
        for i, (Artist_ID, Name, Birth_Place, Age, Style) in enumerate(records, start=1):
            listBox.insert("", "end", values=(Artist_ID, Name, Birth_Place, Age, Style))
            mysqldb.close()
 
root = Tk()
root.geometry("1000x500")
global e1
global e2
global e3
global e4
global e5
tk.Label(root, text="Artist Management Interface", fg="orange", font=("Helvetica", 30)).place(x=350, y=5)
tk.Label(root, text="Artist ID:", font=("Helvetica", 10)).place(x=10, y=10)
Label(root, text="Artist Name:", font=("Helvetica", 10)).place(x=10, y=40)
Label(root, text="Artist Birth Place:", font=("Helvetica", 10)).place(x=10, y=70)
Label(root, text="Age:", font=("Helvetica", 10)).place(x=10, y=90)
Label(root, text="Style:", font=("Helvetica", 10)).place(x=10, y=120)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
 
e3 = Entry(root)
e3.place(x=140, y=70)
 
e4 = Entry(root)
e4.place(x=140, y=100)

e5 = Entry(root)
e5.place(x=140, y=130)
 
Button(root, text="Add",command = Add,height=2, width= 13,  bg='lightgreen', font=("Helvetica", 10)).place(x=30, y=160)
Button(root, text="update",command = update,height=2, width= 13, bg='lightgray', font=("Helvetica", 10)).place(x=150, y=160)
Button(root, text="Delete",command = delete,height=2, width= 13,  bg='red', font=("Helvetica", 10)).place(x=270, y=160)
 
cols = ("Artist_ID", "Name", "Birth_Place", "Age", "Style")
listBox = ttk.Treeview(root, columns=cols, show='headings' )
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=1)
    listBox.place(x=10, y=220)
 
show()
listBox.bind('<Double-Button-1>',GetValue)
 
root.mainloop()