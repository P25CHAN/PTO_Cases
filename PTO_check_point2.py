from tkinter import *
from tkinter import messagebox
from xlwt import Workbook, easyxf, easyfont

content_list = []

def add_info():
    a = ticket.get()
    b = summary.get()
    c = reporter.get()
    d = status.get()
    e = actions.get()
    content_list.append(a+","+b+","+c+","+d+","+e)
    #print(content_list)
    add_files()
    excel_file(a, b, c, d, e)
    messagebox.showinfo("Saved", "It was added successsfully!")
    ticket.set("")
    summary.set("")
    reporter.set("")
    status.set("")
    actions.set("")
    check_files()

def delete_info():
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

def excel_file(pos1, pos2, pos3, pos4, pos5):
    row = 1
    wb = Workbook()
    style1 = easyxf("font: color red; align: vert centre, horiz centre; font: bold 1, height 300")
    sheet1 = wb.add_sheet("Sheet 1")
    while True:
        sheet1.write(0,0, str("TICKET #"), style1)
        sheet1.col(0).width = 5000
        sheet1.write(row,0, str(pos1))
            
        sheet1.write(0,1, str("SUMMARY"), style1)
        sheet1.col(1).width = 14000
        sheet1.write(row,1, str(pos2))
        
        sheet1.write(0,2, str("REPORTER"), style1)
        sheet1.col(2).width = 10000
        sheet1.write(row,2, str(pos3))
        
        sheet1.write(0,3, str("STATUS"), style1)
        sheet1.col(3).width = 10000
        sheet1.write(row,3, str(pos4))
        
        sheet1.write(0,4, str("ACTIONS"), style1)
        sheet1.col(4).width = 10000
        sheet1.write(row,4, str(pos5))
        wb.save("xlwt example.xls")
        row += 1
        information = wb
        save_info(information)
        break

def save_info(information):
    wb.save("xlwt example.xls")
    messagebox.showinfo("Saved", "It was saved successsfully!")
    
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
add_lines = StringVar()
save_tickets = StringVar()
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
add_option = Button(interface_agenda, text = "Add!", command = add_info, bg = "#009", fg = "white").place (x = 180, y = 230)
delete_option = Button(interface_agenda, text = "Delete!", command = delete_info, bg = "#009", fg = "white").place (x = 470, y = 110)
save_option = Button(interface_agenda, height=1, width=5, text = "Save!", font =("gothic", 20), command = save_info, bg = "#009", fg = "red").place (x = 670, y = 80)

if __name__ == '__main__':
    load_files()
    check_files()
    mainloop()