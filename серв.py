import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/<name>/<int:age>', methods=['GET', 'POST'])
def return_dic(name):
    nosj = open("test.json", encoding="utf-8")
    data = json.load(nosj)
    for i in data:
        if i["name"] == name:
            return jsonify(i)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
