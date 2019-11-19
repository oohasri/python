from flask import Flask, render_template, request, redirect # added request
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def display_result():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    lang_from_form = request.form['lang']
    comments_from_form = request.form['comments']
    gender_from_form = request.form['gender']
    interests_sports = request.form['sports']
    interests_foods = request.form['foods']
    print(gender_from_form)
    # interests_sport	= request.form['interests']
    return render_template("show.html", name=name_from_form, location=location_from_form, lang=lang_from_form, comments=comments_from_form, gender=gender_from_form, interests=interests_sports+" "+interests_foods)
if __name__ == "__main__":
    app.run(debug=True)