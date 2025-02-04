from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/about')
def about():
    name = request.args.get('name', 'Guest')
    return f"This is the Flask API about page. Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)