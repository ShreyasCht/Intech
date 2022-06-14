import sys
import mysql.connector as ms
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import database_code

database_name = 'student_management_system'
database_code.Database_Creation(database_name)

connection = ms.connect(host="localhost", user="root", passwd="Shreyas25%")
cur = connection.cursor()


def open_d():
    """Function To Open Connection To Database"""
    try:
        cur.execute("use {}".format(database_name))  # Name of my database is 'database_name'
    except Exception as e:
        response = messagebox.showerror("ERROR!", e)


def personal_records():
    """Funtion To Show Submenu Of Personal Records"""
    global frame2
    try:
        frame2.destroy()
    except:
        pass
    root.geometry("950x400")
    frame2 = LabelFrame(root, bg="#414F4B", text="Personal Record", padx=10, pady=10, font=("Verdana", 10, "bold"))
    frame2.grid(row=2, column=1, padx=20, pady=10)
    Button(frame2, text="View/Update Records", width=25, command=v_u_p_rec, font=("David", 10, "bold")) \
        .grid(row=0, column=0, padx=5, pady=5)


def v_u_p_rec():
    pass


def view_homework():
    """Function To Show Submenu Of View Homework"""
    global frame2
    try:
        frame2.destroy()
    except:
        pass
    root.geometry("950x400")
    frame2 = LabelFrame(root, bg="#414F4B", text="View Homework", padx=10, pady=10, font=("Verdana", 10, "bold"))
    frame2.grid(row=2, column=1, padx=10, pady=10)
    Button(frame2, text="View All Homework", command=vah, font=("David", 10, "bold")) \
        .grid(row=0, column=0, padx=5, pady=5)
    Button(frame2, text="View Pending Homework", command=vph, font=("David", 10, "bold")) \
        .grid(row=0, column=1, padx=5, pady=5)
    Button(frame2, text="View Submitted Homework", command=vsh, font=("David", 10, "bold")) \
        .grid(row=0, column=2, padx=5, pady=5)


def vah():
    """Function To Show Submenu Of View All Homework"""
    global frame2
    try:
        frame2.destroy()
    except:
        pass
    root.geometry("950x400")
    frame2 = LabelFrame(root, bg="#414F4B", text="View All Homework", padx=10, pady=10, font=("Verdana", 10, "bold"))
    frame2.grid(row=2, column=1, padx=10, pady=10)
    Button(frame2, text="Physics", command=p_a_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=0, padx=5, pady=5)
    Button(frame2, text="Chemistry", command=c_a_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=1, padx=5, pady=5)
    Button(frame2, text="Maths", command=m_a_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=2, padx=5, pady=5)


def p_a_hw():
    pass


def c_a_hw():
    pass


def m_a_hw():
    pass


def vph():
    """Function To Show Submenu Of View Pending Homework"""
    global frame2
    try:
        frame2.destroy()
    except:
        pass
    root.geometry("950x400")
    frame2 = LabelFrame(root, bg="#414F4B", text="View Pending Homework", padx=10, pady=10, font=("Verdana", 10, "bold"))
    frame2.grid(row=2, column=1, padx=10, pady=10)
    Button(frame2, text="Physics", command=p_p_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=0, padx=5, pady=5)
    Button(frame2, text="Chemistry", command=c_p_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=1, padx=5, pady=5)
    Button(frame2, text="Maths", command=m_p_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=2, padx=5, pady=5)


def p_p_hw():
    pass


def c_p_hw():
    pass


def m_p_hw():
    pass


def vsh():
    """Function To Show Submenu Of View Submitted Homework"""
    global frame2
    try:
        frame2.destroy()
    except:
        pass
    root.geometry("950x400")
    frame2 = LabelFrame(root, bg="#414F4B", text="View Submitted Homework", padx=10, pady=10,
                        font=("Verdana", 10, "bold"))
    frame2.grid(row=2, column=1, padx=10, pady=10)
    Button(frame2, text="Physics", command=p_s_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=0, padx=5, pady=5)
    Button(frame2, text="Chemistry", command=c_s_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=1, padx=5, pady=5)
    Button(frame2, text="Maths", command=m_s_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=2, padx=5, pady=5)


def p_s_hw():
    pass


def c_s_hw():
    pass


def m_s_hw():
    pass


def submit_homework():
    pass


def view_submitted_homework():
    pass


def report_card():
    pass


def student_list():
    pass


def teachers_list():
    pass


def close():
    """"Function To Exit The Application"""

    def quitprog():
        response = messagebox.showinfo("CLOSED", "Portal Closed")
        connection.close()
        sys.exit()

    def noquit():
        frame2.destroy()

    global frame2
    try:
        frame2.destroy()
    except:
        pass
    root.geometry("950x400")
    frame2 = LabelFrame(root, bg="#414F4B", text="CONFIRM EXIT", padx=10, pady=10, font=("Verdana", 10, "bold"))
    frame2.grid(row=2, column=1, padx=10, pady=10)
    Button(frame2, text="No, Take Me Back", width=25, font=("David", 10, "bold"), command=noquit) \
        .grid(row=0, column=0, padx=5, pady=5)
    Button(frame2, text="Yes, I Want To Quit", width=25, command=quitprog, font=("David", 10, "bold")) \
        .grid(row=0, column=1, padx=5, pady=5)


root = tk.Tk()  # Tk is used to create a main window
root.title("H.C.E.T Syndicate School Portal")
root.geometry("950x400")
root.eval('tk::PlaceWindow . center')  # Positions the new screen window to open up in the center of the screen
root['background'] = "#5E889F"  # HexDecimal colour code

lbl1 = Label(root, text="Student Portal", font=("Lucida Bright", 20, "bold", "underline"))\
    .grid(row=0, column=1, columnspan=2, pady=(10, 0))

frame = LabelFrame(root, bg="#414F64", text="MAIN MENU", padx=5, pady=20, font=("Verdana", 10, "bold"))
frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

btn1 = Button(frame, text="Personal Records", command=personal_records, width=25, state=NORMAL,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=0, padx=8, pady=15)

btn2 = Button(frame, text="View Homework", command=view_homework, width=25, state=NORMAL,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=1, padx=8, pady=15)

btn3 = Button(frame, text="Submit Homework", command=submit_homework, width=25, state=NORMAL,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=2, padx=8, pady=15)

btn4 = Button(frame, text="View Homework Answers", command=view_submitted_homework, width=25, state=NORMAL,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=3, padx=8, pady=15)

btn5 = Button(frame, text="Report Card", command=report_card, width=25, state=NORMAL,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=1, column=0, padx=8, pady=15)

btn6 = Button(frame, text="Student List", command=student_list, width=25, state=NORMAL,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=1, column=1, padx=8, pady=15)

btn7 = Button(frame, text="Teachers List", command=teachers_list, width=25, state=NORMAL,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=1, column=2, padx=8, pady=15)

btn8 = Button(frame, text="Exit The Program", command=close, width=25, state=NORMAL,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=1, column=3, padx=8, pady=15)


root.mainloop()

connection.close()
