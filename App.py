from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my website"

@app.route('/contact')
def Contact_page():
    return "This is contact page"

@app.route('/home')
def Home_page():
    return "This is home page"

@app.route('/gallery')
def Gallery_page():
    return "This is gallery"


if __name__=="__main__":
    app.run()