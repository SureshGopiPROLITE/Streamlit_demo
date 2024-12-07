# from flask import Flask, request, jsonify, render_template
# from logic import add, subtract, multiply, divide

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/api/add', methods=['POST'])
# def api_add():
#     data = request.get_json()
#     num1 = data['num1']
#     num2 = data['num2']
#     result = add(num1, num2)
#     return jsonify({'result': result})

# @app.route('/api/subtract', methods=['POST'])
# def api_subtract():
#     data = request.get_json()
#     num1 = data['num1']
#     num2 = data['num2']
#     result = subtract(num1, num2)
#     return jsonify({'result': result})

# @app.route('/api/multiply', methods=['POST'])
# def api_multiply():
#     data = request.get_json()
#     num1 = data['num1']
#     num2 = data['num2']
#     result = multiply(num1, num2)
#     return jsonify({'result': result})

# @app.route('/api/divide', methods=['POST'])
# def api_divide():
#     data = request.get_json()
#     num1 = data['num1']
#     num2 = data['num2']
#     try:
#         result = divide(num1, num2)
#         return jsonify({'result': result})
#     except ValueError as e:
#         return jsonify({'error': str(e)}), 400

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
from logic import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/api/add', methods=['POST'])
def api_add():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = add(num1, num2)
    return jsonify({'result': result})

@app.route('/api/subtract', methods=['POST'])
def api_subtract():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = subtract(num1, num2)
    return jsonify({'result': result})

@app.route('/api/multiply', methods=['POST'])
def api_multiply():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = multiply(num1, num2)
    return jsonify({'result': result})

@app.route('/api/divide', methods=['POST'])
def api_divide():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    try:
        result = divide(num1, num2)
        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

