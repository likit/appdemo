from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Welcome to Flask demo</h1>'


@app.route('/customer/<name>')
def greet(name):
	return '<h1>Welcome ' + name.title() + '</h1>'

@app.route('/services')
def show_services():
	return '<ul><li>Glucose</li><li>Cholesterol</li></ul>'


@app.route('/api/customer/<name>')
def api_greet(name):
	return jsonify({'data': 'Welcome {}'.format(name.title())})


if __name__ == '__main__':
	app.run(debug=True, port=8000)
