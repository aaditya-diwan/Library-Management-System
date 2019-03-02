import sqlite3


def connect():
	conn=sqlite3.connect("books1.db")
	curr=conn.cursor()
	curr.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,ISBN INTEGER)")
	conn.commit()
	conn.close()


def insert(title,author,year,ISBN):
	conn=sqlite3.connect("books.db")
	curr=conn.cursor()
	curr.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,ISBN))
	conn.commit()
	conn.close()

def view():
	conn=sqlite3.connect("books.db")
	curr=conn.cursor()
	curr.execute("SELECT * FROM book")
	rows=curr.fetchall()
	conn.close()
	return rows

def Search(title="",year="",author="",ISBN=""):
	conn=sqlite3.connect("books.db")
	curr=conn.cursor()
	curr.execute("SELECT * FROM book WHERE title=? OR author=? OR ISBN=? OR year=?",(title,author,ISBN,year))
	rows=curr.fetchall()
	conn.close()
	return rows

def Delete(id):
	conn=sqlite3.connect("books.db")
	curr=conn.cursor()
	curr.execute("DELETE FROM book WHERE id=?",(id,))
	conn.commit()
	conn.close()

def update(id,title,author,year,ISBN):
	conn=sqlite3.connect("books.db")
	curr=conn.cursor()
	curr.execute("UPDATE book SET title=?,author=?,year=?,ISBN=? WHERE id=?",(title,author,year,ISBN,id))
	conn.commit()
	conn.close()

connect()


