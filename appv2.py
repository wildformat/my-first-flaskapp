from flask import Flask
app = Flask(__name__)
@app.route("/") #location of service implemented by my_function
def my_function():
    return("hello Liz, from v2")
