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


def v_u_p_rec():
    pass


def homework():
    """Function To Show Submenu Of View Homework"""
    global frame2
    try:
        frame2.destroy()
    except:
        pass
    root.geometry("950x400")
    frame2 = LabelFrame(root, bg="#414F4B", text="Homework", padx=10, pady=10, font=("Verdana", 10, "bold"))

    frame2.grid(row=2, column=1, padx=10, pady=10)
    Button(frame2, text="Assign Homework", command=ah, font=("David", 10, "bold")) \
        .grid(row=0, column=0, padx=5, pady=5)
    Button(frame2, text="View Assigned Homework", command=vah, font=("David", 10, "bold")) \
        .grid(row=0, column=1, padx=5, pady=5)


def ah():
    """Function To Show Submenu Of Assign Homework"""
    global frame2
    try:
        frame2.destroy()
    except:
        pass
    root.geometry("950x400")
    frame2 = LabelFrame(root, bg="#414F4B", text="Assign Homework", padx=10, pady=10, font=("Verdana", 10, "bold"))
    frame2.grid(row=2, column=1, padx=10, pady=10)
    Button(frame2, text="Physics", command=p_a_h, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=0, padx=5, pady=5)
    Button(frame2, text="Chemistry", command=c_a_h, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=1, padx=5, pady=5)
    Button(frame2, text="Maths", command=m_a_h, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=2, padx=5, pady=5)


def p_a_h():
    pass


def c_a_h():
    pass


def m_a_h():
    pass


def vah():
    """Function To Show Submenu Of View Assigned Homework"""
    global frame2
    try:
        frame2.destroy()
    except:
        pass
    root.geometry("950x400")
    frame2 = LabelFrame(root, bg="#414F4B", text="View Assigned Homework", padx=10, pady=10, font=("Verdana", 10, "bold"))
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


def view_student_profile():
    """Function To Show Submenu Of View Homework"""
    global frame2
    try:
        frame2.destroy()
    except:
        pass
    root.geometry("950x400")
    frame2 = LabelFrame(root, bg="#414F4B", text="Student Profile", padx=10, pady=10, font=("Verdana", 10, "bold"))

    Button(frame2, text="Select Student", command=ss, font=("David", 10, "bold")) \
        .grid(row=0, column=0, padx=5, pady=5)
    frame2.grid(row=2, column=1, padx=10, pady=10)
    Button(frame2, text="Total Homeworks", command=total_hw, font=("David", 10, "bold")) \
        .grid(row=0, column=1, padx=5, pady=5)
    Button(frame2, text="Pending Homework", command=pending_hw, font=("David", 10, "bold")) \
        .grid(row=0, column=2, padx=5, pady=5)


def total_hw():
    """Function To Show Submenu Of Total Homeworks"""
    global frame2
    try:
        frame2.destroy()
    except:
        pass
    root.geometry("950x400")
    frame2 = LabelFrame(root, bg="#414F4B", text="Total Homeworks", padx=10, pady=10,
                        font=("Verdana", 10, "bold"))
    frame2.grid(row=2, column=1, padx=10, pady=10)
    Button(frame2, text="Physics", command=p_t_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=0, padx=5, pady=5)
    Button(frame2, text="Chemistry", command=c_t_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=1, padx=5, pady=5)
    Button(frame2, text="Maths", command=m_t_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=2, padx=5, pady=5)


def pending_hw():
    """Function To Show Submenu Of Total Homeworks"""
    global frame2
    try:
        frame2.destroy()
    except:
        pass
    root.geometry("950x400")
    frame2 = LabelFrame(root, bg="#414F4B", text="Pending Homeworks", padx=10, pady=10,
                        font=("Verdana", 10, "bold"))
    frame2.grid(row=2, column=1, padx=10, pady=10)
    Button(frame2, text="Physics", command=p_p_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=0, padx=5, pady=5)
    Button(frame2, text="Chemistry", command=c_p_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=1, padx=5, pady=5)
    Button(frame2, text="Maths", command=m_p_hw, width=25, font=("David", 10, "bold")) \
        .grid(row=0, column=2, padx=5, pady=5)


def p_t_hw():
    """Function to show submenu of Physics Total hw"""
    pass


def c_t_hw():
    """Function to show submenu of chemistry total hw"""
    pass


def m_t_hw():
    """Function to show submenu of maths total hw"""
    pass


def p_p_hw():
    """Function to show submenu of Physics pending hw"""
    pass


def c_p_hw():
    """Function to show submenu of chemistry pending hw"""
    pass


def m_p_hw():
    """Function to show submenu of maths pending hw"""
    pass


def ss():
    """Function to select student"""
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

lbl1 = Label(root, text="Teacher's Portal", font=("Lucida Bright", 20, "bold", "underline"))\
    .grid(row=0, column=1, columnspan=2, pady=(10, 0))

frame = LabelFrame(root, bg="#414F64", text="MAIN MENU", padx=5, pady=20, font=("Verdana", 10, "bold"))
frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

btn1 = Button(frame, text="Student Profile", command=view_student_profile, width=25, state=NORMAL,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=0, padx=8, pady=15)

btn2 = Button(frame, text="Homework", command=homework, width=25, state=NORMAL,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=1, padx=8, pady=15)

btn3 = Button(frame, text="Student List", command=student_list, width=25, state=NORMAL,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=2, padx=8, pady=15)

btn4 = Button(frame, text="Teachers List", command=teachers_list, width=25, state=NORMAL,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=3, padx=8, pady=15)

btn5 = Button(frame, text="Exit The Program", command=close, width=25, state=NORMAL,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=1, column=0, padx=8, pady=15)


root.mainloop()

connection.close()
