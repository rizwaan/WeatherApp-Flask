from flask import Flask
import os

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/goodbye")
def goodbye():
    return 'Goodbye world'

##Dynamic Routing

@app.route("/hello/<name>/<int:age>")
def hello_name(name,age):
    return "Hello! {}. You are {} years old. Bye".format(name,age)

if __name__=='__main__':

    app.run(debug=True)