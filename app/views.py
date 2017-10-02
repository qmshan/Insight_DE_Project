from flask import render_template

from app import app

@app.route('/')
def main():
  return render_template('main.html')
@app.route('/index')
def index():
  return render_template('index.html')
@app.route('/index2')
def index2():
  return render_template('index2.html')

