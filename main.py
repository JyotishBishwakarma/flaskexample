from flask import Flask, render_template
import random

app = Flask('app')

@app.route('/')
def hello_world():
  #return 'Hello, World!'
  numbers = f"{random.randint(1,49)} {random.randint(1,49)} {random.randint(1,49)} {random.randint(1,49)} {random.randint(1,49)} {random.randint(1,49)}".center(60," ")
  return render_template("index.html", numbers = numbers)

app.run(host='0.0.0.0', port=8080)
