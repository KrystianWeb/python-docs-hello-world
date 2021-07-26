from flask import Flask, request, jsonify, render_template, url_for
import pandas as pd
app = Flask(__name__)

#---------dummy data----------
list = [
    {
        'author': 'Author 1',
        'title': 'Title 1',
        'content': 'Bla bla bla',
        'date': 'Date 1'
    },
    {
        'author': 'Author 2',
        'title': 'Title 2',
        'content': 'Bla bla bla 2',
        'date': 'Date 2'
    },
    {
        'author': 'Author 3',
        'title': 'Title 3',
        'content': 'Bla bla bla 3',
        'date': 'Date 3'
    }

]
#-----------------------------

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', list=list, title='TEST')

@app.route("/test")
def test():
    return jsonify(list)

@app.route("/squared", methods=['POST','GET'])
def squared_value():
    if 'number' in request.args:
        number = int(request.args['number'])
    else:
        return "Error: No number field provided. Please specify a number."
    
    return jsonify(number*number)

if __name__ == '__main__':
    app.run(debug=True)