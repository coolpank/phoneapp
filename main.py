from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import Db

d = Db()

app = Tk()
def clearText():
    first.set('')
    last.set('')
    mobile.set('')

def populatelist():
    rowss = d.fetch()
    for row in rowss:
        lb.insert(END, row)

def submit():
    if first.get() == '' or last.get() == '' or mobile.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields!')
        return
    d.insert(first.get(), last.get(), mobile.get())
    clearText()
    lb.delete(0, END)
    populatelist()

def searching():
    rows = d.search(search.get())
    lb.delete(0, END)
    for row in rows:
        lb.insert(END, row)

app.title("Phoneapp")
#Label
fname = Label(app, text='First Name').grid(row=0, column=0, pady=4, padx=4)
lname = Label(app, text='Last Name').grid(row=0, column=1, pady=4, padx=4)
mno = Label(app, text='Mobile No.').grid(row=0, column=2, pady=4, padx=4)

#Entry widgets
first = StringVar()
Entry(app, width=10, textvariable=first).grid(row=1, column=0, pady=4, padx=4)

last = StringVar()
Entry(app, width=10, textvariable=last).grid(row=1, column=1, pady=4, padx=4)

mobile = StringVar()
Entry(app, width=10, textvariable=mobile).grid(row=1, column=2, pady=4, padx=4)

#Buttons
Button(app, text="Submit", fg='Red', command=submit).grid(row=2, column=0, pady=6, padx=4)

#Searching
search = StringVar()
Entry(app, width=25, textvariable=search).grid(row=3, column=0, columnspan=2, pady=6, padx=4, sticky=W)

Button(app, text='Search', command=searching).grid(row=3, column=2, pady=6, padx=4)

#Listbox
lb = Listbox(app, height=10, width=35)
lb.grid(row=4, column=0, columnspan=3, pady=10, padx=6, sticky=W)

populatelist()

app.mainloop()
