import sqlite3

## Connect to sqlite
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record,create table
cursor=connection.cursor()

## Create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute("""Insert Into Student values("Zeeshan","Data Science","A",90)""")
cursor.execute("""Insert Into Student values("Essa","Data Science","A",92)""")
cursor.execute("""Insert Into Student values("Manshah","Data Science","A",93)""")
cursor.execute("""Insert Into Student values("Shahab","Artifical Intelligence","A",95)""")
cursor.execute("""Insert Into Student values("Talal","Data Science","A",85)""")
cursor.execute("""Insert Into Student values("Ahmed","Data Science","A",89)""")


## Display all the records
print("The inserted records are")
data=cursor.execute("""Select * from STUDENT""")
for row in data:
    print(row)

## Commit you changes
connection.commit()
connection.close()