# Import Modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
import sqlite3



# Import Modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
import sqlite3


# Setup Window
root = Tk()
root.title('AnimalAIyes')
root.iconphoto(False, PhotoImage(file='cat.png'))
root.geometry("1200x600")



def primary_color():
    primary_color = colorchooser.askcolor()[1]

    if primary_color:
         my_tree.tag_configure('evenrow', background=primary_color)


def secondary_color():
    secondary_color = colorchooser.askcolor()[1]

    if secondary_color:
         my_tree.tag_configure('oddrow', background=secondary_color)

def highlight_color():
    highlight_color = colorchooser.askcolor()[1]

    if highlight_color:
        style.map('Treeview',
        background=[('selected', highlight_color)])
         

# Add Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Configure Menu
option_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Options", menu=option_menu)

# Drop Down Menu
option_menu.add_command(label="Primary Color", command=primary_color)
option_menu.add_command(label="Secondary Color", command=secondary_color)
option_menu.add_command(label="Highlight Color", command=highlight_color)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=root.quit)





# Setup the Database
# Create a database and make a connection and cursor
conn = sqlite3.connect('CRM77.db')
c = conn.cursor()

# Make tables
c.execute("""CREATE TABLE if not exists students (
          student_num integer,
          name integer, 
          birthday text, 
          email text,
          phone text, 
          station text,
          city text, 
          course text, 
          start text
          )
""")
# Commit Changes and Close connection 



##################################
####    FAKE DATA   ##############
##################################


#Add Fake data to SQLITE Database
# for record in data:
#     c.execute("INSERT INTO students VALUES (:student_num, :name, :birthday, :email, :phone, :station, :city, :course, :start)",
#               {
#               'student_num': record[0],
#               'name': record[1],
#               'birthday': record[2],
#               'email': record[3],
#               'phone': record[4],
#               'station': record[5],
#               'city': record[6],
#               'course': record[7],
#               'start': record[8],
#               }
#               )


# #Commit Changes and Close connection 
# conn.commit()
# conn.close()



#Query Database
def query_database():
     conn = sqlite3.connect('CRM77.db')
     c = conn.cursor()
     
     c.execute("SELECT rowid, * FROM students")
     records = c.fetchall()
    #  print(records)

    # Add data from database to Tree View
     global count
     count = 0



     for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9] ), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9] ), tags=('oddrow',))
        count +=1

     conn.commit()
     conn.close()





# Setup Treeview Style Theme
style = ttk.Style()
style.theme_use('vista')

style.configure('Treeview',
                background='#F54E71',
                foreground='black',
                rowheight=25,
                fieldbackground="#D#D#D#")

style.map('Treeview',
          background=[('selected', "#347083")])


# Setup Treeview Frame and Scrollbar

style.map('Treeview',
          background=[('selected', "#7f65d7")])

#Setup Treeview Frame and Scrollbar
tree_frame = Frame(root)
tree_frame.pack(pady=10)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

tree_scroll.config(command=my_tree.yview)


# Define Columns
my_tree['columns'] = ( "Record ID", "Student ID", "Name",  "Birthday", "Email", "Phone", "Station", "City", "Course", "Start Date")

# Format Columns
my_tree.column("#0", width=0, stretch=NO, )
my_tree.column("Record ID", anchor=CENTER, width=90)
my_tree.column("Student ID", anchor=W, width=100)
my_tree.column("Name", anchor=W, width=120)
my_tree.column("Birthday", anchor=CENTER, width=100)
my_tree.column("Email", anchor=CENTER, width=140)
my_tree.column("Phone", anchor=CENTER, width=120)
my_tree.column("Station", anchor=CENTER, width=120)
my_tree.column("City", anchor=CENTER, width=120)
my_tree.column("Course", anchor=CENTER, width=120)
my_tree.column("Start Date", anchor=CENTER, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Record ID", text="Record #", anchor=CENTER)
my_tree.heading("Student ID", text="Student #", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Birthday", text="Birthday", anchor=CENTER)
my_tree.heading("Email", text="Email", anchor=CENTER)
my_tree.heading("Phone", text="Phone", anchor=CENTER)
my_tree.heading("Station", text="Station", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("Course", text="Course", anchor=CENTER)
my_tree.heading("Start Date", text="Start Date", anchor=CENTER)

# Create Striped Rows
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="#e5e7f2")




# Add data to Tree View
global count
count = 0

    # for record in records:
    #     print(record)

# Loop through data one record at a time
# Get even rows (remainder of modulos is 0)
# Specify the color depening on even or odd rows
# for record in data:
#     if count % 2 == 0:   
#             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],   ), tags=('evenrow',))
#     else:
#             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],   ), tags=('oddrow',))
#     count +=1





# Select Record
# Select Record
def select_record(e):
    # Clear All Records
    id_entry.delete(0, END)
    st_entry.delete(0, END)
    name_entry.delete(0, END)
    birthday_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)
    station_entry.delete(0, END)
    city_entry.delete(0, END)
    course_entry.delete(0, END)
    start_entry.delete(0, END)

    # Pickup a Record and Output to entry boxes
    # The item that is clicked on becomes the focus
    selected = my_tree.focus()
    values = my_tree.item(selected, 'values')

    id_entry.insert(0, values[0])
    st_entry.insert(0, values[1])
    name_entry.insert(0, values[2])
    birthday_entry.insert(0, values[3])
    email_entry.insert(0, values[4])
    phone_entry.insert(0, values[5])
    station_entry.insert(0, values[6])
    city_entry.insert(0, values[7])
    course_entry.insert(0, values[8])
    start_entry.insert(0, values[9])







# Clear Entry Boxes
def clear_entries():
    id_entry.delete(0, END)
    st_entry.delete(0, END)
    name_entry.delete(0, END)
    birthday_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)
    phone_entry.delete(0, END)
    station_entry.delete(0, END)
    city_entry.delete(0, END)
    course_entry.delete(0, END)
    start_entry.delete(0, END)

