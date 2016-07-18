
# connect to MS SQL server
# fetch the data from table and store it into csv file

import pymssql  
import sys
import csv
    
SRVR='127.0.0.1'
USR='dsusr'	
PWD='Passw0rd'
DB='sample'

try:
	conn = pymssql.connect(server=SRVR, user=USR, password=PWD, database=DB)
except :
	print "Error", sys.exc_info()[0]
	exit()

cursor = conn.cursor()  
cursor.execute("select course_id, title, dept_name, credits from [dbo].[course]")

"""
with open('output_file.csv', 'wb') as fout:
    writer = csv.writer(fout)
    writer.writerow([ i[0] for i in cursor.description ]) # heading row
    writer.writerows(cursor.fetchall())
"""

csv_out = open('mycsv.csv', 'wb')
mywriter = csv.writer(csv_out)
mywriter.writerow([ i[0] for i in cursor.description ]) # heading row

"""
row = cursor.fetchone()  
while row:  
	print row
	mywriter.writerow(row)
	row = cursor.fetchone()
"""

rows = cursor.fetchmany(10)  
while rows:  
	print rows
	mywriter.writerows(rows)
	rows = cursor.fetchmany(10)

csv_out.close()	



