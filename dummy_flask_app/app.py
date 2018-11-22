import requests
from  flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/") 
def hello():
    return render_template("hello.html")


@app.route("/foo")
def foo():
   return "Your lucky number is :{}".format(random.randint())

if __name__ == "__main__":
    app.run()
