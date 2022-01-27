from flask import Flask
import requests
app = Flask(__name__)
@app.route("/") #location of service implemented by my_function
def my_function():
    return("hello Liz, from v1")

@app.route("/call")
def call():
    req = requests.get(url="http://app_v2:5000/")
    return(req.text)

    