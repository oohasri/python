from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)
app.secret_key = 'keet it secre'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect("/show")	# changed this line!
    # return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print("sss"*50)
    return render_template("show.html", name_on_template=session['name'], email_on_template=session['email'])
if __name__ == "__main__":
    app.run(debug=True)
