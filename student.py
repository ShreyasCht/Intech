import os


def student_login():
    import sys
    import mysql.connector as ms
    import tkinter as tk
    from tkinter import ttk, messagebox
    import database_code

    database_name = 's_m_s'
    database_code.database_creation(database_name)

    connection = ms.connect(host="localhost", user="root", passwd="Shreyas25%")
    cur = connection.cursor()

    def open():
        """Function To Open Connection To Database"""
        try:
            cur.execute("use {}".format(database_name))  # Name of my database is 'database_name'
        except Exception as e:
            response = messagebox.showerror("ERROR!", e)

    def personal_records():
        """Function To Show Submenu Of Personal Records"""
        global frame2
        try:
            frame2.destroy()
        except:
            pass
        root.geometry("950x400")
        frame2 = tk.LabelFrame(root, bg="#414F4B", text="Personal Record", padx=10, pady=10,
                               font=("Verdana", 10, "bold"))
        frame2.grid(row=2, column=1, padx=20, pady=10)
        tk.Button(frame2, text="View/Update Records", width=25, command=v_u_p_rec, font=("David", 10, "bold")) \
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
        root.geometry("700x400")
        frame2 = tk.LabelFrame(root, bg="#414F4B", text="View Homework", padx=10, pady=10,
                               font=("Verdana", 10, "bold"))
        frame2.grid(row=2, column=1, padx=10, pady=10)
        tk.Button(frame2, text="Physics", command=p_a_hw, width=25, font=("David", 10, "bold")) \
            .grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame2, text="Chemistry", command=c_a_hw, width=25, font=("David", 10, "bold")) \
            .grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame2, text="Maths", command=m_a_hw, width=25, font=("David", 10, "bold")) \
            .grid(row=0, column=2, padx=5, pady=5)

    def p_a_hw():
        view_asgnhw('P')

    def c_a_hw():
        view_asgnhw('C')

    def m_a_hw():
        view_asgnhw('M')

    def view_asgnhw(id):
        open()
        Display = tk.Toplevel()
        Display.title("All Records")
        frame_d = tk.LabelFrame(Display)
        frame_d.grid(row=0, column=0, padx=10, pady=10)
        cur.execute("select * from assignment where hw_id like '{}'".format(id + '%'))
        rows = cur.fetchall()
        if len(rows) == 0:
            Display.destroy()
            response = messagebox.showerror("WARNING", "No Homework Added yet")
            return ()

        # Scroll Bar
        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=600, height=250)

        canvas = tk.Canvas(frame_d)
        frame_d_l = tk.LabelFrame(canvas, bd=0, padx=10, pady=10)
        myscrollbar = tk.Scrollbar(frame_d, orient='vertical', command=canvas.yview)
        myscrollbar2 = tk.Scrollbar(frame_d, orient='horizontal', command=canvas.xview)
        canvas.configure(xscrollcommand=myscrollbar2.set)
        canvas.configure(yscrollcommand=myscrollbar.set)
        myscrollbar.pack(side="right", fill="y")
        myscrollbar2.pack(side="bottom", fill="x")
        canvas.pack(side="left")
        canvas.create_window((0, 0), window=frame_d_l, anchor='nw')
        frame_d_l.bind("<Configure>", myfunction)

        col = ["Homework ID", "Homework", "Classes Assigned"]
        for i in range(len(col)):
            tk.Label(frame_d_l, text=col[i], font=("Ariel Bold", 12, "bold", "underline")) \
                .grid(row=0, column=i, pady=10, padx=5)
        j = 1
        for r in rows:
            for i in range(len(col)):
                tk.Label(frame_d_l, text=r[i], font=("Times New Roman", 12, "italic")) \
                    .grid(row=j, column=i, pady=10, padx=5)
            j += 1

    def submit_homework():
        global frame2
        try:
            frame2.destroy()
        except:
            pass
        os.system("cmd /c notepad")

    def view_submitted_homework():
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
        open()
        Display = tk.Toplevel()
        Display.title("All Records")
        frame_d = tk.LabelFrame(Display)
        frame_d.grid(row=0, column=0, padx=10, pady=10)
        cur.execute("select * from staff")
        rows = cur.fetchall()
        if len(rows) == 0:
            Display.destroy()
            response = messagebox.showerror("WARNING", "No Records Of Teacher Added Yet")
            return ()

        # Scroll Bar
        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=972, height=245)

        canvas = tk.Canvas(frame_d)
        frame_d_l = tk.LabelFrame(canvas, bd=0, padx=10, pady=10)
        myscrollbar = tk.Scrollbar(frame_d, orient='vertical', command=canvas.yview)
        myscrollbar2 = tk.Scrollbar(frame_d, orient='horizontal', command=canvas.xview)
        canvas.configure(xscrollcommand=myscrollbar2.set)
        canvas.configure(yscrollcommand=myscrollbar.set)
        myscrollbar.pack(side="right", fill="y")
        myscrollbar2.pack(side="bottom", fill="x")
        canvas.pack(side="left")
        canvas.create_window((0, 0), window=frame_d_l, anchor='nw')
        frame_d_l.bind("<Configure>", myfunction)

        col = ["Staff ID", "Name", "Phone", "Class-Teacher", " Subject", "Address", "Email-ID",
               "Classes", "Date Of Birth"]
        for i in range(len(col)):
            tk.Label(frame_d_l, text=col[i], font=("Ariel Bold", 12, "bold", "underline")) \
                .grid(row=0, column=i, pady=10, padx=5)
        j = 1
        for r in rows:
            for i in range(len(col)):
                tk.Label(frame_d_l, text=r[i], font=("Times New Roman", 12, "italic")) \
                    .grid(row=j, column=i, pady=10, padx=5)
            j += 1

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
        frame2 = tk.LabelFrame(root, bg="#414F4B", text="CONFIRM EXIT", padx=10, pady=10, font=("Verdana", 10, "bold"))
        frame2.grid(row=2, column=1, padx=10, pady=10)
        tk.Button(frame2, text="No, Take Me Back", width=25, font=("David", 10, "bold"), command=noquit) \
            .grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame2, text="Yes, I Want To Quit", width=25, command=quitprog, font=("David", 10, "bold")) \
            .grid(row=0, column=1, padx=5, pady=5)

    root = tk.Tk()  # Tk is used to create a main window
    root.title("H.C.E.T Syndicate School Portal")
    root.geometry("950x400")
    root.eval('tk::PlaceWindow . center')  # Positions the new screen window to open up in the center of the screen
    root['background'] = "#5E889F"  # HexDecimal colour code

    lbl1 = tk.Label(root, text="Student Portal", font=("Lucida Bright", 20, "bold", "underline"))\
        .grid(row=0, column=1, columnspan=2, pady=(10, 0))

    frame = tk.LabelFrame(root, bg="#414F64", text="MAIN MENU", padx=5, pady=20, font=("Verdana", 10, "bold"))
    frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    tk.Button(frame, text="Personal Records", command=personal_records, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=0, padx=8, pady=15)

    tk.Button(frame, text="View Homeworks", command=view_homework, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=1, padx=8, pady=15)

    tk.Button(frame, text="Submit Homework", command=submit_homework, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=2, padx=8, pady=15)

    tk.Button(frame, text="View Homework Answers", command=view_submitted_homework, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=1, column=1, padx=8, pady=15)

    tk.Button(frame, text="Teachers List", command=teachers_list, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=1, column=0, padx=8, pady=15)

    tk.Button(frame, text="Exit The Program", command=close, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=1, column=2, padx=8, pady=15)

    root.mainloop()
    connection.close()
