from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('count.html')
@app.route('/play/<x>')
def x_times(x):
	return render_template('count.html',num_times=int(x))
@app.route('/play/<x>/<color>')
def color(x,color):
	return render_template('count.html',num_times=int(x),color=color)
@app.errorhandler(404)
def error_handler(e):
    return "Page not found"
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
	app.run(debug=True)    # Run the app in debug mode.