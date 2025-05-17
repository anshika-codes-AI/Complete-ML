from flask import Flask,render_template,request
## responsible to redirect to desired page
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<H1>Welcome to the flask course</H1>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)