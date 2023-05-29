from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello, welcome to the calculator!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    if num1 is None or num2 is None:
        return jsonify(error="Please provide 'num1' and 'num2' in the request body."), 400

    try:
        result = float(num1) + float(num2)
        return jsonify(result=result)
    except ValueError:
        return jsonify(error="Invalid input. Please provide numeric values for 'num1' and 'num2'."), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    if num1 is None or num2 is None:
        return jsonify(error="Please provide 'num1' and 'num2' in the request body."), 400

    try:
        result = float(num1) - float(num2)
        return jsonify(result=result)
    except ValueError:
        return jsonify(error="Invalid input. Please provide numeric values for 'num1' and 'num2'."), 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
