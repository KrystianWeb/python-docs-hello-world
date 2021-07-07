from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/squared", methods=['POST'])
def squared_value():
    if 'number' in request.args:
        number = int(request.args['number'])
    else:
        return "Error: No number field provided. Please specify a number."
    
    return jsonify(number*number)

#app.run()