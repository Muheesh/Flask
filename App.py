from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my website"

@app.route('/contact')
def Contact_page():
    return render_template("contact.html")

@app.route('/home')
def Home_page():
    return render_template("home.html")

@app.route('/gallery')
def Gallery_page():
    return render_template("gallery.html")


if __name__=="__main__":
    app.run()