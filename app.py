from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Welcome to Flask demo</h1>'


@app.route('/customer/<name>')
def greet(name):
	return '<h1>Welcome ' + name.title() + '</h1>'


if __name__ == '__main__':
	app.run(debug=True, port=8000)
