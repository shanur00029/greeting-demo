from flask import request
from flask import jsonify
from flask import Flask
from flask import Flask, url_for, send_from_directory, request
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__ ,template_folder='static')

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/hello', methods=['POST'])
def hello():
    message = request.get_json(force=True)
    name = message['name']
    response = {
        'greeting': 'Hello   , ' + name + '  this deployment server is for personal learning purpose !'
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
