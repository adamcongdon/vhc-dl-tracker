import sqlite3

con = sqlite3.connect('data.db')

cur = con.curser()

#create table
cur.execute('''CREATE TABLE counts
                (date text, count text)''')

#insert data

#save (commit) changes

#close connection