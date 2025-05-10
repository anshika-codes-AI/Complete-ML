from flask import Flask

'''
It creates an instance of the Flask class,
which will be our WSGI(web server gateway interface) application.
'''

## WSGI application
app = Flask(__name__) ## parameter - entry point

 # when this route is hit , this welcome function will be executed
@app.route("/")
def welcome():
    return "Welcome to this Flask Course."

@app.route("/index")
def index():
    return "Welcome to the index page."

## Entry point for execution.
if __name__ == "__main__":
    app.run(debug = True)