# Move Row Up
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# Move Row Down
def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# Remove 1 Record
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

# Update Records
def update_record():
    selected = my_tree.focus()
    my_tree.item(selected, text="", values=(id_entry.get(), st_entry.get(), name_entry.get(), birthday_entry.get(), email_entry.get(), phone_entry.get(), station_entry.get(), city_entry.get(), course_entry.get(), start_entry.get(),))

    #Update Database
    conn = sqlite3.connect('CRM77.db')
    c = conn.cursor()

    c.execute(""" UPDATE students SET
              student_num = :student, 
              name = :name, 
              birthday = :birthday, 
              email = :email, 
              phone = :phone, 
              station = :station, 
              city = :city,
              course = :course, 
              start = :start

              WHERE oid = :oid""",

              {
                'student': st_entry.get(),
                'name': name_entry.get(),
                'birthday': birthday_entry.get(),
                'email': email_entry.get(),
                'phone': phone_entry.get(),
                'station': station_entry.get(),
                'city': city_entry.get(),
                'course': course_entry.get(),
                'start': start_entry.get(),
                'oid': id_entry.get(),

})
    
    conn.commit()
    conn.close()

    clear_entries()


# # Add Record to Database 
#  Add Record
def add_record():
      conn = sqlite3.connect('CRM77.db')
      c = conn.cursor()

      c.execute("INSERT INTO students VALUES (:student_num, :name, :birthday, :email, :phone, :station, :city, :course, :start)",

         {
                   
                   'student_num': st_entry.get(),
                   'name': name_entry.get(),
                   'birthday': birthday_entry.get(),
                   'email': email_entry.get(),
                   'phone': phone_entry.get(),
                   'station': station_entry.get(),
                   'city': city_entry.get(),
                   'course': course_entry.get(),
                   'start': start_entry.get(),

               } )

    # Clear Entry Boxes

      conn.commit()
      conn.close()

      clear_entries()

      # Clear Tree View Table and Refresh so that changes are reflected in Treeview
      my_tree.delete(*my_tree.get_children())

      query_database()


# Remove 1 Record
def remove_one():
    # Delete the selected record from the Treeview 
    x = my_tree.selection()[0]
    my_tree.delete(x)

    #Delete record from database 
    conn = sqlite3.connect('CRM77.db')
    c = conn.cursor()

    c.execute("DELETE from students WHERE oid=" + id_entry.get())

    conn.commit()
    conn.close()

    clear_entries()

    messagebox.showinfo("Deleted", "Record was deleted")



# Add Record Entry Boxes
data_frame  = LabelFrame(root, text="Records")
data_frame.pack(fill="x", expand="yes", padx=20)

id_label = Label(data_frame, text="Record #")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=1, padx=10, pady=10)

st_label = Label(data_frame, text="Student #")
st_label.grid(row=0, column=2, padx=10, pady=10)
st_entry = Entry(data_frame)
st_entry.grid(row=0, column=3, padx=10, pady=10)

name_label = Label(data_frame, text="Name")
name_label.grid(row=0, column=4, padx=10, pady=10)
name_entry = Entry(data_frame)
name_entry.grid(row=0, column=5, padx=10, pady=10)

birthday_label = Label(data_frame, text="Birthday")
birthday_label.grid(row=0, column=6, padx=10, pady=10)
birthday_entry = Entry(data_frame)
birthday_entry.grid(row=0, column=7, padx=10, pady=10)

email_label = Label(data_frame, text="Email")
email_label.grid(row=0, column=8, padx=10, pady=10)
email_entry = Entry(data_frame)
email_entry.grid(row=0, column=9, padx=10, pady=10)

phone_label = Label(data_frame, text="Phone")
phone_label.grid(row=1, column=0, padx=10, pady=10)
phone_entry = Entry(data_frame)
phone_entry.grid(row=1, column=1, padx=10, pady=10)

station_label = Label(data_frame, text="Station")
station_label.grid(row=1, column=2, padx=10, pady=10)
station_entry = Entry(data_frame)
station_entry.grid(row=1, column=3, padx=10, pady=10)

city_label = Label(data_frame, text="City")
city_label.grid(row=1, column=4, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=5, padx=10, pady=10)

course_label = Label(data_frame, text="Course")
course_label.grid(row=1, column=6, padx=10, pady=10)
course_entry = Entry(data_frame)
course_entry.grid(row=1, column=7, padx=10, pady=10)

start_label = Label(data_frame, text="Start")
start_label.grid(row=1, column=8, padx=10, pady=10)
start_entry = Entry(data_frame)
start_entry.grid(row=1, column=9, padx=10, pady=10)

# Command Buttons
button_frame  = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

add_button = Button(button_frame, text="Add Record", command=add_record)
add_button.grid(row=0, column=0, padx=10, pady=10)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=1, padx=10, pady=10)

remove_record = Button(button_frame, text="Remove Record", command=remove_one)
remove_record.grid(row=0, column=2, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=3, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down",command=down)
move_down_button.grid(row=0, column=4, padx=10, pady=10)

clear_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
clear_button.grid(row=0, column=5, padx=10, pady=10)






# Bind the Treeview
my_tree.bind("<ButtonRelease-1>", select_record)





query_database()



root.mainloop()
