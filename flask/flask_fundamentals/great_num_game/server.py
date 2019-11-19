from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "SSSHHHH secret key"
@app.route('/')
def app_home():
	return render_template('/index.html')
@app.route('/guess_num', methods=['POST'])
def guess_num():
	if session.get('generated_num') is None:
		session['generated_num'] = random.randint(1, 100)
		session['count'] = 1
	else:
		session['generated_num'] = session['generated_num']
		if session['count']<5:
			session['count'] += 1
		else:
			session.clear()
			return render_template('/index.html', message="You lost the game :( Please try again!")
	session['user_num'] = request.form['num']
	print(f"system generated num is {session['generated_num']}")
	print(f"user entered num is {session['user_num']}")
	return redirect('/result')
@app.route('/result')
def result():
	session['generated_num']=session['generated_num']
	session['user_num'] = session['user_num']
	session['count'] = session['count']
	return render_template('/index.html',generated_num=session['generated_num'], user_num=session['user_num'], count=session['count'])
@app.route('/user_details')
def display_details():
	return render_template('/user_details.html')
@app.route('/leaderboard')
def l_board():
	return render_template('/leaderboard.html')
@app.route('/reset')
def destroy_session():
	if 'generated_num' and 'user_num' and 'count' in session:
		print('key exists!')
	else:
		print("no"*50)
	session.clear()		# clears all keys
	# session.pop('count')		# clears a specific key
	return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)