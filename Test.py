from tkinter import *
from tkinter import messagebox

content_list = []

def save():
    a = names_users.get()
    b = lastnames_users.get()
    c = email_users.get()
    d = phone_users.get()
    content_list.append(a+"$"+b+"$"+c+"$"+d)
    add_files()
    messagebox.showinfo("Saved", "It was saved successsfully!")
    names_users.set("")
    lastnames_users.set("")
    email_users.set("")
    phone_users.set("")
    check_files()

def delete():
    print("Bye")

def check_files():
    x = Text(interface_agenda, width = 80, height = 15)
    content_list.sort()
    values = []
    x.insert(INSERT, "Name\t\tLast Name\t\tEmail\t\tPhone\n")
    for item in content_list:
        sort_lines = item.split("$")
        values.append(sort_lines[2])
        x.insert(INSERT, sort_lines[0]+"\t\t"+sort_lines[1]+"\t\t"+sort_lines[2]+"\t\t"+sort_lines[3]+"\t\n")
    x.place (x = 20, y = 230)
    delete_line = Spinbox(interface_agenda, value = (values), textvariable = delete_users).place (x = 450, y = 80)
    if content_list == []:
        delete_box = Spinbox(interface_agenda, value = (values)).place (x = 450, y = 80)
    x.config(state = DISABLED)

def my_files():
    archive = open("My_agenda.txt", "a")
    archive.close()

def load_files():
    archive = open("My_agenda.txt", "r")
    line = archive.readline()
    if line:
        while line:
            if line [-1] == '\n':
                line = line [:-1]
            content_list.append(line)
            line = archive.readline()
    archive.close()

def add_files():
    archive = open("My_agenda.txt", "w")
    content_list.sort()
    for item in content_list:
        archive.write(item + "\n")
    archive.close()

interface_agenda = Tk()
names_users = StringVar()
lastnames_users = StringVar()
email_users = StringVar()
phone_users = StringVar()
delete_users = StringVar()
table_color = "#006"
letter_color = "#FFF"
interface_agenda.title("My Project Agenda!")
interface_agenda.geometry("700x500")
interface_agenda.configure(background = table_color)
tittle_line = Label(interface_agenda, text = "My Files!", bg = table_color, fg = letter_color, font =("Helvetica", 16)).place(x = 300, y = 25)
name_line = Label(interface_agenda, text = "Name:", bg =  table_color, fg = letter_color).place (x = 50, y = 80)
name_box = Entry(interface_agenda, textvariable = names_users).place (x = 150, y = 80)
lastname_line = Label(interface_agenda, text = "Last Name:", bg =  table_color, fg = letter_color).place (x = 50, y = 110)
lastname_box = Entry(interface_agenda, textvariable = lastnames_users).place (x = 150, y = 110)
email_line = Label(interface_agenda, text = "Email:", bg =  table_color, fg = letter_color).place (x = 50, y = 140)
email_box = Entry(interface_agenda, textvariable = email_users).place (x = 150, y = 140)
phone_line = Label(interface_agenda, text = "Phone:", bg =  table_color, fg = letter_color).place (x = 50, y = 170)
phone_box = Entry(interface_agenda, textvariable = phone_users).place (x = 150, y = 170)
delete_line = Label(interface_agenda, text = "Phone:", bg = table_color, fg = letter_color).place (x = 370, y = 80)
delete_box = Spinbox(interface_agenda, textvariable = delete_users).place (x = 450, y = 80)
save_option = Button(interface_agenda, text = "Save!", command = save, bg = "#009", fg = "white").place (x = 180, y = 200)
delete_option = Button(interface_agenda, text = "Delete!", command = delete, bg = "#009", fg = "white").place (x = 470, y = 110)

load_files()
check_files()
mainloop()