from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r'/cpu-scheduling': {"origins": "*"}})


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/cpu-scheduling', methods=['post', 'get'])
def schedule_processes():
    return 'sksdvk'
    # return ['hello', 'world']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
