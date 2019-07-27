from bottle import run, route, template, get,static_file
import json
import sys

images = [
    "https://nuts.com/images/auto/801x534/assets/0efa260340dac6fe.jpg",
    "https://nuts.com/images/auto/228x152fill/assets/c6c3d4639d81f871.png",
    "https://goobjoog.com/wp-content/uploads/2015/10/loos-480x320.jpg",
    "https://www.ohnuts.com/noapp/showImage.cfm/group-medium/Macadamia%20In%20Shell1.jpg?b=GroupImages/cachedir/120.Macadamia%20In%20Shell1.jpg",
]

@route('/', method='GET')
def index():
    return template('index.html')
@route('/get_images')
def default():
    return json.dumps(images)

@get('/static/js/<filename:re:.*\.js>')
def stylesheets(filename):
    return static_file(filename, root='static/js')


run(host='localhost', port= 7000, debug= True)