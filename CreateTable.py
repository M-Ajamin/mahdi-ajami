import sqlite3

conn = sqlite3.connect('mahdi.db')
c = conn.cursor()

c.execute("CREATE TABLE students (ID int PRIMARY KEY NOT NULL ,name nvarchar(50) NOT NULL ,family nvarchar(50) NOT NULL )")
c.execute("CREATE TABLE Professors (Code int PRIMARY KEY NOT  NULL ,name nvarchar(50) NOT NULL ,family nvarchar(50) NOT NULL ,rate varchar NOT NULL )")
c.execute("CREATE TABLE Courses (Code int PRIMARY KEY NOT NULL ,name nvarchar(50) NOT NULL ,unit int NOT NULL ,PCode int NOT NULL )")
c.execute("CREATE TABLE Marks (id int, ms int ,Mark double(3) )")
conn.commit()
conn.close()