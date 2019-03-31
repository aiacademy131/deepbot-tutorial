#!/usr/bin/python
# -*- coding: utf-8 -*
'''
api.py: DeepBot Api Server
'''

import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/chatting', methods=['GET', 'POST'])
def chatting():
    okt = Okt()
    message = request.json['message']
    return jsonify({'message': message})


if __name__ == '__main__':
    app.run(debug=True)
