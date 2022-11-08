import sqlite3
conn=sqlite3.connect("sqlite.db")

ins=('''
insert data student (st_name,st_class,st_email), VALUES ('harsh","12th","harsh@23gmail.com")
''')

conn.execute(ins)
conn.commit()
conn.close()