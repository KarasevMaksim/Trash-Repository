from flask import Flask, jsonify

app = Flask(__name__)
TOKEN = '123'

data = [
    {'title': 'SenkoSun',
     'desc': 'GET, POST'},
    {'title': 'Holo',
     'desk': 'PUT, DELETE'}
    ]

@app.route('/get-data')
def get_data():
    return jsonify(data)

@app.route('/add-data', methods=['POST'])
def add_data():
    pass

if __name__ == '__main__':
    Flask.run(app, debug=True)