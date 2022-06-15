from tkinter import Toplevel, LabelFrame, Label, Entry, Button


def admin_login():
    import sys
    import mysql.connector as ms
    import tkinter as tk
    from tkinter import ttk, messagebox
    import database_code

    database_name = 's_m_s'
    database_code.database_creation(database_name)

    connection = ms.connect(host="localhost", user="root", passwd="Shreyas25%")
    cur = connection.cursor()

    def open_d():
        """Function To Open Connection To Database"""
        try:
            cur.execute("use {}".format(database_name))  # Name of my database is 'database_name'
        except Exception as e:
            response = messagebox.showerror("ERROR!", e)

    def homework():
        """Function To Show Submenu Of View Homework"""
        global frame2
        try:
            frame2.destroy()
        except:
            pass
        root.geometry("700x350")
        frame2 = tk.LabelFrame(root, bg="#414F4B", text="Homework", padx=10, pady=10, font=("Verdana", 10, "bold"))
        frame2.grid(row=2, column=1, padx=10, pady=10)
        tk.Button(frame2, text="Assign Homework", width=25, command=ah, font=("David", 10, "bold")) \
            .grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame2, text="View Assigned Homework", width=25, command=vah, font=("David", 10, "bold")) \
            .grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame2, text="View Submitted Homework", width=25, command=vsh, font=("David", 10, "bold")) \
            .grid(row=0, column=2, padx=5, pady=5)

    def ah():
        """Function To Show Submenu Of Assign Homework"""
        global frame2
        try:
            frame2.destroy()
        except:
            pass
        root.geometry("700x350")
        frame2 = tk.LabelFrame(root, bg="#414F4B", text="Assign Homework", padx=10, pady=10,
                               font=("Verdana", 10, "bold"))
        frame2.grid(row=2, column=1, padx=10, pady=10)
        tk.Button(frame2, text="Physics", command=p_a_h, width=25, font=("David", 10, "bold")) \
            .grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame2, text="Chemistry", command=c_a_h, width=25, font=("David", 10, "bold")) \
            .grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame2, text="Maths", command=m_a_h, width=25, font=("David", 10, "bold")) \
            .grid(row=0, column=2, padx=5, pady=5)

    def p_a_h():
        """Function To Show Submenu Of Physics Assign Homework"""
        Adder = Toplevel()
        Adder.title("Assign Homework")
        Adder.geometry("595x225")
        frame_a = LabelFrame(Adder, text="Enter Details", padx="20", pady=20, font=("Verdana", 10, "bold"))
        frame_a.grid(row=0, column=0, padx=10, pady=10)

        def submit():
            """Function That Takes Value From Screen And Adds It To Database"""
            # Retrieve Data Entered By User
            b0 = hw_id.get()
            b1 = hw_name.get().upper()
            if len(b0) == 0:
                response = messagebox.showerror("WARNING!", "Homework id Can't Be Left Empty")
                Adder.lift()
                return ()
            b2 = classes_assigned.get()
            if len(b1) == 0:
                response = messagebox.showerror("WARNING!", "Homework Name Can't Be Left Empty")
                Adder.lift()
                return ()
            query = "Insert into assignment values('{}', '{}', {})"\
            .format(b0, b1, b2)
            cur.execute(query)
            connection.commit()
            Adder.destroy()
            response = messagebox.showinfo("SUCCESSFUL!", "Record Added Successfully")

        hw_id_label = Label(frame_a, text="Homework id", font=("Comic Sans MS", 10))
        hw_id_label.grid(row=0, column=0,)
        hw_name_label = Label(frame_a, text="Homework Name", font=("Comic Sans MS", 10))
        hw_name_label.grid(row=1, column=0)
        classes_assigned_label = Label(frame_a, text="Class Assigned", font=("Comic Sans MS", 10))
        classes_assigned_label.grid(row=2, column=0)

        hw_id = Entry(frame_a, width=15, font=("Century", 10))
        hw_id.grid(row=0, column=1, pady=(10, 0), padx=5)
        hw_name = Entry(frame_a, width=15, font=("Century", 10))
        hw_name.grid(row=1, column=1, padx=5)
        classes_assigned = Entry(frame_a, width=15, font=("Century", 10))
        classes_assigned.grid(row=2, column=1, padx=5)

        # Insert Homework id Automatically
        cur.execute("select hw_id from users")
        rows = cur.fetchall()
        if len(rows) == 0:
            hw_id.insert(0, 1)
        else:
            hw_id.insert(0, int(rows[-1][0]) + 1)
        hw_id.config(state="disabled")

        submit_btn = Button(frame_a, text="Submit", command=submit, width=10, font=("Times New Roman", 12, "bold"))
        submit_btn.grid(row=4, column=3, sticky=E)


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
        root.geometry("700x350")
        frame2 = tk.LabelFrame(root, bg="#414F4B", text="View Assigned Homework", padx=10, pady=10,
                               font=("Verdana", 10, "bold"))
        frame2.grid(row=2, column=1, padx=10, pady=10)
        tk.Button(frame2, text="Physics", command=p_a_hw, width=25, font=("David", 10, "bold")) \
            .grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame2, text="Chemistry", command=c_a_hw, width=25, font=("David", 10, "bold")) \
            .grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame2, text="Maths", command=m_a_hw, width=25, font=("David", 10, "bold")) \
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
        root.geometry("800x400")
        frame2 = tk.LabelFrame(root, bg="#414F4B", text="View Submitted Homework", padx=10, pady=10,
                               font=("Verdana", 10, "bold"))
        frame2.grid(row=2, column=1, padx=10, pady=10)
        tk.Button(frame2, text="Physics", command=p_s_hw, width=25, font=("David", 10, "bold")) \
            .grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame2, text="Chemistry", command=c_s_hw, width=25, font=("David", 10, "bold")) \
            .grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame2, text="Maths", command=m_s_hw, width=25, font=("David", 10, "bold")) \
            .grid(row=0, column=2, padx=5, pady=5)

    def p_s_hw():
        pass

    def c_s_hw():
        pass

    def m_s_hw():
        pass

    def student_list():
        global frame2
        try:
            frame2.destroy()
        except:
            pass

    def teachers_list():
        global frame2
        try:
            frame2.destroy()
        except:
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
        root.geometry("500x350")
        frame2 = tk.LabelFrame(root, bg="#414F4B", text="CONFIRM EXIT", padx=10, pady=10, font=("Verdana", 10, "bold"))
        frame2.grid(row=2, column=1, padx=10, pady=10)
        tk.Button(frame2, text="No, Take Me Back", width=25, font=("David", 10, "bold"), command=noquit) \
            .grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame2, text="Yes, I Want To Quit", width=25, command=quitprog, font=("David", 10, "bold")) \
            .grid(row=0, column=1, padx=5, pady=5)

    root = tk.Tk()  # Tk is used to create a main window
    root.title("H.C.E.T Syndicate School Portal")
    root.geometry("500x300")
    root.eval('tk::PlaceWindow . center')  # Positions the new screen window to open up in the center of the screen
    root['background'] = "#5E889F"  # HexDecimal colour code

    lbl1 = tk.Label(root, text="Admin", font=("Lucida Bright", 20, "bold", "underline"))\
        .grid(row=0, column=1, columnspan=2, pady=(10, 0))

    frame = tk.LabelFrame(root, bg="#414F64", text="MAIN MENU", padx=5, pady=20, font=("Verdana", 10, "bold"))
    frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    tk.Button(frame, text="Homework", command=homework, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=1, column=2, padx=8, pady=15)

    tk.Button(frame, text="Student List", command=student_list, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=2, padx=8, pady=15)

    tk.Button(frame, text="Teachers List", command=teachers_list, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=3, padx=8, pady=15)

    tk.Button(frame, text="Exit The Program", command=close, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=1, column=3, padx=8, pady=15)

    root.mainloop()
    connection.close()
