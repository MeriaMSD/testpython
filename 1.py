from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
@route('/')
def index():
    return '<h1>Hello It is Index page</h1>!'


@route('/about')
def about():
    return '<h1>Hello It is test 2 Index page</h1>!'


@route('/contact')
def index():
    return '<h1>Hello It is test 3 Index page</h1>!'


@route('/blog')
def index():
    return '<h1>Hello It is test 4 Index page</h1>!'


@route('/login')
def index():
    return '<h1>Hello It is test 5 Index page</h1>!'


@route('/News')
def index():
    return '<h1>Hello It is test news Index page</h1>!'

@route('/faq')
def faq():
    return '<h1>Hello It is test news Index page</h1>!'

run(host='localhost', port=8080)
