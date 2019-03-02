"""
A Graphical user interface for Library mangement system

Title,author
Year,ISBN

User can : 
1)View all records
2)Search an Entry
3)Add an entry
4)Update an entry
5)Close 
"""

from tkinter import *
import Database 


def view_command():
    list1.delete(0,END) 
    for row in Database.view():
        list1.insert(END,row)

def Search_book():
    list1.delete(0,END)
    for books in Database.Search(title_text.get(),year_text.get(),author_text.get(),ISBN_text.get()):
        list1.insert(END,books)
def add_command():
    Database.insert(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())
    list1.delete(0,END)
    list1.insert(END,title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    
def delete_command():
    Database.Delete(selected_tuple[0])

def update_command():
    Database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())
    
 


window=Tk()

window.wm_title("Library Management System")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)
l2=Label(window,text="Author")
l2.grid(row=0,column=2)
l3=Label(window,text="Year")
l3.grid(row=1,column=0)
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

ISBN_text=StringVar()
e4=Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=36)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)


b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12,command=Search_book)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()






