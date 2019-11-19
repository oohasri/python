from django.shortcuts import render, redirect
def index(request):
	if request.session.get('count_gold') is None:
		request.session['count_gold'] = 0
		request.session['moves'] = 0
		request.session['history'] = " "
	else:
		request.session['count_gold'] = request.session['count_gold']
		request.session['history'] = request.session['history']
		request.session['moves'] = request.session['moves']
	return render(request, "first_app/index.html")

def process_money(request):
	if request.session['moves'] == 15 and request.session['count_gold'] >= 500:
		request.session.clear()
		request.session['message'] = "You won"
		return render(request,'first_app/index.html')
	elif request.session['moves'] == 15 and request.session['count_gold'] < 500:
		request.session.clear()
		request.session['message'] = "You Lost"
		return render(request,'first_app/index.html')
	if request.POST['property'] == 'farm':
		request.session['count_gold'] += 10
		request.session['moves'] += 1
		request.session['history'] = "<div class='green'>Earned 10 golds from the farm......Yay!</div>" +request.session['history']
	elif request.POST['property'] == 'cave':
		request.session['count_gold'] += 15
		request.session['moves'] += 1
		request.session['history'] = "<div class='green'>Earned 15 golds from the cave.....Yay!</div>" +request.session['history']
	elif request.POST['property'] == 'house':
		request.session['count_gold'] += 20
		request.session['moves'] += 1
		request.session['history'] = "<div class='green'>Earned 20 golds from the house... Yay!</div>"+request.session['history']
	elif request.POST['property'] == 'casino':
		request.session['count_gold'] -= 50
		request.session['moves'] += 1
		request.session['history'] = "<div class='red'>Entered a casino and lost 50 golds..ouch</div>"+request.session['history']
	print(request.session['history'])
	return redirect('/')

def destroy(request):
	request.session.clear()		# clears all keys
	# session.pop('count')		# clears a specific key
	return redirect('/')
# Create your views here.
