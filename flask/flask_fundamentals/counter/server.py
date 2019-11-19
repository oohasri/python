from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "SSSHHHH secret key"
@app.route('/')
def app_home():
	session['count'] = 0
	session['page_visited'] = 0
	return redirect('/count')
@app.route('/count')
def count():
	session['count'] += 1
	session['page_visited'] += 1
	print(session['count'])
	return render_template(request,'index.html')
@app.route('/add2')
def add_2():
	session['count'] += 1
	session['page_visited'] = session['page_visited']
	return redirect('/count')
@app.route('/count_increment', methods=['POST'])
def countIncrement():
	c = request.form['count']
	print(c*40)
	print(session['count'])
	session['page_visited'] = session['page_visited']
	session['count'] = session['count'] + int(c) - 1
	return redirect('/count')
@app.route('/destroy_session')
def destroy_session():
	print('count')
	if 'count' in session:
		print('key exists!')
	else:
		print("no"*50)
	# session.clear()		# clears all keys
	session.pop('count')		# clears a specific key
	return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)