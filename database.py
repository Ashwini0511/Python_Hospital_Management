import mysql.connector

def create_table():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='1111',
        database='hospital'
    )

    cursor=conn.cursor()

    cursor.execute('CREATE DATABASE IF NOT EXISTS hospital')
    cursor.execute('USE hospital')

    #patient Table
    cursor.execute('CREATE TABLE IF NOT EXISTS patients('
                   'id INT AUTO_INCREMENT PRIMARY KEY,'
                   'name varchar(35), '
                   'age int,'
                   'gender varchar(10),'
                   'disease varchar(255))')


    #doctor table
    cursor.execute('CREATE TABLE IF NOT EXISTS doctors('
                   'id int AUTO_INCREMENT PRIMARY KEY,'
                   'name varchar(35),'
                   'age int,'
                   'gender varchar(10),'
                   'specialization varchar(255))')

    conn.commit()
    cursor.close()
    conn.close()

#add info about patients in table

def add_patients_to_db(name,age,gender,disease):
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='1111',
        database='hospital'
    )

    cursor=conn.cursor()
    cursor.execute('INSERT INTO patients(name,age,gender,disease) VALUES(%s,%s,%s,%s)', (name,age,gender,disease))
    conn.commit()
    cursor.close()
    conn.close()



def get_all_patients():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='1111',
        database='hospital'
    )
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM patients')
    patients =cursor.fetchall()
    cursor.close()
    conn.close()
    return patients


#inser info about doctors in table
def add_doctors_to_db(name,age,gender,specialization):

    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='1111',
        database='hospital'
    )

    cursor=conn.cursor()
    cursor.execute('INSERT INTO doctors(name,age,gender,specialization) VALUES(%s,%s,%s,%s)',(name,age,gender,specialization))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_doctors():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='1111',
        database='hospital'
    )

    cursor=conn.cursor()
    cursor.execute('SELECT * FROM doctors')
    doctors=cursor.fetchall()
    cursor.close()
    conn.close()
    return doctors