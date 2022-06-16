import mysql.connector as ms


def database_creation(database_name='s_m_s'):
    connection = ms.connect(host="localhost", user="root", passwd="Shreyas25%")
    cur1 = connection.cursor()

    try:
        cur1.execute("create database if not exists {}".format(database_name))
        cur1.execute("use {}".format(database_name))
        cur1.execute("create table if not exists staff(\
                     staff_id integer primary key,\
                     name varchar(50) not null,\
                     phone bigint not null,\
                     class_teacher varchar(3) not null,\
                     subject varchar(10) not null,\
                     address varchar(80) not null,\
                     email_id varchar(60) not null,\
                     classes varchar(100),\
                     dob date not null)")

        cur1.execute("create table if not exists student(\
                     admn_no integer primary key,\
                     name varchar(40) not null,\
                     gender char(6) not null,\
                     class_section char(5) not null,\
                     f_name varchar(40) not null,\
                     m_name varchar(40) not null,\
                     mobile bigint not null,\
                     email_id varchar(50) not null,\
                     d_o_b date not null,\
                     aadhar varchar(12) not null,\
                     address_line_1 varchar(80),\
                     address_line_2 varchar(80))")

        cur1.execute("create table if not exists users(\
                    admn_no integer primary key,\
                    password varchar(10) not null)")

        cur1.execute("insert into users values(0, 'percy')")

        cur1.execute("create table if not exists assignment(\
                     hw_id char(5) primary key,\
                     hw_name varchar(30) not null,\
                     classes_assigned varchar(100) not null)")

        cur1.execute("create table if not exists report_card(\
                    adm_no integer primary key,\
                    name varchar(40) not null,\
                    class_section char(3) not null,\
                    p_marks int(2) not null,\
                    c_marks int(2) not null,\
                    m_marks int(2) not null,\
                    percentage integer(3) not null)")

    except Exception as e:
        print("ERROR is", e)
    connection.close()
