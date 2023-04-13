from tkinter import *
import tkinter
import sqlite3

root = tkinter.Tk()
root.title('Employee Management System')
root.geometry('450x500')

connection = sqlite3.connect('ems.db')
cursor = connection.cursor()

connection.execute('''CREATE TABLE IF NOT EXISTS employees
             (first_name TEXT,
              last_name TEXT,
              date_of_employment TEXT,
              salary REAL);''')

def submit_employee():
    connection = sqlite3.connect('ems.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO employees VALUES (:f_name, :l_name, :doe, :salary)',
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'doe': doe.get(),
            'salary': salary.get()
        }
    )

    connection.commit()
    connection.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    doe.delete(0, END)
    salary.delete(0, END)

def emp_query():
    connection = sqlite3.connect('ems.db')
    cursor = connection.cursor()

    cursor.execute('SELECT *, oid FROM employees')
    emp_records = cursor.fetchall()
    print(emp_records)

    records = ''
    for emp in emp_records:
        records += str(emp[4]) + ' ' + str(emp[0]) + ' ' + str(emp[1]) + ' ' + str(emp[2]) + ' ' + str(emp[3]) + '\n'
    emp_label = Label(root, text=records)
    emp_label.grid(row=12, column=0, pady=(10, 0), columnspan=2)

    connection.commit()
    connection.close()

def update_emp():
    edit_window = tkinter.Tk()
    edit_window.title('Update Employee Record')
    edit_window.geometry('400x300')
    connection = sqlite3.connect('ems.db')
    cursor = connection.cursor()

     #Textboxes
    f_name_edit_window = Entry(edit_window, width=30)
    f_name_edit_window.grid(row=0, column=1, padx=15, pady=(20, 0))

    l_name_edit_window = Entry(edit_window, width=30)
    l_name_edit_window.grid(row=1, column=1, padx=15)

    doe_edit_window = Entry(edit_window, width=30)
    doe_edit_window.grid(row=2, column=1, padx=15)

    salary_edit_window = Entry(edit_window, width=30)
    salary_edit_window.grid(row=3, column=1, padx=15)

    emp_id = delete_box.get()

    connection.execute('''UPDATE employees SET
            first_name = :first,
            last_name = :last,
            date_of_employment = :doe,
            salary = :salary
            WHERE oid = :oid''',
            {
            'first': f_name_edit_window.get(),
            'last': l_name_edit_window.get(),
            'doe': doe_edit_window.get(),
            'salary': salary_edit_window.get(),
            'oid': emp_id
            })

    connection.commit()
    connection.close()
    edit_window.destroy()


def edit_emp():
    edit_window = tkinter.Tk()
    edit_window.title('Update Employee Record')
    edit_window.geometry('400x300')
    connection = sqlite3.connect('ems.db')
    cursor = connection.cursor()

    emp_id = emp_id_box.get()

    #Textboxes
    f_name_edit_window = Entry(edit_window, width=30)
    f_name_edit_window.grid(row=0, column=1, padx=15, pady=(20, 0))

    l_name_edit_window = Entry(edit_window, width=30)
    l_name_edit_window.grid(row=1, column=1, padx=15)

    doe_edit_window = Entry(edit_window, width=30)
    doe_edit_window.grid(row=2, column=1, padx=15)

    salary_edit_window = Entry(edit_window, width=30)
    salary_edit_window.grid(row=3, column=1, padx=15)

    cursor.execute('SELECT * FROM employees WHERE oid =' + emp_id)
    emp_records = cursor.fetchall()
    print(emp_records)

    connection.execute('''UPDATE employees SET
            first_name = :first,
            last_name = :last,
            date_of_employment = :doe,
            salary = :salary
            WHERE oid = :oid''',
            {
            'first': f_name_edit_window.get(),
            'last': l_name_edit_window.get(),
            'doe': doe_edit_window.get(),
            'salary': salary_edit_window.get(),
            'oid': emp_id
            })

    #Textboxes
    f_name_edit_window = Entry(edit_window, width=30)
    f_name_edit_window.grid(row=0, column=1, padx=15, pady=(20, 0))

    l_name_edit_window = Entry(edit_window, width=30)
    l_name_edit_window.grid(row=1, column=1, padx=15)

    doe_edit_window = Entry(edit_window, width=30)
    doe_edit_window.grid(row=2, column=1, padx=15)

    salary_edit_window = Entry(edit_window, width=30)
    salary_edit_window.grid(row=3, column=1, padx=15)

    #Textbox Labels
    f_name_label_edit_window = Label(edit_window, text='First Name')
    f_name_label_edit_window.grid(row=0, column=0, pady=(10, 0))

    l_name_label_edit_window = Label(edit_window, text='Last Name')
    l_name_label_edit_window.grid(row=1, column=0)

    doe_label_edit_window = Label(edit_window, text='Date of Employment')
    doe_label_edit_window.grid(row=2, column=0)

    salary_label_edit_window = Label(edit_window, text='Salary')
    salary_label_edit_window.grid(row=3, column=0)

    #Buttons
    submit_button = Button(edit_window, text='Submit Edit', command=submit_employee)
    submit_button.grid(row=4, column=0, columnspan=3, padx=10, pady=(30, 0), ipadx=62.5)

    for emp in emp_records:
        f_name_edit_window.insert(0, emp[0])
        l_name_edit_window.insert(0, emp[1])
        doe_edit_window.insert(0, emp[2])
        salary_edit_window.insert(0, emp[3])

    connection.commit()
    connection.close()

# DELETE EMPLOYEE
def delete_emp():
    connection = sqlite3.connect('ems.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM employees WHERE oid=' + delete_box.get())
    emp_records = cursor.fetchall()

    connection.commit()
    connection.close()


#Textboxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=15, pady=(20, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=15)

doe = Entry(root, width=30)
doe.grid(row=2, column=1, padx=15)

salary = Entry(root, width=30)
salary.grid(row=3, column=1, padx=15)

emp_id_box = Entry(root, width=30)
emp_id_box.grid(row=7, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=10, column=1)

#Textbox Labels
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)

doe_label = Label(root, text='Date of Employment')
doe_label.grid(row=2, column=0)

salary_label = Label(root, text='Salary')
salary_label.grid(row=3, column=0)

emp_id__label = Label(root, text='Edit Employee ID')
emp_id__label.grid(row=7, column=0)

delete_box_label = Label(root, text='Remove Employee ID')
delete_box_label.grid(row=10, column=0)

#Buttons
submit_button = Button(root, text='Add Employee to Database', command=submit_employee)
submit_button.grid(row=4, column=0, columnspan=3, padx=10, pady=(30, 0), ipadx=62.5)

query_button = Button(root, text='Employee Records', command=emp_query)
query_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10, ipadx=90)

edit_button = Button(root, text='Edit Employee', command=edit_emp)
edit_button.grid(row=9, column=0, columnspan=3, padx=10, pady=10, ipadx=90)

delete_button = Button(root, text='Remove Employee', command=delete_emp)
delete_button.grid(row=11, column=0, columnspan=3, padx=10, pady=10, ipadx=90)

connection.commit()
connection.close()

root.mainloop()
