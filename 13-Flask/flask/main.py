from flask import Flask,render_template
## responsible to redirect to desired page
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<H1>Welcome to the flask course</H1>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)