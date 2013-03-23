"""
tipsy.py -- A flask-based todo list
"""

from flask import Flask, render_template
import model

app = Flask(__name__)

@app.route("/")
def index():
	return "Woo I'm tipsy!"

if __name__ == "__main__":
	app.run(debug=True)