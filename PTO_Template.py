from tkinter import *
from tkinter import messagebox

content_list = []

def save():
    a = ticket.get()
    b = summary.get()
    c = reporter.get()
    d = status.get()
    e = actions.get()
    content_list.append(a+","+b+","+c+","+d+","+e)
    add_files()
    messagebox.showinfo("Saved", "It was saved successsfully!")
    ticket.set("")
    summary.set("")
    reporter.set("")
    status.set("")
    actions.set("")
    check_files()

def delete():
    d = delete_case.get()
    removed = False
    for item in content_list:
        sort_lines = item.split(",")
        if delete_case.get() == sort_lines[0]:
            content_list.remove(item)
            removed = True
    add_files()
    check_files()
    if removed:
        messagebox.showinfo("Deleted", "Item was deleted! " + d)

def check_files():
    x = Text(interface_agenda, width = 131, height = 25)
    content_list.sort()
    values = []
    x.insert(INSERT, "TICKET\t\tSUMMARY\t\t\t\t\tREPORTER\t\t\tSTATUS\t\t\tACTIONS\n")
    for item in content_list:
        sort_lines = item.split(",")
        values.append(sort_lines[0])
        x.insert(INSERT, sort_lines[0]+"\t\t"+sort_lines[1]+"\t\t\t\t\t"+sort_lines[2]+"\t\t\t"+sort_lines[3]+"\t\t\t"+sort_lines[4]+"\t\n")
    x.place (x = 20, y = 270)
    delete_line = Spinbox(interface_agenda, value = (values), textvariable = delete_case).place (x = 450, y = 80)
    if content_list == []:
        delete_box = Spinbox(interface_agenda, value = (values)).place (x = 450, y = 80)
    x.config(state = DISABLED)
    excel_file()

def excel_file():
    z = 'C:\\Users\\juan\\Documents\\Python Proyect\\PTO_Cases\\My_agenda1.txt'
    archive = open(z, "w")
    content_list.sort()
    for item in content_list:
        archive.write(item + "\n")
    archive.close()

def my_files():
    z = 'C:\\Users\\juan\\Documents\\Python Proyect\\PTO_Cases\\My_agenda.txt'
    archive = open(z, "a")
    archive.close()

def load_files():
    z = 'C:\\Users\\juan\\Documents\\Python Proyect\\PTO_Cases\\My_agenda.txt'
    archive = open(z, "r")
    line = archive.readline()
    if line:
        while line:
            if line [-1] == '\n':
                line = line [:-1]
            content_list.append(line)
            line = archive.readline()
    archive.close()

def add_files():
    z = 'C:\\Users\\juan\\Documents\\Python Proyect\\PTO_Cases\\My_agenda.txt'
    archive = open(z, "w")
    content_list.sort()
    for item in content_list:
        archive.write(item + "\n")
    archive.close()

interface_agenda = Tk()
ticket = StringVar()
summary = StringVar()
reporter = StringVar()
status = StringVar()
actions = StringVar()
delete_case = StringVar()
table_color = "#416"
letter_color = "#FFA"
interface_agenda.title("My Project Agenda!")
interface_agenda.geometry("1100x700")
interface_agenda.configure(background = table_color)
tittle_line = Label(interface_agenda, text = "My Files!", bg = table_color, fg = letter_color, font =("gothic", 25)).place(x = 280, y = 25)
ticket_line = Label(interface_agenda, text = "TICKET:", bg =  table_color, fg = letter_color, font =("gothic", 14)).place (x = 50, y = 80)
ticket_box = Entry(interface_agenda, textvariable = ticket).place (x = 170, y = 80)
summary_line = Label(interface_agenda, text = "SUMMARY:", bg =  table_color, fg = letter_color, font =("gothic", 14)).place (x = 50, y = 110)
summary_box = Entry(interface_agenda, textvariable = summary).place (x = 170, y = 110)
reporter_line = Label(interface_agenda, text = "REPORTER:", bg =  table_color, fg = letter_color, font =("gothic", 14)).place (x = 50, y = 140)
reporter_box = Entry(interface_agenda, textvariable = status).place (x = 170, y = 140)
status_line = Label(interface_agenda, text = "STATUS:", bg =  table_color, fg = letter_color, font =("gothic", 14)).place (x = 50, y = 170)
status_box = Entry(interface_agenda, textvariable = reporter).place (x = 170, y = 170)
actions_line = Label(interface_agenda, text = "ACTIONS:", bg = table_color, fg = letter_color, font =("gothic", 14)).place (x = 50, y = 200)
actions_box = Entry(interface_agenda, textvariable = actions).place (x = 170, y = 200)
delete_line = Label(interface_agenda, text = "DELETE!", bg = table_color, fg = letter_color, font =("gothic", 14)).place (x = 370, y = 80)
delete_box = Spinbox(interface_agenda, textvariable = delete_case).place (x = 450, y = 80)
save_option = Button(interface_agenda, text = "Save!", command = save, bg = "#009", fg = "white").place (x = 180, y = 230)
delete_option = Button(interface_agenda, text = "Delete!", command = delete, bg = "#009", fg = "white").place (x = 470, y = 110)

if __name__ == '__main__':
    load_files()
    check_files()
    mainloop()



