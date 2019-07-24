from bottle import route, run, template
import json

import random


@route('/')
def getDictionary():
    lucky_number = random.randint(0, 100)

    dictionary = {
        "name": "Israel Tech Challnege",
        "address": "Shoken 18",
        "isNonProfit": True,
        "num_of_programs": 5,
        "your_lucky_number": lucky_number
    }

    return json.dumps(dictionary)


if __name__ == "__main__":
    run(host='localhost', port=7000, debug=True)
