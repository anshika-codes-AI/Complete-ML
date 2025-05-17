### building urls dynamically
### variable rule
### Jinja 2 template engine

## Why? -  once we get the name , we should be able to redirect it to a HTML page , and after that  we have to pass this information dynamically to  my HTML page and we will be able to display it.

### Jinja template engine
'''
Multiple ways to read the data sources from backend in HTML

{{ }} expression to print output in HTML
{%...%} conditions, loops
{#...#} single line comment

'''

from flask import Flask,render_template,request
## responsible to redirect to desired page
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<H1>Welcome to the flask course</H1>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


## variable rule - restricting a parameter w.r.t datatype 
# @app.route('/success/<int:score>') - type error
# @app.route('/success/<score>')
# @app.route('/success/<int:score>')
# def success(score):
#     return "The marks you got is "+str(score)


## Building URL dynamically 
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template('result.html',results=res)

## For loop 
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    exp = {'score' : score , 'res' : res}
    return render_template('result1.html',results=exp)

## If condition
@app.route('/successif/<int:score>')
def successif(score):
    res=""
    return render_template('result.html',results=score)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
