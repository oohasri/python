from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response
@app.route('/<name>/<times>')          # The "@" decorator associates this route with the function immediately following
def hello(name,times):
    return render_template('name.html',some_name=name, num_times=int(times)) 
@app.route('/<uname>/<pwd>')
def my_details(uname,pwd):
	return f"Username is {uname} Password is {pwd}"
@app.route('/say/<uname>')
def my_friends(uname):
	return f"Hi {uname}!"
@app.route('/repeat/<count>/<name>')
def friends(count,name):
	return name *int(count)
@app.route('/display')
def display_list():
	users = [{'first_name' : 'Michael', 'last_name' : 'Choi'},
	{'first_name' : 'John', 'last_name' : 'Supsupin'},
	{'first_name' : 'Mark', 'last_name' : 'Guillen'},
	{'first_name' : 'KB', 'last_name' : 'Tonel'}]
	return render_template('index.html', user=users)
@app.errorhandler(404)
def error_handler(e):
    return "Page not found"
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
	app.run(debug=True)    # Run the app in debug mode.
