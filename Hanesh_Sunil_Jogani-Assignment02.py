from tkinter import *
from tkinter import messagebox

box = Tk()
box.title("LEAP PhoneBook")
box.resizable(0,0)

contact = {}

# Defining a function add to take in the values from the User
def add():
    c_name = e1.get()
    c_num = e2.get()
    if len(c_name) == 0:
        messagebox.showerror("ERROR", "ENTER THE CONTACT NAME !!!")
    elif len(c_num) == 0:
        messagebox.showerror("ERROR", "ENTER THE CONTACT NUMBER !!!")
    elif c_name in contact:
        messagebox.showerror("ERROR", "THIS CONTACT ALREADY EXISTS !!!")
    else:
        contact[c_name] = c_num
        messagebox.showinfo("INFORMATION", "CONTACT ADDED SUCCESSFULLY !!!")

# Defining a function show to display the output
def show():
    if not contact:
        messagebox.showerror("ERROR", "THERE ARE NO CONTACTS AT PRESENT!!!")
    else:
        for key, value in contact.items():
            print(key, ' : ', value)

# Defining a function delete to delete the contacts entered before
def delete():
    c_name = e1.get()
    if c_name in contact:
        del contact[c_name]
        messagebox.showinfo("INFORMATION", "CONTACT DELETED SUCCESSFULLY !!!")
    else:
        messagebox.showerror("ERROR", "THERE ARE NO CONTACTS TO DELETE !!!")


# Labels
l1 = Label(box, text="Contact Name", bg="snow4", width=20)
l1.grid(row=0, column=1)
l2 = Label(box, text="Contact Number", bg="snow4", width=20)
l2.grid(row=2, column=1)

# Entry widget for taking in the values
e1 = Entry(box, width=30, bg="gray40", fg='white')
e1.grid(row=0, column=2)
e2 = Entry(box, width=30, bg="gray40", fg='white')
e2.grid(row=2, column=2)

# Buttons for different operations taking place.
b2 = Button(box, text="Add", bg="snow4", width=20, command=add)
b2.grid(row=3, column=1)
b3 = Button(box, text="Show All Contacts", bg="snow4", width=20, command=show)
b3.grid(row=4, column=1)
b4 = Button(box, text="Delete", bg="snow4", width=20, command=delete)
b4.grid(row=5, column=1)
b5 = Button(box, text="Quit", bg="snow4", command=box.quit, width=20)
b5.grid(row=6, column=1)

box.mainloop()