from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Welcome to Flask demo</h1>'


@app.route('/customer/<name>')
def greet(name):
	return '<h1>Welcome ' + name.title() + '</h1>'


@app.route('/api/customer/<name>')
def api_greet(name):
	return jsonify({'message': 'Welcome {}'.format(name.title())})


if __name__ == '__main__':
	app.run(debug=True, port=8000)
