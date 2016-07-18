

import pyodbc

dsn = 'sampleDB'
user = 'dsusr'
password = 'Passw0rd'
database = 'sample'

con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
cnxn = pyodbc.connect(con_string)

cursor = cnxn.cursor()
cursor.execute("select course_id, title, dept_name, credits from [dbo].[course]")
row = cursor.fetchone()

if row:
	print row
