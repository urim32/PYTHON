from bottle import route, run, static_file
@route('/')
def index():
    return "hello world!"


def main():
    run(host='localhost', port=7000, debug=True)


if __name__ == "__main__":
    main()
