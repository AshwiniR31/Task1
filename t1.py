# import streamlit as st
# import sqlite3
# from sqlite3 import Error

# # Function to create a database connection
# def create_connection(db_file):
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#     except Error as e:
#         st.error(e)
#     return conn

# # Function to create user table
# def create_user_table(conn):
#     try:
#         c = conn.cursor()
#         c.execute('''CREATE TABLE IF NOT EXISTS users
#                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                      name TEXT NOT NULL,
#                      email TEXT NOT NULL UNIQUE,
#                      contact TEXT NOT NULL,
#                      password TEXT NOT NULL)''')
#     except Error as e:
#         st.error(e)

# # Function to create bed availability table
# def create_bed_table(conn):
#     try:
#         c = conn.cursor()
#         c.execute('''CREATE TABLE IF NOT EXISTS beds
#                      (bed_number TEXT PRIMARY KEY,
#                      available BOOLEAN)''')
#     except Error as e:
#         st.error(e)

# # Function to insert user into the database
# def insert_user(conn, name, email, contact, password):
#     try:
#         c = conn.cursor()
#         c.execute("INSERT INTO users (name, email, contact, password) VALUES (?, ?, ?, ?)",
#                   (name, email, contact, password))
#         conn.commit()
#         st.success("User registered successfully!")
#     except Error as e:
#         st.error(e)

# # Function to check if user exists in the database
# def user_exists(conn, email, password):
#     try:
#         c = conn.cursor()
#         c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
#         row = c.fetchone()
#         if row:
#             return True
#         else:
#             return False
#     except Error as e:
#         st.error(e)
#         return False

# # Function to initialize bed availability table
# def initialize_bed_availability(conn):
#     try:
#         c = conn.cursor()
#         c.execute("DELETE FROM beds")
#         bed_data = [("Bed 1", True), ("Bed 2", True), ("Bed 3", True), ("Bed 4", True), ("Bed 5", True), ("Bed 6", True)]
#         c.executemany("INSERT INTO beds (bed_number, available) VALUES (?, ?)", bed_data)
#         conn.commit()
#     except Error as e:
#         st.error(e)

# # Function to update bed availability in the database
# def update_bed_availability(conn, bed_number, availability):
#     try:
#         c = conn.cursor()
#         c.execute("UPDATE beds SET available=? WHERE bed_number=?", (availability, bed_number))
#         conn.commit()
#     except Error as e:
#         st.error(e)

# # Main function
# def main():
#     # Database initialization
#     conn = create_connection("hostel.db")
#     if conn is not None:
#         create_user_table(conn)
#         create_bed_table(conn)

#     # Page navigation logic
#     page = st.sidebar.selectbox("Navigation", ["Register", "Login"])
#     if page == "Register":
#         st.title("Registration")
#         name = st.text_input("Name")
#         email = st.text_input("Email")
#         contact = st.text_input("Contact Number")
#         password = st.text_input("Password", type="password")
#         if st.button("Register"):
#             if conn is not None:
#                 insert_user(conn, name, email, contact, password)

#     elif page == "Login":
#         st.title("Login")
#         email = st.text_input("Email")
#         password = st.text_input("Password", type="password")
#         if st.button("Login"):
#             if conn is not None:
#                 if user_exists(conn, email, password):
#                     st.success("Login successful!")
#                     initialize_bed_availability(conn)
#                     show_bed_availability(conn)
#                 else:
#                     st.error("Invalid email or password")

# # Function to display bed availability
# def show_bed_availability(conn):
#     st.title("Bed Availability")
#     c = conn.cursor()
#     c.execute("SELECT * FROM beds")
#     beds = c.fetchall()
#     for bed in beds:
#         st.write(f"{bed[0]} - {'Available' if bed[1] else 'Not Available'}")

# if __name__ == "__main__":
#     main()

import streamlit as st
import sqlite3
from sqlite3 import Error

# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        st.error(e)
    return conn

# Function to create user table
def create_user_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     name TEXT NOT NULL,
                     email TEXT NOT NULL UNIQUE,
                     contact TEXT NOT NULL,
                     password TEXT NOT NULL)''')
    except Error as e:
        st.error(e)

# Function to create bed availability table
def create_bed_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS beds
                     (bed_number TEXT PRIMARY KEY,
                     available BOOLEAN)''')
    except Error as e:
        st.error(e)

# Function to insert user into the database
def insert_user(conn, name, email, contact, password):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO users (name, email, contact, password) VALUES (?, ?, ?, ?)",
                  (name, email, contact, password))
        conn.commit()
        st.success("User registered successfully!")
    except Error as e:
        st.error(e)

# Function to check if user exists in the database
def user_exists(conn, email, password):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        row = c.fetchone()
        if row:
            return True
        else:
            return False
    except Error as e:
        st.error(e)
        return False

# Function to initialize bed availability table
def initialize_bed_availability(conn):
    try:
        c = conn.cursor()
        c.execute("DELETE FROM beds")
        bed_data = [("Bed 1", True), ("Bed 2", True), ("Bed 3", True), ("Bed 4", True), ("Bed 5", True), ("Bed 6", True)]
        c.executemany("INSERT INTO beds (bed_number, available) VALUES (?, ?)", bed_data)
        conn.commit()
    except Error as e:
        st.error(e)

# Function to update bed availability in the database
def update_bed_availability(conn, bed_number, availability):
    try:
        c = conn.cursor()
        c.execute("UPDATE beds SET available=? WHERE bed_number=?", (availability, bed_number))
        conn.commit()
    except Error as e:
        st.error(e)

# Main function
def main():
    
    # Database initialization
    conn = create_connection("hostel.db")
    if conn is not None:
        create_user_table(conn)
        create_bed_table(conn)

    # Page navigation logic
    page = st.sidebar.selectbox("Navigation", ["Register", "Login"])
    if page == "Register":
        # st.title("Hostel MAnagement System")
        st.title("Registration")
        name = st.text_input("Name")
        email = st.text_input("Email")
        contact = st.text_input("Contact Number")
        password = st.text_input("Password", type="password")
        if st.button("Register"):
            if conn is not None:
                insert_user(conn, name, email, contact, password)

    elif page == "Login":
        # st.title("Hostel MAnagement System")
        st.title("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if conn is not None:
                if user_exists(conn, email, password):
                    st.success("Login successful!")
                    initialize_bed_availability(conn)
                    book_bed(conn)
                else:
                    st.error("Invalid email or password")

# Function to book beds
def book_bed(conn):
    st.title("Bed Booking")

    c = conn.cursor()
    c.execute("SELECT bed_number FROM beds WHERE available=1")
    available_beds = c.fetchall()
    available_bed_numbers = [bed[0] for bed in available_beds]

    selected_bed = st.selectbox("Select a bed", available_bed_numbers)

    if st.button("Book"):
        if selected_bed:
            update_bed_availability(conn, selected_bed, False)
            st.success(f"You have successfully booked {selected_bed}!")
        else:
            st.error("Please select a bed")

if __name__ == "__main__":
    main()
