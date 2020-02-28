from flask import Flask
from flask import request
from flask_cors import CORS

from scheduling.views import fcfs


app = Flask(__name__)
cors = CORS(app, resources={r'/cpu-scheduling': {'origins': '*'}})


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/cpu-scheduling', methods=['POST', 'GET'])
def schedule_processes():
    data = request.get_json()
    fcfs(data=data)
    print(f'JSON: {data}')
    return {'results': 'kshdfh'}


if __name__ == '__main__':
    app.run()
