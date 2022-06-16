import os
from tkinter import Toplevel, LabelFrame, Label, Entry, Button, E


def admin_login():
    import sys
    import mysql.connector as ms
    import tkinter as tk
    from tkinter import ttk, messagebox
    import database_code
    from datetime import datetime

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

    def homework():
        """Function To Show Submenu Of View Homework"""
        global frame2
        try:
            frame2.destroy()
        except:
            pass
        root.geometry("700x400")
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
        root.geometry("700x400")
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
        asgnhw('P')

    def c_a_h():
        asgnhw('C')

    def m_a_h():
        asgnhw('M')

    def asgnhw(id):
        """Function To Show Submenu Of Physics Assign Homework"""
        Adder = tk.Toplevel()
        Adder.title("Assign Homework")
        Adder.geometry("595x225")
        frame_a = tk.LabelFrame(Adder, text="Enter Details", padx="20", pady=20, font=("Verdana", 10, "bold"))
        frame_a.grid(row=0, column=0, padx=10, pady=10)
        open()

        def submit():
            """Function That Takes Value From Screen And Adds It To Database"""
            # Retrieve Data Entered By User
            b0 = hw_id.get().upper()
            b1 = hw_name.get().upper()
            if len(b0) == 0:
                response = messagebox.showerror("WARNING!", "Subject Can't Be Left Empty")
                Adder.lift()
                return ()
            b2 = classes_assigned.get().lower()
            if len(b1) == 0:
                response = messagebox.showerror("WARNING!", "Homework Name Can't Be Left Empty")
                Adder.lift()
                return ()
            if len(b2) == 0:
                response = messagebox.showerror("WARNING!", "Class Assigned Can't Be Left Empty")
                Adder.lift()
                return ()
            query = "Insert into assignment values('{}', '{}', '{}')".format(str(b0), b1, b2)
            cur.execute(query)
            connection.commit()
            Adder.destroy()
            response = messagebox.showinfo("SUCCESSFUL!", "Record Added Successfully")

        hw_id_label = tk.Label(frame_a, text="Homework id", font=("Comic Sans MS", 10))
        hw_id_label.grid(row=0, column=0, )
        hw_name_label = tk.Label(frame_a, text="Homework Name", font=("Comic Sans MS", 10))
        hw_name_label.grid(row=1, column=0)
        classes_assigned_label = tk.Label(frame_a, text="Class Assigned", font=("Comic Sans MS", 10))
        classes_assigned_label.grid(row=2, column=0)

        hw_id = tk.Entry(frame_a, width=15, font=("Century", 10))
        hw_id.grid(row=0, column=1, pady=(10, 0), padx=5)
        hw_name = tk.Entry(frame_a, width=15, font=("Century", 10))
        hw_name.grid(row=1, column=1, padx=5)
        classes_assigned = tk.Entry(frame_a, width=15, font=("Century", 10))
        classes_assigned.grid(row=2, column=1, padx=5)

        # Insert Branch Number Automatically
        cur.execute("select hw_id from assignment where hw_id like '{}'".format(id + '%'))
        rows = cur.fetchall()
        if len(rows) == 0:
            hw_id.insert(0, id + '1')
        else:
            hw_id.insert(0, id + str(int(rows[-1][0][1:]) + 1))
        hw_id.config(state="disabled")

        submit_btn = tk.Button(frame_a, text="Submit", command=submit, width=10, font=("Times New Roman", 12, "bold"))
        submit_btn.grid(row=4, column=3, sticky=tk.E)

    def vah():
        """Function To Show Submenu Of View Assigned Homework"""
        global frame2
        try:
            frame2.destroy()
        except:
            pass
        root.geometry("700x400")
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
        open()
        Display = tk.Toplevel()
        Display.title("All Records")
        frame_d = tk.LabelFrame(Display)
        frame_d.grid(row=0, column=0, padx=10, pady=10)
        cur.execute("select * from student")
        rows = cur.fetchall()
        for x in rows:
            print(x)
        if len(rows) == 0:
            Display.destroy()
            response = messagebox.showerror("WARNING", "No Records Of Student Added Yet")
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

        col = ["Admission No", "Name", "Gender", "Class-Section", "Father's Name", "Mother's Name", "Mobile",
               "Email-ID",
               "Date Of Birth", "Aadhar Number", "Address_line_1", "Address_line_2"]
        for i in range(len(col)):
            tk.Label(frame_d_l, text=col[i], font=("Ariel Bold", 12, "bold", "underline")) \
                .grid(row=0, column=i, pady=10, padx=5)
        j = 1
        for r in rows:
            for i in range(len(col)):
                tk.Label(frame_d_l, text=r[i], font=("Times New Roman", 12, "italic")) \
                    .grid(row=j, column=i, pady=10, padx=5)
            j += 1

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

    def add_students():
        Adder = tk.Toplevel()
        Adder.title("Add Student")
        Adder.geometry("620x340")
        frame_a = tk.LabelFrame(Adder, text="Enter Details", padx="20", pady=20, font=("Verdana", 10, "bold"))
        frame_a.grid(row=0, column=0, padx=10, pady=10)
        open()

        def submit():
            """Function That Takes Value From Screen And Adds It To Database"""
            # Retrieve Data Entered By User
            a0 = admn_no.get().upper()
            if len(a0) == 0:
                response = messagebox.showerror("WARNING!", "Admission Number Can't Be Left Empty")
                Adder.lift()
                return ()
            a1 = name.get().upper()
            if len(a1) == 0:
                response = messagebox.showerror("WARNING!", "Name Can't Be Left Empty")
                Adder.lift()
                return ()
            a2 = gender.get().upper()
            if len(a2) == 0:
                response = messagebox.showerror("WARNING!", "Gender Can't Be Left Empty")
                Adder.lift()
                return ()
            a3 = class_section.get().upper()
            if len(a3) == 0:
                response = messagebox.showerror("WARNING!", "Class & Section Can't Be Left Empty")
                Adder.lift()
                return ()
            a4 = f_name.get().upper()
            if len(a4) == 0:
                response = messagebox.showerror("WARNING!", "Father's Name Can't Be Left Empty")
                Adder.lift()
                return ()
            a5 = m_name.get().upper()
            if len(a5) == 0:
                response = messagebox.showerror("WARNING!", "Mother's Name can't be left Empty")
                Adder.lift()
                return ()
            a6 = mobile.get().upper()
            if len(a6) != 10 or len(a6) == 0:
                response = messagebox.showerror("WARNING!", "Please enter a valid 10-digit mobile number ")
                Adder.lift()
                return ()
            a7 = email_id.get().upper()
            if len(a7) == 0:
                response = messagebox.showerror("WARNING!", "Email ID Can't Be Left Empty")
                Adder.lift()
                return ()
            a8 = str(d_o_b.get()).split('-')[:: -1]
            if len(a8[0]) != 4 or len(a8[1]) != 2 or len(a8[2]) != 2:
                response = messagebox.showerror("WARNING!", "Please Enter Date In dd-mm-yyyy Format")
                Adder.lift()
                return ()
            a8_final = datetime(int(a8[0]), int(a8[1]), int(a8[2]))
            a9 = aadhar.get().upper()
            if len(a9) == 0 or len(a9) != 12:
                response = messagebox.showerror("WARNING", "Please Enter a Valid 12-digit Aadhar Number")
                Adder.lift()
                return ()
            a10 = address_line_1.get().upper()
            a11 = address_line_2.get().upper()

            query = "Insert into student values({}, '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', {}, '{}', '{}')" \
                .format(a0, a1, a2, a3, a4, a5, a6, a7, a8_final, a9, a10, a11)
            cur.execute(query)
            connection.commit()
            Adder.destroy()
            response = messagebox.showinfo("SUCCESSFUL!", "Student Added Successfully")

        # Creating Text Box Labels
        admn_no_label = tk.Label(frame_a, text="Admission No", font=("Comic Sans MS", 10))
        admn_no_label.grid(row=0, column=0, pady=(10, 0))
        name_label = tk.Label(frame_a, text="Enter Name", font=("Comic Sans MS", 10))
        name_label.grid(row=1, column=0)
        gender_label = tk.Label(frame_a, text="Gender(M/F)", font=("Comic Sans MS", 10))
        gender_label.grid(row=2, column=0)
        class_section_label = tk.Label(frame_a, text="Enter Class & Section", font=("Comic Sans MS", 10))
        class_section_label.grid(row=3, column=0)
        f_name_label = tk.Label(frame_a, text="Enter Father's Name", font=("Comic Sans MS", 10))
        f_name_label.grid(row=4, column=0, pady=(10, 0))
        m_name_label = tk.Label(frame_a, text="Enter Mother's Name", font=("Comic Sans MS", 10))
        m_name_label.grid(row=5, column=0)
        mobile_label = tk.Label(frame_a, text="Enter Mobile Number", font=("Comic Sans MS", 10))
        mobile_label.grid(row=0, column=2)
        email_id_label = tk.Label(frame_a, text="Enter Email id", font=("Comic Sans MS", 10))
        email_id_label.grid(row=1, column=2)
        d_o_b_label = tk.Label(frame_a, text="Enter Date Of Birth", font=("Comic Sans MS", 10))
        d_o_b_label.grid(row=2, column=2, pady=(10, 0))
        aadhar_label = tk.Label(frame_a, text="Enter Aadhar Number", font=("Comic Sans MS", 10))
        aadhar_label.grid(row=3, column=2)
        address_line_1_label = tk.Label(frame_a, text="Enter Address Line 1", font=("Comic Sans MS", 10))
        address_line_1_label.grid(row=4, column=2)
        address_line_2_label = tk.Label(frame_a, text="Enter Address Line 2", font=("Comic Sans MS", 10))
        address_line_2_label.grid(row=5, column=2)

        # Creating Drop-Down Boxes
        clicked = tk.StringVar()
        per_click = clicked.get()
        gender = ttk.Combobox(frame_a, width=12, textvariable=per_click, state='readonly', font=("Century", 10))
        gender['values'] = ("Male", "Female")
        gender.current(0)
        gender.grid(row=2, column=1, padx=5)

        # Create Text Boxes
        admn_no = tk.Entry(frame_a, width=15, font=("Century", 10))
        admn_no.grid(row=0, column=1, pady=(10, 0), padx=5)
        name = tk.Entry(frame_a, width=15, font=("Century", 10))
        name.grid(row=1, column=1, padx=5)
        class_section = tk.Entry(frame_a, width=15, font=("Century", 10))
        class_section.grid(row=3, column=1, padx=5)
        f_name = tk.Entry(frame_a, width=15, font=("Century", 10))
        f_name.grid(row=4, column=1, padx=5)
        m_name = tk.Entry(frame_a, width=15, font=("Century", 10))
        m_name.grid(row=5, column=1, padx=5)
        mobile = tk.Entry(frame_a, width=15, font=("Century", 10))
        mobile.grid(row=0, column=3, padx=5)
        email_id = tk.Entry(frame_a, width=15, font=("Century", 10))
        email_id.grid(row=1, column=3, padx=5)
        d_o_b = tk.Entry(frame_a, width=15, font=("Century", 10))
        d_o_b.grid(row=2, column=3, padx=5)
        aadhar = tk.Entry(frame_a, width=15, font=("Century", 10))
        aadhar.grid(row=3, column=3, padx=5)
        address_line_1 = tk.Entry(frame_a, width=15, font=("Century", 10))
        address_line_1.grid(row=4, column=3, padx=5)
        address_line_2 = tk.Entry(frame_a, width=15, font=("Century", 10))
        address_line_2.grid(row=5, column=3, padx=5)

        cur.execute("select admn_no from student")
        rows = cur.fetchall()
        if len(rows) == 0:
            admn_no.insert(0, 1)
        else:
            admn_no.insert(0, int(rows[-1][0]) + 1)
        admn_no.config(state="disabled")

        # Creating Button
        submit_btn = tk.Button(frame_a, text="Submit", command=submit, width=10, font=("Times New Roman", 12, "bold"))
        submit_btn.grid(row=7, column=3, sticky=tk.E, padx=10, pady=10)

    def add_teachers():
        Adder = tk.Toplevel()
        Adder.title("Add a New Teacher")
        Adder.geometry("610x300")
        frame_a = tk.LabelFrame(Adder, text="Enter Details", padx=20, pady=20, font=("Verdana", 10, "bold"))
        frame_a.grid(row=0, column=0, padx=10, pady=10)
        open()

        def add():
            """Function That Takes Value From Screen And Adds It To Database"""
            # Retrieve Data Entered By User
            s0 = staff_id.get().upper()
            if len(s0) == 0:
                response = messagebox.showerror("WARNING!", "Staff Id Can't Be Left Empty")
                Adder.lift()
                return ()
            s1 = name.get().upper()
            if len(s1) == 0:
                response = messagebox.showerror("WARNING!", "Name Can't Be Left Empty")
                Adder.lift()
                return ()
            s2 = phone.get().upper()
            if len(s2) == 0 or len(s2) != 10:
                response = messagebox.showerror("WARNING!", "Enter a Valid 10-digit Phone Number")
                Adder.lift()
                return ()
            s3 = class_teacher.get().upper()
            if len(s3) == 0:
                response = messagebox.showerror("WARNING!", "Class Teacher Can't Be Left Empty")
                Adder.lift()
                return ()
            s4 = subject.get()
            if len(s4) == 0:
                response = messagebox.showerror("WARNING!", "Subject Can't Be Left Empty")
                Adder.lift()
                return ()
            s5 = address.get()
            if len(s5) == 0:
                response = messagebox.showerror("WARNING!", "Please Enter Your Address")
                Adder.lift()
                return ()
            s6 = email_id.get()
            if len(s6) == 0:
                response = messagebox.showerror("WARNING!", "Please Enter Your Email ID")
                Adder.lift()
                return ()
            s7 = classes.get()
            if len(s7) == 0:
                response = messagebox.showerror("WARNING!", "Please Enter Your Address")
                Adder.lift()
                return ()
            s8 = str(d_o_b.get()).split('-')[:: -1]
            if len(s8[0]) != 4 or len(s8[1]) != 2 or len(s8[2]) != 2:
                response = messagebox.showerror("WARNING!", "Please Enter Date In dd-mm-yyyy Format")
                Adder.lift()
                return ()
            s8_final = datetime(int(s8[0]), int(s8[1]), int(s8[2]))
            query = "Insert into staff values({}, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}')" \
                .format(s0, s1, s2, s3, s4, s5, s6, s7, s8_final)
            cur.execute(query)
            connection.commit()
            Adder.destroy()
            response = messagebox.showinfo("SUCCESSFUL!", "Teacher Added Successfully")

            # Creating Text Box Labels

        staff_id_label = tk.Label(frame_a, text="Teacher/Staff ID", font=("Comic Sans MS", 10))
        staff_id_label.grid(row=0, column=0, pady=(10, 0))
        name_label = tk.Label(frame_a, text="Enter Name", font=("Comic Sans MS", 10))
        name_label.grid(row=1, column=0)
        phone_label = tk.Label(frame_a, text="Enter Phone Number", font=("Comic Sans MS", 10))
        phone_label.grid(row=2, column=0)
        class_teacher_label = tk.Label(frame_a, text="Class Teacher", font=("Comic Sans MS", 10))
        class_teacher_label.grid(row=3, column=0)
        subject_label = tk.Label(frame_a, text="Subject Taught", font=("Comic Sans MS", 10))
        subject_label.grid(row=0, column=2, pady=(10, 0))
        address_label = tk.Label(frame_a, text="Enter Address", font=("Comic Sans MS", 10))
        address_label.grid(row=1, column=2)
        email_id_label = tk.Label(frame_a, text="Enter Email ID", font=("Comic Sans MS", 10))
        email_id_label.grid(row=3, column=2)
        classes_label = tk.Label(frame_a, text="No. Of Classes Taught", font=("Comic Sans MS", 10))
        classes_label.grid(row=4, column=0)
        d_o_b_label = tk.Label(frame_a, text="Enter Date Of Birth", font=("Comic Sans MS", 10))
        d_o_b_label.grid(row=2, column=2)

        clicked = tk.StringVar()
        per_click = clicked.get()
        class_teacher = ttk.Combobox(frame_a, width=15, textvariable=per_click, state='readonly', font=("Century", 10))
        class_teacher['values'] = ("Yes", "No")
        class_teacher.current(0)
        class_teacher.grid(row=3, column=1, padx=5)
        clicked2 = tk.StringVar()
        per_click2 = clicked2.get()
        subject = ttk.Combobox(frame_a, width=15, textvariable=per_click2, state='readonly', font=("Century", 10))
        subject['values'] = ("Physics", "Chemistry", "Maths")
        subject.current(0)
        subject.grid(row=0, column=3, padx=10)

        staff_id = tk.Entry(frame_a, width=18, font=("Century", 10))
        staff_id.grid(row=0, column=1, pady=(10, 0), padx=5)
        name = tk.Entry(frame_a, width=18, font=("Century", 10))
        name.grid(row=1, column=1, padx=5)
        phone = tk.Entry(frame_a, width=18, font=("Century", 10))
        phone.grid(row=2, column=1, padx=5)
        address = tk.Entry(frame_a, width=18, font=("Century", 10))
        address.grid(row=1, column=3, padx=5)
        email_id = tk.Entry(frame_a, width=18, font=("Century", 10))
        email_id.grid(row=3, column=3, padx=5)
        classes = tk.Entry(frame_a, width=18, font=("Century", 10))
        classes.grid(row=4, column=1, padx=5)
        d_o_b = tk.Entry(frame_a, width=18, font=("Century", 10))
        d_o_b.grid(row=2, column=3, padx=5)

        # Insert Branch Number Automatically
        cur.execute("select staff_id from staff")
        rows = cur.fetchall()
        if len(rows) == 0:
            staff_id.insert(0, 1)
        else:
            staff_id.insert(0, int(rows[-1][0]) + 1)
        staff_id.config(state="disabled")

        # Creating Button
        submit_btn = tk.Button(frame_a, text="Submit", command=add, width=10, font=("Times New Roman", 12, "bold"))
        submit_btn.grid(row=6, column=3, sticky=tk.E)

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
        root.geometry("500x400")
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

    lbl1 = tk.Label(root, text="Admin", font=("Lucida Bright", 20, "bold", "underline")) \
        .grid(row=0, column=1, columnspan=2, pady=(10, 0))

    frame = tk.LabelFrame(root, bg="#414F64", text="MAIN MENU", padx=5, pady=20, font=("Verdana", 10, "bold"))
    frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    tk.Button(frame, text="Student List", command=student_list, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=2, padx=8, pady=15)

    tk.Button(frame, text="Teachers List", command=teachers_list, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=0, column=3, padx=8, pady=15)

    tk.Button(frame, text="Add Students", command=add_students, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=1, column=2, padx=8, pady=15)

    tk.Button(frame, text="Add Teachers", command=add_teachers, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=1, column=3, padx=8, pady=15)

    tk.Button(frame, text="Homework", command=homework, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=2, column=2, padx=8, pady=15)

    tk.Button(frame, text="Exit The Program", command=close, width=25,
              font=("Cascadia Code SemiBold", 10, "bold")).grid(row=2, column=3, padx=8, pady=15)

    root.mainloop()
    connection.close()
