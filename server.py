# Set up server
from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/4')
def index2():
    return render_template("index2.html")

@app.route('/10/10')
def index3():
    return render_template("index3.html")

@app.route('/success')
def success():
    return "Success"

if __name__=="__main__":
    app.run(debug=True)
    