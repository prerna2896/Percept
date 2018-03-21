# A program to create the tables for the inventory database.
# There are 4 tables to store the data in the inventory.

# Table Users
#    The username for the user
#    The password for the user

# Table Students
#   First Name of student
#   Middle Name of student
#   Last Name of student
#   Age of student
#   University of student
#   Year of student
#   Stream of student

# Table Mentors
#   First Name of mentor
#   Middle Name of mentor
#   Last Name of mentor
#   Age of mentor
#   Profession of mentor
#   Experience of mentor
#   Interest of mentor

import sqlite3

# Create a connection with the database
conn = sqlite3.connect('Percept.db')

# cur is used to talk to the database
# cur.execute(Query) will execute queries
cur = conn.cursor()

#Create a table for the users with the login credentials of the user
#   username and password
cur.execute("Create Table Users(" + 
                "Username VARCHAR(100) PRIMARY KEY, " +
                "password VARCHAR(100) NOT NULL);")

conn.commit()

#Create a table for the details of student
#   first name, middle name, last name, age, university, year, stream
cur.execute("Create Table Students(" + 
                "FirstName VARCHAR(100) NOT NULL, " +
                "MiddleName VARCHAR(100), " + 
                "LastName VARCHAR(100) NOT NULL, " + 
                "age INT NOT NULL, " +
                "University VARCHAR(100) NOT NULL, " +
                "year INT NOT NULL, " +
                "stream VARCHAR(100) NOT NULL, "
                "Username VARCHAR(100) PRIMARY KEY, " +
                "FOREIGN KEY(Username) REFERENCES Users(Username));" )
conn.commit()

#Create a table for the details of mentor
#   first name, middle name, last name, age, profession, experience, interest
cur.execute("Create Table Mentors(" + 
                "FirstName VARCHAR(100) NOT NULL, " +
                "MiddleName VARCHAR(100), " + 
                "LastName VARCHAR(100) NOT NULL, " + 
                "age INT NOT NULL, " +
                "Profession VARCHAR(100) NOT NULL, " +
                "Experience INT NOT NULL, " +
                "Interest VARCHAR(100) NOT NULL, " +
                "Username VARCHAR(100) PRIMARY KEY, " +
                "FOREIGN KEY(Username) REFERENCES Users(Username));" )
conn.commit()