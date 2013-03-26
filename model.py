"""
model.py
"""

import sqlite3
import datetime

def connect_db():
	return sqlite3.connect("tipsy.db")

def new_user(db, email, password, first_name, last_name
	):
	c = db.cursor()
	query = """INSERT INTO Users VALUES (NULL, ?, ?, ?, ?)"""
	result = c.execute(query, (email, password, first_name, last_name))
	db.commit()
	return result.lastrowid

def authenticate(db, email, password):
		c = db.cursor()
		query = """SELECT * FROM Users WHERE email = ? AND password = ?"""
		c.execute(query, (email, password))
		result = c.fetchone()
		if result:
			fields = ["id", "email", "password", "first_name", "last_name"]
			print "successful you're logged in!"
			return dict(zip(fields, result))

		print "Sorry we couldn't find you!"
		return None

def new_task(db, title, first_name, last_name):
	c = db.cursor()
	query1= """SELECT id FROM Users WHERE first_name = ? AND last_name = ?"""
	c.execute(query1, (first_name, last_name))
	user_row = c.fetchone()
	user_id = user_row[0]
	created_at = datetime.datetime.now()
	query2 = """INSERT INTO Tasks VALUES (NULL, ?, ?, ?, NULL)"""
	result = c.execute(query2, (user_id, title, created_at))
	db.commit()
	return result.lastrowid

def get_user(db, user_id):
	c = db.cursor()
	query = """ SELECT * FROM Users WHERE id = ?"""
	c.execute(query, (user_id, ))
	result = c.fetchone()
	if result:
		fields = ["id", "email", "password", "first_name", "last_name"]
		return dict(zip(fields, result))
	return None

def complete_task(db, task_id):			
	c = db.cursor()
	finish_time = datetime.datetime.now()
	query = """UPDATE Tasks SET completed_at = ? WHERE id = ?"""
	result = c.execute(query, (finish_time, task_id))
	db.commit()
	return result.lastrowid

def get_tasks(db, user_id = None):
	"""GEt all the tasks matching the user_id, getting all the tasks in the system if the user_id is not provided. Returns the results as a list of dictionaries."""
	c = db.cursor()
	if user_id:
		query = """SELECT * FROM Tasks WHERE user_id = ?"""
		c.execute(query, (user_id, ))	
	else:
		query = """SELECT * FROM Tasks"""
		c.execute(query)
	tasks = []
	rows = c.fetchall()
	for row in rows:
		fields = ["id", "user_id", "title", "created_at", "completed_at"]
		value = dict(zip(fields, row))
		tasks.append(value)
	return tasks

def get_task(db, id):
	"""Gets a single task, given its id. Returns a dictionary of the task data."""
	c = db.cursor()
	query = """SELECT * FROM Tasks WHERE id = ?"""
	c.execute(query, (id, ))
	result = c.fetchone()
	if result:
		fields = ["id", "user_id", "title", "created_at", "completed_at"]
		return dict(zip(fields, result))

