import mysql.connector as m


def Database_Creation(database_name='student_management_system'):
    connection = m.connect(host="localhost", user="root", passwd="Shreyas25%")
    cur1 = connection.cursor()

    def view_structure(t):
        """"Function created to show the structure of the table created"""
        try:
            cur1.execute("use {}".format(database_name))
            cur1.execute("desc {}".format(t))
            print("Structure of table {} is".format(t))
            for r in cur1:
                print(r[0].ljust(25), r[1].ljust(25), r[2].ljust(10), r[3])
            print()
        except Exception as e:
            print("ERROR is", e)

    try:
        cur1.execute("create database if not exists {}".format(database_name))
        cur1.execute("use {}".format(database_name))
        cur1.execute("show tables")
        rows = cur1.fetchall()
        table_list = [('staff',), ('student',), ('users',), ('assignment',), ('report card',)]
        if table_list == rows:
            flag = False
        else:
            flag = True
        if flag:
            cur1.execute("use {}".format(database_name))

            cur1.execute("create table staff(\
                         staff_id integer(5) primary key,\
                         name varchar(50) not null,\
                         phone integer(10) not null,\
                         class_teacher varchar(1) not null,\
                         subject varchar(10) not null,\
                         address varchar(80) not null,\
                         email_id varchar(60) not null,\
                         classes varchar(100),\
                         dob date not null)")

            cur1.execute("create table student(\
                         admn_no integer(5) primary key,\
                         name varchar(40) not null,\
                         gender char(1) not null,\
                         class_section char(3) not null,\
                         f_name varchar(40) not null,\
                         m_name varchar(40) not null,\
                         mobile integer(10) not null,\
                         email_id varchar(50) not null,\
                         d_o_b date not null,\
                         aadhar varchar(12) not null,\
                         address_line_1 varchar(80),\
                         address_line_2 varchar(80))")

            cur1.execute("create table users(\
                        admn_no integer(5) primary key,\
                        password varchar(5) not null,\
                        foreign key(admn_no) references student(admn_no))")

            cur1.execute("create table assignment(\
                         hw_id char(5) primary key,\
                         hw_name varchar(30) not null,\
                         classes_assigned varchar(100) not null)")

            cur1.execute("create table report_card(\
                        adm_no integer(5) primary key,\
                        name varchar(40) not null,\
                        class_section char(3) not null,\
                        p_marks int(2) not null,\
                        c_marks int(2) not null,\
                        m_marks int(2) not null,\
                        percentage integer(3) not null)")

        view_structure("staff")
        view_structure("student")
        view_structure("assignment")
        view_structure("report_card")

    except Exception as e:
        print("ERROR is", e)
    connection.close()
