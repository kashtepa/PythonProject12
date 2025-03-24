import response
import json
from flask import Flask

from flask import request
app = Flask(__name__)




@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'


@app.route('/submit', methods=['POST'])
def submit():
  name = request.form['name']
  return f'Hello, {name}'


@app.route('/httpbin')
def postHttpbin():
  return  json.loads(response.postHttpbin().text)


if __name__ == '__main__':
    app.run()