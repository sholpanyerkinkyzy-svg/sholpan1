from flask import Flask, request

app = Flask(__name__)

@app.route('/sum')
def sum_ab():
    a = 5
    b = 3
    return str(a + b)

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)