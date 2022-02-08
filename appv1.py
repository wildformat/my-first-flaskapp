from flask import Flask
import requests
import psycopg2
params = {
    "host": "127.0.0.1",
    "port": 5432,
    "database": "fee",
    "user": "child",
    "password": "password"     
}
conn = psycopg2.connect(**params)
#create a cursor to run a query for testing the connection
cursor = conn.cursor()

cursor.execute("select version()")

print(cursor.fetchone())

cursor.close()

app = Flask(__name__)
@app.route("/") #location of service implemented by my_function
def my_function():
    return("hello Liz, from v1")

@app.route("/call")
def call():
    req2 = requests.get(url="http://app_v2:5000/")
    req3 = requests.get(url="http://app_v3:5000/")
    req4 = requests.get(url="http://app_v4:5000/")
    return(req2.text + "\n" + req3.text + "\n" +req4.text + "\n")
