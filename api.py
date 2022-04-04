import os
from canvas_generator.generator import Generator
import datetime
from flask import Flask, request, send_file

app = Flask(__name__)

global g

@app.before_first_request
def init_generator():
    global g
    g = Generator()

@app.route('/')
def index():
    month = int(request.args['m']) if 'm' in request.args else 3
    day = int(request.args['d']) if 'd' in request.args else 31
    hour = int(request.args['h']) if 'h' in request.args else 0
    minute = int(request.args['min']) if 'min' in request.args else 4
    second = int(request.args['s']) if 's' in request.args else 48
    dt = datetime.datetime(2017, month, day, hour, minute, second)
    epoch = datetime.datetime.utcfromtimestamp(0)
    time = (dt - epoch).total_seconds() * 1000.0
    
    if not os.path.isfile(f"canvas/{time}.png"):
        g.generate_picture_from_time(time)

    return send_file(f"canvas/{time}.png", mimetype='image/png')

if __name__ == "__main__":
    app.run()

