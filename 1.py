from bottle import route, run, template,response
import sqlite3
from json import dumps
import mysql.connector
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
@route('/')
def index():
    #cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    # conn = sqlite3.connect('databas1.db')
    # c = conn.cursor()
    # c.execute("SELECT * from blog")
    # result = c.fetchall()
    # response.content_type = 'application/json'
    # return dumps(result)


    mydb = mysql.connector.connect(
     host="127.0.0.1",
     user="root",
     password="",
     database="localdatabase"
    )
    cur = mydb.cursor()
    cur.execute("SELECT * FROM blog")
    Result= cur.fetchall()
    response.content_type = 'application/json'
    mydb.close()
    return dumps(Result)




@route('/about')
def about():
    return '<h1>Hello It is test 2 Index page</h1>!'


@route('/contact')
def contact():
    return '<h1>Hello It is test 3 Index page</h1>!'


@route('/blog')
def blog():
    return '<h1>Hello It is test 4 Index page</h1>!'


@route('/login')
def login():
    return '<h1>Hello It is test 5 Index page</h1>!'


@route('/News')
def News():
    return '<h1>Hello It is test news Index page</h1>!'

@route('/faq')
def faq():
    return '<h1>Hello It is test news Index page</h1>!'

run(host='localhost', port=8080)
