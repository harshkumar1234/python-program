import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute(''' 
    create table student(
    st_id INT AUTO_INCREMENT PRIMARY KEY,
    st_name VARCHAR(50),
    st_class VARCHAR(10),
    st_email VARCHAR(30))
''')
# conn.close()
ins='''
insert into student(st_name,st_class,st_email) VALUES ('harsh','12th','harsh@123.com')
'''
conn.execute(ins)
conn.commit()
conn.close()



