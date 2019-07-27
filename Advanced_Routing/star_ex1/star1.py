from bottle import run, static_file, error,route


@error(404)
def page_not_found(error):
    return static_file('404.html', root='')

@route('/')
def index():
    return static_file('index.html', root = '')

run(host='localhost', port=7000, debug=True)
