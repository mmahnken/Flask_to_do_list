"""
tipsy.py -- A flask-based todo list
"""

from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", user_name="albymeono@gmail.com")

@app.route("/tasks")
def list_tasks():
	db = model.connect_db()
	tasks_from_db = model.get_tasks(db)
	return render_template("list_tasks.html", tasks=tasks_from_db)

@app.route("/new_task")
def new_task():
	return render_template("new_task.html")

@app.route("/save_task", methods=["POST"])
def save_task():
	title = request.form['title']
	db = model.connect_db()
	#Assume that all tasks are attached to user Christian Fernandez
	#task ID below
	task_id = model.new_task(db, title, 'Christian', 'Fernandez')
	return redirect("/tasks")

if __name__ == "__main__":
	app.run(debug=True) 