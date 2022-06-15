import mysql.connector as ms
# import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import database_code
import admin
import student

database_name = 's_m_s'
database_code.database_creation(database_name)

connection = ms.connect(host="localhost", user="root", passwd="Shreyas25%")
cur = connection.cursor()


def open_d():
    """Function To Open Connection To Database"""
    try:
        cur.execute("use {}".format(database_name))  # Name of my database is 'database_name'
    except Exception as exc:
        response = messagebox.showerror("ERROR!", exc)


def main_login():
    def login():
        """Function to log in"""
        lt = login_type.get()
        root1.destroy()
        open_d()
        root = Tk()  # Tk is used to create a main window
        root.title("H.C.E.T Syndicate School Portal")
        root.geometry("400x250")
        root['background'] = "#5E889F"  # HexDecimal colour code

        def next():
            u1 = u_id.get()
            u2 = pswrd.get()
            cur.execute("select * from users")
            result = cur.fetchall()
            flag = False
            for ele in result:
                if str(ele[0]) == u1 and ele[1] == u2:
                    root.destroy()
                    response = messagebox.showinfo("SUCCESSFUL!", "Logged In Successfully")
                    if lt == "Admin":
                        admin.admin_login()
                    else:
                        student.student_login()
                    flag = True
            if not flag:
                response = messagebox.showerror("ERROR!", "Username or Password is Incorrect")

        user_id_label = Label(root, text="User Name", font=("Comic Sans MS", 15))
        user_id_label.grid(row=0, column=0, pady=(20, 0))
        password_label = Label(root, text="Enter Your Password", font=("Comic Sans MS", 15))
        password_label.grid(row=2, column=0, padx=10, pady=10)

        Button(root, text="Next", command=next, width=10, font=("Times New Roman", 17, "bold")) \
            .grid(row=8, column=1, pady=(10, 5), sticky=E)

        u_id = Entry(root, width=15, font=("Century", 10))
        u_id.grid(row=0, column=1, pady=(10, 0), padx=5)
        pswrd = Entry(root, width=15, font=("Century", 10))
        pswrd.grid(row=2, column=1, padx=5)

    root1 = Tk()  # Tk is used to create a main window
    root1.title("H.C.E.T Syndicate School Portal")
    root1.geometry("300x300")
    root1['background'] = "#5E889F"  # HexDecimal colour code

    lbl1 = Label(root1, text="Student Portal", font=("Lucida Bright", 30, "bold", "underline"))\
        .grid(row=0, column=1, columnspan=2, padx=(3, 0), pady=(10, 0))
    lbl2 = Label(root1, text="Login Page", font=("Lucida Bright", 25, "bold", "underline"))\
        .grid(row=1, column=1, columnspan=2, pady=(10, 0))

    frame = LabelFrame(root1, bg="#414F64", width=25, padx=5, pady=20, font=("Verdana", 10, "bold"))
    frame.grid(row=2, column=0, columnspan=4, padx=10, pady=20)

    login_type_label = Label(frame, text="Login Type", width=10, font=("Comic Sans MS", 10))
    login_type_label.grid(row=0, column=0)

    clicked = StringVar()
    per_click = clicked.get()
    login_type = ttk.Combobox(frame, width=12, textvariable=per_click, state='readonly', font=("Century", 10))
    login_type['values'] = ("Admin", "Student")
    login_type.current(1)
    login_type.grid(row=0, column=1, padx=5)

    btn1 = Button(root1, text="Next", command=login, width=5, state=NORMAL,
                  font=("Cascadia Code SemiBold", 10, "bold")).grid(row=4, column=2, padx=30, pady=3)

    root1.mainloop()


main_login()
connection.close()
