from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Flask"

app.route('/cal', methods=['GET'])
def math_operator():
    operation=request.json("operation")
    number1=request.json("number1")
    number2=request.json("number2")

    if operation=='add':
        result=number1+number2
    elif operation=='subtract':
        result=number1-number2
    elif operation=='multiply':
        result=number1*number2
    else:
        result=number1/number2
    return "the operation is {} and the result is {}".format(operation, result)

print(__name__)

if __name__ == '__main__':
    app.run()