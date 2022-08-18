'''
Created on Aug 10, 2022

@author: nstru
'''

import sqlite3
import tkinter as Tk

root = Tk.Tk()
root.title("Learning tkinter Databases")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table

'''
Commented out because table only needs to be created once
c.execute("""CREATE TABLE addresses (
        first_name text, 
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
    )""")
'''


# Create functions for database

# Create function to Delete a Record
def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()    

    # Delete a record
    c.execute("DELETE from addresses WHERE oid= " + sel_box.get())
    
    conn.commit()
    conn.close()

# Create a function to save edits
def update():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()   

    record_id = sel_box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid = :oid""",
        {
            'first': f_name_editor.get(),
            'last': l_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode': zipcode_editor.get(),
            'oid': record_id
        }
    )
        
    conn.commit()
    conn.close()
    
    editor.destroy()

# Create Edit Function to update a record
def edit():
    global editor
    editor = Tk.Tk()
    editor.title('Update a Record')
    
    # Create Global Variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    
    f_name_editor = Tk.Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Tk.Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Tk.Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Tk.Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Tk.Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Tk.Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)
    
    # Create Text Box Labels
    f_name_label_ed = Tk.Label(editor, text="First Name")
    f_name_label_ed.grid(row=0, column=0, pady=(10, 0))
    l_name_label_ed = Tk.Label(editor, text="Last Name")
    l_name_label_ed.grid(row=1, column=0)
    address_label_ed = Tk.Label(editor, text="Address")
    address_label_ed.grid(row=2, column=0)
    city_label_ed = Tk.Label(editor, text="City")
    city_label_ed.grid(row=3, column=0)
    state_label_ed = Tk.Label(editor, text="State")
    state_label_ed.grid(row=4, column=0)
    zipcode_label_ed = Tk.Label(editor, text="Zipcode")
    zipcode_label_ed.grid(row=5, column=0)
    
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    
    record_id = sel_box.get()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    
    # Loop Through Results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
 
    # Create Save Button to save edited record
    save_btn = Tk.Button(editor, text="Save Record", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    
# Create Submit Function
def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    

    # Insert Into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            }
              
        )
    
    conn.commit()
    conn.close()
    
    # Clear the Text Boxes
    f_name.delete(0, Tk.END)
    l_name.delete(0, Tk.END)
    address.delete(0, Tk.END)
    city.delete(0, Tk.END)
    state.delete(0, Tk.END)
    zipcode.delete(0, Tk.END)
    
# Create Query Function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    
    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    
    # Loop Through Results
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"
        
    query_label = Tk.Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)
    
    
    # Commit Changes and Close Connection
    conn.commit()
    conn.close()
    

# Text Boxes: First name, last name, address, city, state, zip
f_name = Tk.Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Tk.Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Tk.Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Tk.Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Tk.Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Tk.Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)
sel_box = Tk.Entry(root, width=30)
sel_box.grid(row=8, column=1, pady=5)

# Create Text Box Labels
f_name_label = Tk.Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Tk.Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Tk.Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Tk.Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Tk.Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Tk.Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
sel_box_label = Tk.Label(root, text="ID Number")
sel_box_label.grid(row=8, column=0, pady=5)

# Create Submit Button
sub_button = Tk.Button(root, text="Add Record to Database", command=submit)
sub_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create Query Button
query_button = Tk.Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Create Delete Button
sel_button = Tk.Button(root, text="Select Record", command=delete)
sel_button.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Create Update Button
edit_btn = Tk.Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=133)

# Commit Changes
conn.commit()

# Close Connection
conn.close()


root.mainloop()