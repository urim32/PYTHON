from bottle import run, static_file, route, template, get
import json

@route('/')
def index():
  return template('index.html')

  
@route('/static/css/<filename:re:.*\.css>')
def css(filename):
    return static_file(filename,  root='static/css')


@route('/static/js/<filename:re:.*\.js>')
def js(filename):
    return static_file(filename,  root='static/js')


@route('/img/<filename:re:.*\.(jpg|png)>')
def images(filename):
  return static_file(filename, root='img')

if __name__ == "__main__":
    run(host='localhost', port = 7000, debug = True)