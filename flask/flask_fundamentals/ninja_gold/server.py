from flask import Flask, render_template, request, redirect, session, Markup
import random
app = Flask(__name__)
app.secret_key = "SSSHHHH secret key"
@app.route('/')
def app_home():
	if session.get('count_gold') is None:
		session['count_gold'] = 0
		session['moves'] = 0
		session['history'] = " "
	else:
		session['count_gold'] = session['count_gold']
		session['history'] = session['history']
		session['moves'] = session['moves']
	return render_template('/index.html', count=session['count_gold'], moves= session['moves'], history=session['history'])
@app.route('/process_money', methods=['POST'])
def process_money():
	if session['moves'] == 15 and session['count_gold'] >= 500:
		session.clear()
		seesion['message'] = "You won"
		return render_template('/index.html', message=session['message'])
	elif session['moves'] == 15 and session['count_gold'] < 500:
		session.clear()
		session['message'] = "You Lost"
		return render_template('/index.html', message=session['message'])
	if request.form['property'] == 'farm':
		session['count_gold'] += 10
		session['moves'] += 1
		session['history'] = Markup("<div class='green'>Earned 10 golds from the farm......Yay!</div>") +session['history']
	elif request.form['property'] == 'cave':
		session['count_gold'] += 15
		session['moves'] += 1
		session['history'] = Markup("<div class='green'>Earned 15 golds from the cave.....Yay!</div>") +session['history']
	elif request.form['property'] == 'house':
		session['count_gold'] += 20
		session['moves'] += 1
		session['history'] = Markup("<div class='green'>Earned 20 golds from the house... Yay!</div>")+session['history']
	elif request.form['property'] == 'casino':
		session['count_gold'] -= 50
		session['moves'] += 1
		session['history'] = Markup("<div class='red'>Entered a casino and lost 50 golds..ouch</div>")+session['history']
	print(session['history'])
	return redirect('/')
@app.route('/reset')
def destroy_session():
	if 'count_gold' and 'history' in session:
		print('key exists!')
	else:
		print("no"*50)
	session.clear()		# clears all keys
	# session.pop('count')		# clears a specific key
	return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)