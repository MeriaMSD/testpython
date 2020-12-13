from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
@route('/')
def index():
    return '<h1>Hello It is Index page</h1>!'

































run(host='localhost', port=8080)
