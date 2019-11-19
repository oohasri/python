from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/<x>')
def num_times(x):
	return render_template('index.html', num_times=int(x))
@app.route('/<x>/<y>')
def x_y(x,y):
	return render_template('index.html', rows=int(x), num_times=int(y))
@app.route('/<x>/<y>/<color1>/<color2>')
def color_checks(x,y,color1,color2):
	return render_template('index.html', rows=int(x), num_times=int(y), color_one=color1, color_two=color2)
@app.errorhandler(404)
def error_handler(e):
	return "Page Not Found"
if __name__=="__main__":
	app.run(debug=True)